# Macksie

**Building a free and open internet, together.**

Welcome to Macksie: a project for people who want to help build an internet that serves its communities. Developers, designers, researchers, writers, organizers, and curious newcomers all have a place here.

This repository begins with documentation and project organization. It does not yet contain a working application. Our first product priority is a **Commons prototype**: a searchable public knowledge database where people can follow information back to its sources.

## How the pieces fit together

These introductions describe the intended direction. Detailed responsibilities and interfaces remain proposals for review.

| Part | Purpose | Starting point |
| --- | --- | --- |
| **Foundry** | Coordinate the people, decisions, research, and resources that help Macksie grow. Its eight Glances give contributors different views of that work. | [Foundry and its eight Glances](foundry/README.md) |
| **Forge** | The place for builders to develop, share, and connect applications and tools within the Macksie ecosystem. | Define its relationship to the Core as concrete product needs emerge; no Forge implementation is included here. |
| **Commons** | A searchable, sourced public knowledge database that people can explore, improve, and connect. | [Commons prototype brief](commons/README.md) |
| **Shared Core** | The common technical foundation that Macksie applications can use, with consistent contracts for capabilities such as identity, permissions, and shared data access. | Identify only the capabilities the Commons actually needs before choosing implementations or expanding the platform. |

The Foundry coordinates the work. The Forge supports builders and their applications. The Commons is the first product focus. The shared Core supports reuse across that ecosystem without requiring every part to be built before the Commons can be useful.

## Start here

- Read the [roadmap](docs/ROADMAP.md) for the path to a working Commons prototype and its review checkpoints.
- Visit the [contribution guide](CONTRIBUTING.md) to find useful work, including ways to help without writing code.
- Review the [draft Accords](docs/ACCORDS.md). **The Ten Foundations are not supplied or finalized in this repository.**
- Explore the [Foundry Glances](foundry/README.md): Time, Architects, Roundtable, Sentinel, Benevolence, Treasure, Talent, and Looking Glass.

## Repository map

```text
README.md            Project introduction
CONTRIBUTING.md      Ways to help and the review workflow
docs/
  ACCORDS.md         Draft framework; Ten Foundations pending
  ROADMAP.md         Commons-first milestones
commons/
  README.md         Proposed knowledge model and prototype scope
foundry/
  README.md         Eight Glances and proposed responsibilities
```

## Current boundaries

This foundation contains documentation only. Technology choices, hosting, implementation, and release dates remain open. Future application work should arrive in separate, reviewable changes after the prototype scope is agreed.

Macksie is being organized as an open-source project. No license has been selected or added to this repository yet; license selection is an explicit follow-up decision, not something this documentation settles.

Bring a question, a source, a design, or a small improvement. Start with an [issue](https://github.com/MacksieOS/macksie/issues) or a focused pull request, and help make the next step understandable to the next person.
