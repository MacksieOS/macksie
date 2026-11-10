#!/usr/bin/env python3
"""Offline checks for this repository's Markdown subset; Python 3.10+, stdlib only.

Checks inline local links and ATX heading fragments, fenced blocks, and the simple
quoted-scalar issue frontmatter used here. Not a full Markdown or YAML parser.
"""

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)\)")


def prose(text):
    """Remove fenced content and return whether all fences were closed."""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token
                continue
            if token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                fence = None
                continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence is None


def anchors(text):
    result = set()
    counts = {}
    for heading in re.findall(r"^#{1,6} (.+)$", prose(text)[0], re.MULTILINE):
        heading = re.sub(r"\s+#+\s*$", "", heading).lower()
        slug = "".join(c for c in heading if c.isalnum() or c in " _-")
        slug = slug.replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def check(root):
    # Include new files before staging, but ignore generated and Git-ignored files.
    names = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=root,
    ).decode("utf-8").split("\0")
    files = sorted({root / name for name in names if name.endswith(".md")})
    errors = []
    for path in files:
        if not path.is_file():
            continue  # A staged or working-tree deletion is not an unreadable document.
        text = path.read_text(encoding="utf-8")
        body, closed = prose(text)
        label = path.relative_to(root)
        if not closed:
            errors.append(f"{label}: unclosed fenced block")
        for target in LINK.findall(body):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not destination.is_relative_to(root):
                errors.append(f"{label}: link escapes repository: {target}")
            elif not destination.exists():
                errors.append(f"{label}: missing link target: {target}")
            elif url.fragment and destination.suffix == ".md":
                if unquote(url.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"{label}: missing heading fragment: {target}")
        if path.parent == root / ".github" / "ISSUE_TEMPLATE":
            parts = text.split("---\n", 2)
            if len(parts) != 3 or parts[0]:
                errors.append(f"{label}: missing opening YAML frontmatter")
                continue
            metadata = {}
            for line in parts[1].splitlines():
                match = re.fullmatch(r'([a-z]+): (".*")', line)
                if not match:
                    errors.append(f"{label}: use one JSON-quoted scalar per metadata line")
                    continue
                key, value = match.groups()
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    errors.append(f"{label}: invalid quoted value for {key}")
                    continue
                if key in metadata:
                    errors.append(f"{label}: duplicate metadata key: {key}")
                metadata[key] = value
            for key in ("name", "about"):
                if not metadata.get(key, "").strip():
                    errors.append(f"{label}: missing nonempty {key}")
    return files, errors


if __name__ == "__main__":
    documents, problems = check(ROOT)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print(f"Documentation checks passed ({len(documents)} Markdown files).")
