# Agent development guide

This is a small static business application. Favor reliability, simple deployment, accessibility, and data safety over framework or dependency expansion.

## Workflow

1. Read `PLAN.md`, `README.md`, `SECURITY.md`, CI, and `scripts/check_site.py` before editing behavior.
2. Verify browser APIs against current official documentation when changing frontend behavior. Context7 may assist with current docs.
3. Keep dependencies at zero unless a concrete requirement justifies one.
4. Preserve responsive layouts, keyboard usability, readable contrast, and fast loading.
5. Validate user-entered data before storing or rendering it, and avoid unsafe HTML injection.
6. Run the existing site checker after changes.
7. Add Playwright only for meaningful interactive flows that static checks cannot cover; do not add browser tooling merely for presence.

## Review roles

For meaningful changes, review separately for implementation, accessibility/UX, tests, and data/privacy impact.

## Completion gate

A change is complete only when relevant CI passes and browser-visible behavior has a concise manual verification path. Do not add tooling that creates more maintenance than the feature it protects.
