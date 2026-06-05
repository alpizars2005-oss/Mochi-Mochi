# Mochi Mochi Web

Mochi Mochi is a web application built with HTML, CSS, and vanilla JavaScript for a small food business.

I created this project to provide a simple way to display products, receive orders through WhatsApp, and keep a basic sales record without requiring a complex system or backend.

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
- LocalStorage
- SheetJS
- GitHub Pages

## How to Run the Project

1. Clone or download this repository.
2. Open `app.js` and update the business information and product catalog.
3. Open `index.html` in your browser.

## Sales Storage and Export

Sales are stored locally in the browser using `localStorage`. This means the data remains on the device where the application is used and is not stored in the cloud.

The sales section can export the saved history as an Excel or CSV file.

## GitHub Pages

Because the main files are stored in the repository root, the project can be published from:

`Settings > Pages > Deploy from branch > main > /root`

## Project Decisions

I built this project without frameworks so it would remain easy to understand, edit, and maintain while I continue improving my JavaScript skills.

A future version could migrate to React and include a backend for cloud-based inventory, accounts, and sales management.

## What I Learned

This project helped me practice responsive interface design, dynamic JavaScript content, browser storage, order workflows, sales tracking, and data exports for a real small business.
