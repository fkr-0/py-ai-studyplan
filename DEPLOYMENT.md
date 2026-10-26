# Publishing the course at study.fkr.dev

This site uses **GitHub Pages, deploy from the `main` branch's root directory**. No Actions or Node build is required on GitHub. The committed generated HTML is served as static files.

## Layout and links

- `index.html`: simple public entry point that redirects to `build-revealjs/`. It also has visible fallback links.
- `build-revealjs/index.html`: full Reveal.js slide deck.
- `build-revealjs/py-ai-studyplan-materials.zip`: complete course ZIP with a link on the first two slides.
- `docs/*.md`: Markdown study materials usable directly in a text editor.
- `CNAME`: contains exactly `study.fkr.dev`.
- `.nojekyll`: instructs Pages to serve the files as-is.

The ZIP is rebuilt deterministically from an explicit allowlist by `scripts/build_slides.py`. In particular, it excludes virtual environments, caches, the ZIP itself, and common secrets. External media is referenced by the presentation rather than redistributed.

## Updating

```sh
make check   # build deck + ZIP, run tests and link checks
git add -A
git commit -m "Update Python and AI course"
git push origin main
```

GitHub Pages deploys the published branch as soon as GitHub finishes processing the push. Media elements require online access to YouTube/CDNs; the presentation has external fallback links.

## DNS

GitHub Pages repo owner: `fkr-0`. Custom domain: `study.fkr.dev`.

Expected DNS at GoDaddy:

```text
Type    Name    Value
CNAME   study   fkr-0.github.io.
```

Per GitHub guidance, assign the custom domain in Pages **before** adding the DNS record, and target the account Pages host rather than the repository name. DNS propagation and certificate issuance may take time. Never replace wildcard, apex, MX, or other unrelated domain records.

## Verification

```sh
dig +short CNAME study.fkr.dev
curl -I https://study.fkr.dev/
curl -I https://study.fkr.dev/build-revealjs/
curl -I https://study.fkr.dev/build-revealjs/py-ai-studyplan-materials.zip
```

Actual end-to-end verification includes visiting the deck in a browser, checking navigation and media fallbacks, and downloading/inspecting the ZIP. If HTTPS is not yet ready, inspect GitHub Pages certificate state and DNS rather than falling back to serving the site over plaintext HTTP permanently.
