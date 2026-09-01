# SignalWall

**SignalWall** is a personal-use mass media ingestion wall. Paste links from supported media platforms, spawn each source into its own tile, resize/snap feeds into a clean grid, mute/pause where the platform exposes controls, and keep per-feed notes/transcripts.

Version: `0.2.1-working-prototype`

## Supported source routing

- YouTube videos
- YouTube livestream links
- Twitch channels / livestreams
- Twitch videos
- Twitch clips
- Facebook public video/live links
- X / Twitter post links
- Vimeo videos
- Direct `.m3u8` HLS livestreams
- Generic website URLs as web tiles when the site allows iframe embedding

## Controls

Each tile supports small/medium/large sizing, fullscreen focus, reload, open original source, remove, notes/transcript drawer, and mute/unmute/volume/play/pause where the source exposes a controllable player.

Global controls include batch ingest, mute all, pause all, clear wall, export session JSON, and import session JSON.

## Run locally

The YouTube and Twitch embeds work best when served over `localhost`.

### Windows

Double-click:

```bat
START_SIGNALWALL.bat
```

### Linux / macOS

```bash
./START_SIGNALWALL.sh
```

### Manual

From the project folder:

```bash
python -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

### Validate the checkout

Run the dependency-free doctor before publishing or packaging changes:

```bash
python scripts/doctor.py
node --check app.js
```

## Platform limits

Some platforms block embedded playback using security headers such as `Content-Security-Policy` or `X-Frame-Options`. SignalWall does not bypass those restrictions. When a platform blocks embedding, the tile provides an **Open Original** fallback.

Best-supported right now: YouTube, Twitch, and direct HLS `.m3u8` streams.

Partial support: Facebook public video/live embeds, X/Twitter post embeds, and generic website tiles.

## Transcript / caption notes

Each feed includes a local notes/transcript drawer. Full automatic transcript capture should be added later as a separate local helper service because every platform exposes captions differently.

## Roadmap

- Electron desktop version
- True draggable/resizable grid
- Saved feed library
- Audio solo mode
- Local SQLite session store
- Platform adapter modules split into separate files
- Optional local transcript helper
- Screenshot/timestamp notes
- Feed status badges: live, blocked, external-only, replay

## Contributing and security

See `CONTRIBUTING.md` and `SECURITY.md`. SignalWall does not bypass platform access controls, authentication, DRM, embedding restrictions, or browser security policies.

## License

SignalWall source is licensed under **GPL-3.0-or-later**. See `LICENSE`. Groundstate/SignalWall names, logos, and official-project identity are separate from the source-code license.

## Support

See `SUPPORT.md` for Groundstate Technology Patreon, PayPal, and Kickstarter links. Financial support does not purchase ownership, equity, IP rights, or special licensing rights.

## Standalone-first deployment

This project does not require Groundstate Admin Center or a Groundstate account. Core operation remains local and independently deployable. See [docs/STANDALONE_OPERATION.md](docs/STANDALONE_OPERATION.md) for the product-specific identity and outage boundary.
