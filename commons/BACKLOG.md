# First Commons implementation backlog

**Status: scoped proposal for review; no application features are implemented.**
This breaks the [Commons brief](README.md) and [roadmap](../docs/ROADMAP.md) into
small tasks. IDs below are planning IDs, not existing GitHub issue numbers. Copy
one task into the [task template](../.github/ISSUE_TEMPLATE/task.md), link dependencies,
and attach acceptance evidence to its PR. No owners or delivery dates are assigned.

## Milestone boundary

Commons v0.1 is a local prototype: a reader finds a sourced knowledge entry and
inspects its history; a local test contributor creates and corrects entries. The
first code PR is **C2**, after C0 and C1 establish the minimum contract and fixtures.
It demonstrates persistent create/read behavior without requiring search or a UI.

Use one local test operator and synthetic attribution initially; no public signup
or internet-facing write endpoint. This is a prototype boundary, not a production
identity or governance decision. C0 must document how the chosen runner enforces it.

Exclude payments, compensation, Time/Talent/Treasure accounting, recruitment,
government integrations, crawling, federation, DNS, and a complete shared Core.
The neighborhood road/lighting example can inform a sourced knowledge fixture;
project proposals and factual entries must remain distinguishable if an actionable
project type is proposed later. This milestone does not choose that product model.

## Common acceptance criteria

These apply to every implementation task where relevant. A task cannot claim full
international support merely because it passes a few fixtures.

