# Commons

**A searchable, sourced public knowledge database for Macksie.**

The Commons is intended to help people find useful knowledge, inspect its sources, and improve it together. A reader should be able to tell what an entry says, where its claims come from, and how it has changed.

**Status:** proposed product brief. This directory contains documentation only; the database, search interface, and contribution workflow are not implemented in this repository.

## The first useful experience

Start with a small collection and one complete journey: search for a topic, open an entry, read its description, follow its sources, and inspect its revision history. A permitted contributor can propose or make a correction through a review process still to be specified.

The first entry needs a **title, description, sources, categories, and revision history**. Related-entry links and a wider internet index follow after that foundation works.

## Proposed entry model

This is a discussion model, not a committed database schema or API.

| Field | Purpose |
| --- | --- |
| Stable identifier | Keep an entry addressable when its title changes. |
| Title | Give the topic a clear, recognizable name. |
| Description | Explain the topic in readable language and connect factual claims to supporting sources. |
| Sources | Record source title, URL, author or publisher when known, relevant publication date, access date, and which claim the source supports. |
| Categories | Support browsing and filtering with a small, understandable vocabulary. |
| Revision history | Preserve earlier versions, timestamps, contributor attribution appropriate to the agreed privacy policy, and reasons for changes. |
| Review status | Distinguish draft, reviewed, and disputed material using a workflow to be agreed. |

Missing source metadata should remain visibly unknown. A source link or a review label must not imply that every claim is true or that consensus exists.

## Search and discovery

For the prototype, propose text search over titles and descriptions with category filters. Results should show enough context to choose an entry, then lead to its sources and history. Provide clear no-results and error states, readable layouts, keyboard navigation, and screen-reader labels.

Do not require automated crawling, personalized recommendations, or a large search infrastructure to demonstrate this journey. Search ranking and richer connections can be evaluated after there is a usable collection.

## Sources and corrections

- Prefer direct, inspectable evidence and primary sources where appropriate; explain when secondary interpretation is used.
- Preserve disagreements and uncertainty rather than forcing disputed claims into a single confident summary.
- Record broken or changed links and support a documented correction path.
- Use material contributors are permitted to share, with attribution and reuse terms recorded where relevant. Public availability is not itself permission to republish an entire source.
- Keep private information and credentials out of the collection. Content review, edit permissions, and abuse reporting need explicit decisions before public contributions open.

The Commons aims to make evidence easier to inspect. Its prototype should not present itself as an authority that guarantees the truth of every entry.

## Relationship to the wider project

The **Foundry** coordinates the work and its review. The **Forge** is the intended builder ecosystem through which tools and applications can connect. The **shared Core** should provide common capabilities where they are needed, with the smallest useful contracts defined alongside the prototype rather than assumed in advance.

## Open design decisions

The storage and search technology, starter collection, review workflow, contributor permissions, category vocabulary, source-content reuse policy, and hosting model remain open. Record the decisions in reviewable changes before treating them as implementation requirements.

See the [roadmap](../docs/ROADMAP.md) for acceptance scenarios and the [contribution guide](../CONTRIBUTING.md) for ways to help.
