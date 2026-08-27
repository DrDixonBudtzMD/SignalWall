# Contributing to SignalWall

SignalWall welcomes focused contributions that improve reliability, accessibility, source adapters, transcript workflows, layout behavior, documentation, and local-first usability.

## Before opening a pull request

- Keep platform integrations within the source platform's normal public/embed mechanisms.
- Do not add DRM bypasses, credential theft, paywall circumvention, or scraping that violates access controls.
- Keep secrets, cookies, tokens, and personal browsing data out of the repository.
- Test the project from a clean local checkout.
- Describe which source types and browsers you tested.

## Development

Run the repository through a local web server rather than opening `index.html` directly:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080`.

Groundstate Technology LLC maintains the official SignalWall project identity. Forks remain welcome under the repository license but should not imply they are official Groundstate releases.
