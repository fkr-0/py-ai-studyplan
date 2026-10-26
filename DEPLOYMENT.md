# Publishing at study.fkr.dev using GitHub Actions

This project deploys to **GitHub Pages via a dedicated GitHub Actions workflow**:
[.github/workflows/pages.yml](.github/workflows/pages.yml).

## Architecture

```text
git push main / workflow_dispatch
                |
                v
      checkout + Python + Pandoc
                |
          make check
    (build slides + course ZIP,
     run tests, validate links)
                |
   python scripts/stage_pages.py
                |
        _site/ (allowlisted)
                |
  actions/upload-pages-artifact@v4
                |
   actions/deploy-pages@v4
                |
       https://study.fkr.dev/
```

The workflow follows the [official GitHub Pages custom-workflow pattern](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages). The build job uses `actions/checkout@v6`, `actions/setup-python@v6`, `actions/configure-pages@v5` and `actions/upload-pages-artifact@v4`. The deploy job uses `actions/deploy-pages@v4` with `pages: write`, `id-token: write`, environment `github-pages` and a dependency on the build job.

## Published artifact, not the repository checkout

The source checkout is **not** uploaded wholesale. `scripts/stage_pages.py` stages only:

- `index.html`: redirects to the first presentation slide.
- `studyplan.html`: welcome page with course overview, slide entry and ZIP download; linked from the bottom of slide 1.
- `CNAME`: `study.fkr.dev`.
- `.nojekyll`.
- `docs/*.md`: readable course chapters.
- `build-revealjs/index.html` and styles.
- `build-revealjs/py-ai-studyplan-materials.zip`: full course, with link on the first two slides.

The ZIP itself is rebuilt by `scripts/build_slides.py`, with an explicit allowlist that excludes common secrets, virtual environments and cache files. The uploaded site artifact does not contain Git metadata or the full source tree. Third-party videos/PDFs are loaded from their publishers or opened via source links; they are not redistributed.

## Update/publish

```sh
make check
python3 scripts/stage_pages.py
git add <the files intentionally changed>
git commit -m "Update Python and AI curriculum"
git push origin main
gh run list --workflow pages.yml
```

You can also manually start the workflow from the Actions tab (or with `gh workflow run pages.yml`). Keep the auto-build and deployment in the same workflow so `deploy-pages` uses the artifact from its own build job.

### DNS and custom domain

GitHub Pages is configured with custom domain `study.fkr.dev`. GoDaddy record:

```text
CNAME  study  fkr-0.github.io.  TTL 600
```

Changing Pages' publishing source to **GitHub Actions** must not change the custom domain or this DNS record. GitHub may need time to issue or renew the HTTPS certificate. Do not disable validation or work around it by exposing the site insecurely.

## Verification

```sh
make check
python3 scripts/stage_pages.py
gh run list --workflow pages.yml --limit 5
gh api repos/fkr-0/py-ai-studyplan/pages \
  --jq '{build_type,cname,https_enforced,status}'
dig +short CNAME study.fkr.dev
curl -IL https://study.fkr.dev/build-revealjs/
curl -IL https://study.fkr.dev/build-revealjs/py-ai-studyplan-materials.zip
```

A successful deployment includes green jobs for both build and deploy, and HTTP 200 for the public slide deck and ZIP. For Pages configuration, use `gh api -X PUT repos/fkr-0/py-ai-studyplan/pages -f build_type=workflow` once, then verify via the API.
