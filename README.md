# Mochi Mochi Web

Mochi Mochi is a small, dependency-light web application built with HTML, CSS, and vanilla JavaScript for a food business.

The project provides a product menu, WhatsApp order preparation, and a browser-local sales record without requiring a custom backend or account system.

## Features

- Dynamic menu organized by categories
- Product search
- Product flavors, variants, and ingredients
- Shopping cart with quantities and estimated totals
- Orders prepared and sent through WhatsApp
- Sales dashboard with purchase history
- Quick-sale registration
- Excel and CSV export
- Light and dark mode
- Responsive design for mobile devices

## Technologies Used

- HTML
- CSS
- JavaScript
- `localStorage`
- SheetJS `xlsx@0.18.5`
- GitHub Pages

## How to Run the Project

1. Clone or download this repository.
2. Open `app.js` and update the business information and product catalog when needed.
3. Open `index.html` in your browser.

No package manager, build command, or framework installation is required.

## Sales Storage and Privacy

Sales are stored locally in the browser using `localStorage`. The project does not provide a project-owned cloud database or account system, so the saved history remains on the device/browser profile where it was created unless the user explicitly exports it.

The sales section can export the saved history as Excel or CSV. Orders are handed off to WhatsApp only when the user activates the order action.

See [`SECURITY.md`](SECURITY.md) for the project's data and third-party-resource boundary.

## Automated Checks

GitHub Actions protects the small static architecture without adding a build tool only for CI.

The workflow verifies:

- required page sections remain present;
- JavaScript `data-*` hooks used by the app are not accidentally removed;
- local script/style references point to tracked files;
- the SheetJS browser reference remains version-pinned;
- `app.js` passes Node's JavaScript syntax checker.

Run the same checks locally from the repository root:

```bash
python scripts/check_site.py
node --check app.js
```

The Python checker uses only the standard library.

## GitHub Pages

Because the site files are stored in the repository root, the project can be published from:

`Settings > Pages > Deploy from branch > main > /root`

## Project Decisions

The zero-framework architecture is intentional. For the current scope, vanilla HTML/CSS/JavaScript keeps deployment simple, preserves offline-friendly editing, and avoids adding runtime dependencies that do not solve a real problem.

A future backend or framework migration should be driven by a concrete requirement such as multi-device inventory, authenticated accounts, centralized sales data, or server-side order processing—not by framework adoption alone.

## What I Learned

This project practices responsive interface design, dynamic JavaScript content, browser storage, order workflows, sales tracking, export formats, static-site validation, and maintaining a small application with explicit privacy boundaries.
