# Urei Miura — personal research website

English-first, bilingual research website for 三浦憂 / Urei Miura.

Intended URL: https://miura-urei.github.io/

## Preview

No package installation is needed. Open `index.html` directly, or run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Then visit http://127.0.0.1:8765/ (Japanese: `/ja.html`).

## Update content

- Edit the bilingual profile and research copy in `build.py`.
- Edit the bibliography in `data/publications.json`.
- Run `python3 build.py`, then commit the regenerated `index.html`, `ja.html`, `publications.bib`, `robots.txt`, and `sitemap.xml` with the source changes.
- Adjust appearance in `styles.css`; publication filters are in `site.js`.
- Publication pages are complete HTML and remain readable with JavaScript disabled.
- `publications.bib` is a downloadable BibTeX bibliography.

There are no external fonts, analytics, package dependencies, or third-party runtime scripts.

## GitHub Pages

Use the public repository `miura-urei/miura-urei.github.io`. In **Settings → Pages**, choose **Deploy from a branch → main → /(root)**. The included `.nojekyll` file disables Jekyll processing. No custom domain is required.

[GitHub's publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## Sources and editorial decisions

Information checked on **2026-11-13**.

- Affiliation, doctoral status, JSPS status, and professional email: [YITP Japanese directory](https://www.yukawa.kyoto-u.ac.jp/contents/people/people) and [English directory](https://www.yukawa.kyoto-u.ac.jp/en-GB/contents/people/people). The Japanese directory places Miura in condensed matter; the English directory says quantum information. The page therefore gives the institute affiliation and describes research based on the papers, without asserting group membership.
- Each publication includes its primary-source URLs in `data/publications.json`.
- Research summaries are original editorial summaries of the listed papers, not quotations or an approved research statement.
- Preprints are explicitly distinguished from journal articles. A submission to a journal is not counted as a published article.
- The list contains six verified works and is not asserted to be an exhaustive CV.
- The lattice illustration is an original schematic, not a calculated result or figure from a paper.

Profile text, publication status, and contact details should be updated when they change.