- Preserve Unicode text and stable identifiers independent of titles or language.
  Record content language using [BCP 47 language tags](https://www.rfc-editor.org/rfc/rfc5646).
  Test accented Latin, Arabic (right-to-left), and CJK text. Do not infer language,
  country, citizenship, or currency from each other.
- Store revision instants unambiguously using
  [RFC 3339 timestamps](https://www.rfc-editor.org/rfc/rfc3339), with an explicit
  offset or UTC. Keep publication dates distinct from revision instants; do not
  fabricate a day or time when a source gives only a year. UI formatting is separate.
- Geography is optional. Do not require country/state/county/ZIP or a US address.
  Omit location from the initial contract unless needed; if introduced, specify a
  flexible region reference in an ADR and test different administrative structures.
  Do not collect a contributor's precise location. Units and currencies are deferred;
  any later introduction needs explicit units/currency identifiers and review.
- Each factual summary has an inspectable source reference and an indication of
  which claim it supports. Record title, URL, publisher/author when known, access
  date, publication information when known, and reuse terms or explicit unknowns.
  Never equate a source link or review label with verified truth. Preserve uncertainty
  and conflicting evidence; do not copy full source content by default.
- Keep personal data and credentials out of fixtures, logs, public output, and
  attribution. Use synthetic contributors. Document how corrections and potential
  privacy removal interact with history; do not promise irreversible public history.
- Define portable, versioned UTF-8 export records; retain IDs, sources, language,
  and revisions across a round trip. Tests use local fixtures, with no live crawling
  or source fetch required. Rendering must treat contributed content as untrusted.

## C0 — Record the smallest runtime and data contract

**Depends on:** review of this backlog. **Deliverable:** one proposed
[ADR](../docs/decisions/0000-template.md) with a sample entry/export contract.

- [ ] Compare a minimal local implementation with at least one alternative; explain
      storage, validation, tests, restart behavior, and the command a newcomer runs.
- [ ] Specify required title, description, at least one source, categories (possibly
      empty), stable ID, content language, revision metadata, and initial status.
      Define unknown source metadata and claim-to-source links without false defaults.
- [ ] Define versioning, supported URL schemes, error behavior, and timestamp handling;
      describe how script/markup content stays inert and URLs are not fetched automatically.
- [ ] State the local write boundary, synthetic attribution, and export/import contract;
      identify what must change before any public operation.
- [ ] Link an explicit review outcome before implementation relies on an accepted ADR.
      No framework, hosting provider, global identity layer, or charter is selected here.

## C1 — Prepare a small source and compatibility fixture set

**Depends on:** C0's proposed contract; can be prepared during its review.
**Deliverable:** a bounded fixture inventory and reusable local test data.

- [ ] Include 3–5 synthetic entries spanning accented Latin, Arabic, and CJK text,
      at least two content languages, and an entry with no location.
- [ ] Separate synthetic examples from any factual starter content. For factual
      material, record primary sources where available, supported claims, provenance,
      reuse terms, missing metadata, and disagreements. Review permission before copying.
- [ ] Include invalid cases: missing title, missing source, unsafe URL scheme,
      ambiguous revision timestamp, and unsupported export version.
- [ ] Include no personal addresses, real contributor identities, or secrets. Explain
      what the fixtures demonstrate and their limits; make tests work offline.

## C2 — Persist and retrieve one sourced entry (next real code milestone)

**Depends on:** C0's recorded decision and C1. **Deliverable:** a runnable local
create/read slice with persistence, validation, and automated tests.

- [ ] Given a valid fixture, creating an entry returns a stable ID; reading by ID
      after stopping and restarting returns the same fields and first revision.
- [ ] Missing required title/description/source or invalid contract fields produce
      understandable errors and leave no partial record. Unknown IDs return a clear
      not-found result. Source metadata that is genuinely unknown stays unknown.
- [ ] Unicode text round-trips exactly; entries can exist without region/address
      fields. Titles are not identifiers and need not be globally unique.
- [ ] Unsafe source schemes are rejected; content is handled as data. Creating or
      reading an entry does not silently contact source websites or run their content.
- [ ] Demonstrate the documented local write boundary and a disallowed write attempt.
      Include test commands, a restart demonstration, and clean-checkout run instructions.

**Done means:** another contributor can create, restart, retrieve, inspect a source,
and reproduce validation failures. Search, a web UI, and public accounts can wait.

## C3 — Revise entries and preserve inspectable history

**Depends on:** C2. **Deliverable:** a revision operation and history read operation.

- [ ] A correction records a reason, timestamp, synthetic actor, and prior revision;
      retrieving history shows both versions and what changed, including sources.
- [ ] IDs remain stable after title changes. Invalid corrections do not alter the
      current entry or history. A stale base revision reports conflict rather than
      silently overwriting another correction.
- [ ] Document prototype limits for removal/redaction; keep sensitive data out of
      all versions and exports. Public retention policy remains unresolved.

## C4 — Read and search the small collection

**Depends on:** C3. **Deliverable:** a minimal reader UI with search and history.

- [ ] Search titles/descriptions and filter categories; an updated entry is findable.
      Empty query, no matches, duplicate titles, and errors have explicit behavior.
- [ ] Fixture queries find matching accented Latin, Arabic, and CJK text. Document
      actual matching/normalization behavior and unsupported language features;
      do not require transliteration or machine translation in this slice.
- [ ] Detail and history views distinguish summary, evidence, unknown metadata,
      uncertainty, and review status. Unsafe markup stays inert and source links
      are safe to follow; no embedded third-party tracking is needed to read an entry.
- [ ] A tester completes search → entry → source → history using a keyboard and
      checks screen-reader names and focus. Verify right-to-left text and long titles
      in a narrow viewport. Keep interface strings separable for later translation.

## C5 — Demonstrate correction intake and portable recovery

**Depends on:** C3 and C4. **Deliverable:** a complete local prototype walkthrough.

- [ ] From an entry, a reader can find documented instructions for proposing a
      correction with the entry ID, proposed change, reason, and evidence. A manual
      issue-based path is sufficient; warn against private data and do not auto-publish.
- [ ] Export to a versioned format, import into an empty local store, and compare
      IDs, Unicode content, sources, timestamps, and all revisions. Unsupported versions
      and malformed imports fail clearly without partially replacing stored data.
- [ ] Reproduce create → revise → search → inspect sources/history → correction →
      export/restore from a clean checkout. Record automated and manual results.
- [ ] List unresolved pilot requirements from the [roadmap](../docs/ROADMAP.md):
      permissions, content review, private reporting, licensing/reuse, privacy and
      removal, backups, and operational ownership. A successful local demo is not
      authorization for public deployment.
