# Macksie roadmap

**First organizational milestone: establish the Foundry. First product: build the Commons.**

This is a proposed sequence for review, not a release schedule. The foundation change is documentation only; all implementation milestones below are future work. The immediate product goal is a working, inspectable [Commons prototype](../commons/README.md).

## 1. Establish the documentation foundation

Introduce the project, document the eight Foundry Glances, provide a contribution path, and create an explicitly unfinished Accords draft.

**Review checkpoint:** the six foundation documents are coherent, their links work, their terminology is consistent, and the Ten Foundations remain unwritten. Review and merge this documentation separately from any application work.

## 2. Agree on the smallest Commons experience

Define an entry with a title, description, sources, categories, and revision history. Select a small, clearly bounded collection of public material and describe the reading, contribution, correction, and review flows.

Before implementation, review the entry fields, source and reuse requirements, accessibility needs, edit permissions, and handling of disputed claims. Compare technical options and identify the minimum shared Core capabilities needed; do not require a complete platform or all eight Glance applications first.

**Review checkpoint:** a contributor can use the brief and proposed screens to explain the entry lifecycle and the acceptance scenarios below. Record a scoped implementation decision in a separate issue or pull request.

## 3. Build one complete entry workflow

In a later implementation change, make it possible for a permitted contributor to create an entry, add sources and categories, revise it, and inspect its history. Give a reader a clear detail page that distinguishes the entry's summary from the evidence it cites.

**Acceptance scenarios:**

- Create a sourced entry and retrieve it after restarting the prototype.
- Revise its description or source list and inspect both revisions, including what changed and why.
- Follow source links and see provenance and review status without treating an unchecked claim as verified.
- Reject incomplete required fields and disallowed edits with understandable feedback.

## 4. Make the collection searchable

Add text search across titles and descriptions, plus category filtering. Use a small reviewed collection to evaluate results, including empty queries, no matches, and entries with similar titles.

**Working prototype milestone:** a new tester can find an entry, read its description, follow its sources, inspect its revision history, and report a correction. A permitted contributor can update it and find the update through search. Document how to run the prototype and repeat these checks.

Include keyboard-only and screen-reader checks of that journey. Describe limitations honestly; this milestone does not claim production readiness or internet-scale coverage.

## 5. Review the prototype before widening access

Collect feedback from developers, designers, researchers, and volunteers. Review source quality, accessibility, disputed-content handling, contributor permissions, privacy, and operational needs.

**Release checkpoint:** document known limitations, ownership of review and corrections, a confidential reporting route, the selected license and data-reuse policy, and demonstrated backup/export and restore behavior before a wider public pilot. Record the pilot decision explicitly rather than treating the prototype as an automatic launch.

## 6. Expand from demonstrated needs

After the basic workflow works, consider links between related entries, richer source provenance, import/export improvements, and a wider public internet index. Expand the Forge and extract reusable shared Core capabilities where real usage supports doing so.

Defer broad crawling, automated mass ingestion, elaborate ranking, a full suite of Foundry applications, and platform-wide infrastructure until separate proposals justify them. No programming language, framework, database, hosting provider, budget, or delivery date is chosen by this roadmap.

## Keep progress visible

Use issues for scoped tasks and pull requests for reviewable changes. The [Foundry](../foundry/README.md) provides perspectives on planning, architecture, safety, participation, resources, and progress. Each milestone should carry evidence of what works and a list of what remains open.
