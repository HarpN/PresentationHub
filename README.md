# PresentationHub

PresentationHub stores architecture logs and publishing assets used to document system changes across the agent stack.

It is documentation-only. It does not ship with the TheArchives runtime stack.

## Purpose

- Keep architecture logs in a structured, publishable format.
- Capture delivery narratives in consolidated phases rather than fragmented patch history.
- Support lightweight automation for architecture-log indexing.

## Runtime Reference

- The application runtime lives in `TheArchives`.
- TheArchives integrates component repositories as Git submodules.
- PresentationHub should mirror the current clone, setup, launch, and shutdown guidance used by TheArchives.

## Setup Guidance Surface

When setup flow changes, update the instructions in these places together:

- `index.html`
- `README.md`
- `AGENT_CONTEXT.json`
- TheArchives `README.md`
- TheArchives `AGENT_CONTEXT.json`

## Recent Documentation Improvements

- Rewrote architecture log entries into outcome-driven workstreams to reduce noise from iterative implementation.
- Aligned security and moderation narrative with Milo, Charon, TheKeeper, and dashboard changes.
- Added verification snapshot language so logs reflect validated outcomes and known run prerequisites.

## Changelog

### v0.1.0 - 2026-07-14

Added:

- Repository README for architecture-log scope and operating intent.

Changed:

- Consolidated architecture-log style for the current hardening cycle.
