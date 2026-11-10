# Getting started with the Macksie Foundry

The Foundry is ready for small, reviewable contributions to documentation, research,
design, and the proposed Commons backlog. There is no runnable Commons application
yet. Start with the [project introduction](README.md) and [contribution guide](CONTRIBUTING.md).

## Choose a useful first task

1. Read the [Foundry philosophy and names](foundry/PHILOSOPHY.md) and
   [Commons implementation backlog](commons/BACKLOG.md).
2. Check [open issues](https://github.com/MacksieOS/macksie/issues) and
   [open pull requests](https://github.com/MacksieOS/macksie/pulls) for overlapping work.
3. Pick one backlog ID, or propose one small improvement. Use the
   [task template](.github/ISSUE_TEMPLATE/task.md) for implementation, design, or
   research; the [bug template](.github/ISSUE_TEMPLATE/bug_report.md) for a reproducible
   defect; or the [proposal template](.github/ISSUE_TEMPLATE/proposal.md) for a decision.
4. State the intended outcome, dependencies, exclusions, and observable acceptance
   criteria. Comment on an existing issue before duplicating it. An issue is a work
   discussion, not a promise of assignment, compensation, or governing authority.

No coding setup is needed to review wording, trace a source, sketch an accessible
entry page, or review international examples. A first research contribution could
prepare the public-source fixture inventory in C1; a designer could sketch the C4
reader journey. Label proposed work and evidence clearly.

## Get a local copy

For local documentation checks, install Git and Python 3.10 or newer. No additional
Python packages, accounts, credentials, database, or hosting are needed to run checks.
These are documentation tools, not a choice of application stack.

```sh
git clone https://github.com/MacksieOS/macksie.git
cd macksie
git switch -c your-topic
```

Use a fork's clone URL if you will push without repository write access. Create your
topic branch from the relevant base before editing; never push changes to someone
else's active branch.

### While the documentation PRs are under review

[PR #1](https://github.com/MacksieOS/macksie/pull/1) supplies the six introductory
documents on `docs/macksie-foundation`. This contributor milestone starts at its
commit `fac2e784468c91b566ad34b4b9ee1e3d05a16f52` on
`docs/foundry-contributor-milestone` and adds files without editing those six.
Its PR targets `docs/macksie-foundation` so the review shows only this milestone.

To inspect or build on this milestone before it reaches `main`, fetch the upstream
repository and create your own branch from its milestone branch:

```sh
git fetch https://github.com/MacksieOS/macksie.git docs/foundry-contributor-milestone
git switch -c your-foundry-topic FETCH_HEAD
```

Do not merge a stacked PR into its dependency branch as a shortcut. After PR #1 is
merged, refresh this milestone against `main`, retarget its PR to `main`, and verify
that its diff still contains only these additions. A squash or rebase merge may
require replaying only the milestone commit(s) onto the new `main`. Recheck the
current PR state before doing this. This milestone does not merge either PR.

GitHub's issue chooser uses templates from the default branch. Until these changes
reach it, copy the templates from this branch into a new issue manually. See
[GitHub's template documentation](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates).

## Check and submit

From the repository root:

```sh
python3 scripts/check_docs.py
git diff --check
```

The offline checker checks local inline Markdown link targets, heading fragments,
fenced blocks, and the small issue-template metadata format used here. It does not
check external website availability, source accuracy, full Markdown rendering, or
application behavior. Also preview edited Markdown and review the task's acceptance
criteria. On Windows, `py -3` can replace `python3`.

Open a focused PR with the [PR template](.github/pull_request_template.md), the issue
or backlog ID, checks actually run, and remaining questions. Normally target `main`;
for a dependent change, target the dependency branch and explain the eventual
retargeting step as above. Keep the PR open for review. Review feedback and a merge
are repository actions, not ratification of the Accords.

For an architectural choice, copy [the ADR template](docs/decisions/0000-template.md)
to the next available `NNNN-short-title.md` in that directory, leave its status
Proposed, and link the issue and PR. Use it for data contracts, storage, permissions,
or other consequential tradeoffs, not spelling fixes. Record acceptance only with
an explicit linked review decision; preserve superseded records with a successor
link. No architecture decision is accepted by this template alone.

## Protect people and sources

Use synthetic data or public material with documented provenance and reuse terms.
Never put credentials, private addresses, personal contact details, or confidential
reports in public issues, fixtures, logs, or screenshots. A private reporting route
is still unresolved; do not invent a contact or publish sensitive details while it
is being established. Describe a non-sensitive need for that route if necessary.

The [backlog](commons/BACKLOG.md) makes worldwide interoperability, privacy, and
source inspection part of each code slice. License selection, public operation,
governance, and compensation remain separate decisions.
