#!/usr/bin/env python3
"""Regenerate the two static language editions. Python standard library only."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'data/publications.json').read_text())
PAPERS = DATA['publications']
BASE = 'https://miura-urei.github.io'
ARXIV = 'https://arxiv.org/search/?query=Miura%2C+Urei&searchtype=author&abstracts=show&order=-announced_date_first&size=50'
EMAIL = 'urei.miura@yukawa.kyoto-u.ac.jp'

COPY = {
    'en': {
        'title': 'Urei Miura | Theoretical Physics',
        'description': 'Urei Miura, doctoral student at the Yukawa Institute for Theoretical Physics, Kyoto University. Research on supersymmetry, nonequilibrium dynamics, geometry, and integrability.',
        'name': 'Urei Miura', 'other_name': '三浦 憂',
        'skip': 'Skip to main content', 'nav': 'Main navigation',
        'research': 'Research', 'publications': 'Publications', 'contact': 'Contact',
        'field': 'Theoretical physics · Kyoto, Japan',
        'lead': 'Symmetry, geometry,<br>and many-body dynamics.',
        'intro': 'I am a doctoral student at the Yukawa Institute for Theoretical Physics, Kyoto University. I study how symmetry and constraints shape quantum and stochastic many-body systems, and their connections to geometry and integrability.',
        'view': 'Explore my research', 'email': 'Get in touch',
        'role': 'Doctoral student · JSPS Research Fellow',
        'institute': 'Yukawa Institute for<br>Theoretical Physics', 'university': 'Kyoto University',
        'location': 'Kyoto, Japan',
        'latest': 'Latest preprint', 'latest_date': '10 November 2026',
        'research_note': 'Questions at the intersection of condensed matter, statistical physics, and mathematical physics.',
        'research_intro': 'How do microscopic structures give rise to collective behavior?',
        'topics': [
            ('Supersymmetry & quantum matter', 'I study supersymmetry in interacting lattice models, including its spontaneous breaking, emergent spacetime symmetry, and the structure of quantum phases.', 'Kitaev chains · Nicolai models · Quantum criticality'),
            ('Nonequilibrium dynamics', 'I investigate how constraints and fragmentation shape steady states, relaxation, and metastability in stochastic many-body systems.', 'Exclusion processes · Exact steady states · Relaxation'),
            ('Geometry, topology & integrability', 'My recent work explores connections between integrable dynamics, Krylov geometry, counterdiabatic transport, and topological flat bands.', 'Toda–Arnoldi correspondence · Nonlinear dynamics · Topology'),
        ],
        'pub_note': 'Journal articles and preprints, with links to the published and open-access versions.',
        'all': 'All works', 'journals': 'Journal articles', 'preprints': 'Preprints',
        'filter_label': 'Filter publications', 'count': '6 works shown', 'preprint': 'Preprint',
        'journal_link': 'Journal', 'bib': 'Download bibliography',
        'contact_note': 'For research correspondence and scientific discussions.',
        'contact_copy': 'Let’s talk about physics.',
        'affiliation': 'Yukawa Institute for Theoretical Physics<br>Kyoto University · Kyoto, Japan',
        'directory': 'YITP directory',
        'footer': 'Urei Miura · 三浦 憂', 'updated': 'Updated 13 November 2026', 'top': 'Back to top',
        'art_label': 'Schematic of a one-dimensional lattice with alternating bonds',
        'art_caption': 'LATTICE · SYMMETRY · DYNAMICS',
    },
    'ja': {
        'title': '三浦 憂 | Urei Miura — 理論物理学',
        'description': '三浦憂（Urei Miura）の研究者個人サイト。京都大学基礎物理学研究所。超対称性、非平衡ダイナミクス、幾何学・可積分系の研究と論文を紹介します。',
        'name': '三浦 憂', 'other_name': 'Urei Miura',
        'skip': '本文へ移動', 'nav': 'メインナビゲーション',
        'research': '研究', 'publications': '論文', 'contact': '連絡先',
        'field': '理論物理学 · 京都',
        'lead': '対称性・幾何学と<br>多体系のダイナミクス。',
        'intro': '京都大学基礎物理学研究所の博士課程学生です。量子多体系や確率的な多体系において、対称性や制約が生み出す物理と、幾何学・可積分性とのつながりを研究しています。',
        'view': '研究について', 'email': 'お問い合わせ',
        'role': '博士課程学生 · 日本学術振興会特別研究員',
        'institute': '京都大学<br>基礎物理学研究所', 'university': '',
        'location': '京都、日本',
        'latest': '最新のプレプリント', 'latest_date': '2026年11月10日',
        'research_note': '物性理論・統計物理学・数理物理学の接点を探っています。',
        'research_intro': 'ミクロな構造から、どのように集団的な振る舞いが生まれるのか。',
        'topics': [
            ('超対称性と量子多体系', '相互作用する格子模型における超対称性を研究しています。自発的対称性の破れや時空超対称性の創発、量子相の構造に関心があります。', 'Kitaev鎖 · Nicolai模型 · 量子臨界現象'),
            ('非平衡ダイナミクス', '確率的な多体系において、制約や状態空間の断片化が定常状態・緩和・準安定性に及ぼす影響を調べています。', '排他過程 · 厳密な定常状態 · 緩和現象'),
            ('幾何学・トポロジー・可積分性', '最近は、可積分ダイナミクス、Krylov幾何学、反断熱輸送、トポロジカルな平坦バンドの間の関係を研究しています。', 'Toda–Arnoldi対応 · 非線形ダイナミクス · トポロジー'),
        ],
        'pub_note': '査読付き論文とプレプリント。出版社版とarXivへのリンクを掲載しています。',
        'all': 'すべて', 'journals': '査読付き論文', 'preprints': 'プレプリント',
        'filter_label': '論文の種類で絞り込み', 'count': '6 件を表示', 'preprint': 'プレプリント',
        'journal_link': '出版社', 'bib': '文献情報をダウンロード',
        'contact_note': '研究に関するご連絡はこちらへ。',
        'contact_copy': '研究について、お気軽にご連絡ください。',
        'affiliation': '京都大学 基礎物理学研究所<br>京都、日本',
        'directory': '基研の構成員一覧',
        'footer': '三浦 憂 · Urei Miura', 'updated': '最終更新：2026年11月13日', 'top': 'ページ上部へ',
        'art_label': '結合が交互に並ぶ一次元格子の模式図',
        'art_caption': 'LATTICE · SYMMETRY · DYNAMICS',
    }
}


def lattice(c):
    # A schematic, not a plot of a particular model or calculated result.
    return f'''<svg class="lattice" viewBox="0 0 340 240" role="img" aria-label="{c['art_label']}" xmlns="http://www.w3.org/2000/svg">
      <defs><pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".8" fill="#d0d9cd"/></pattern></defs>
      <rect x="1" y="1" width="338" height="214" fill="url(#dots)"/>
      <g fill="none" stroke="#b2c0ae" stroke-width="1.2">
        <path d="M34 115C62 32 115 32 142 115S223 198 250 115"/>
        <path d="M88 115C115 198 169 198 196 115S277 32 304 115"/>
      </g>
      <path d="M34 115H304" fill="none" stroke="#8d9e8d" stroke-width="1.5"/>
      <g stroke="#285b49" stroke-width="5"><path d="M88 115h54m54 0h54"/></g>
      <g stroke="#285b49" stroke-width="1.5" fill="#faf9f5"><circle cx="34" cy="115" r="9"/><circle cx="88" cy="115" r="7"/><circle cx="142" cy="115" r="7"/><circle cx="196" cy="115" r="7"/><circle cx="250" cy="115" r="7"/><circle cx="304" cy="115" r="9"/></g>
      <g fill="#285b49"><circle cx="34" cy="115" r="3"/><circle cx="304" cy="115" r="3"/></g>
      <text x="170" y="237" fill="#66706a" text-anchor="middle" font-family="sans-serif" font-size="8" letter-spacing="2">{c['art_caption']}</text>
    </svg>'''


def paper_html(p, c):
    title = escape(p['title'])
    authors = ', '.join('<strong>Urei Miura</strong>' if a == 'Urei Miura' else escape(a) for a in p['authors'])
    main_url = 'https://doi.org/' + p['doi'] if p['doi'] else p['arxiv']
    venue = escape(p['journal']) if p['journal'] else f"{c['preprint']} · arXiv:{p['id']} ({p['year']})"
    journal_link = f'<a href="https://doi.org/{p["doi"]}" aria-label="{c["journal_link"]}: {title}">{c["journal_link"]} ↗</a>' if p['doi'] else ''
    return f'''<li class="publication" data-kind="{p['kind']}">
      <span class="publication-year">{p['year']}</span>
      <article><h3 lang="en"><a href="{main_url}">{title}</a></h3>
      <p class="authors" lang="en">{authors}</p><p class="venue">{venue}</p>
      <div class="pub-links">{journal_link}<a href="{p['arxiv']}" aria-label="arXiv: {title}">arXiv ↗</a>
      <a href="https://arxiv.org/pdf/{p['id']}" aria-label="PDF: {title}">PDF ↗</a></div></article>
    </li>'''


def render(lang):
    c = COPY[lang]
    page = 'index.html' if lang == 'en' else 'ja.html'
    canonical = BASE + ('/' if lang == 'en' else '/ja.html')
    topics = '\n'.join(f'<article class="research-topic"><h3>{escape(t)}</h3><p>{escape(d)}</p><span class="topic-keywords">{escape(k)}</span></article>' for t, d, k in c['topics'])
    papers = '\n'.join(paper_html(p, c) for p in PAPERS)
    languages = f'''<div class="language" aria-label="Language / 言語"><a href="index.html" lang="en" hreflang="en" {'aria-current="page"' if lang == 'en' else 'data-language-link'}>EN</a><a href="ja.html" lang="ja" hreflang="ja" {'aria-current="page"' if lang == 'ja' else 'data-language-link'}>日本語</a></div>'''
    schema = {
        '@context': 'https://schema.org', '@type': 'ProfilePage', 'dateModified': DATA['verified'],
        'mainEntity': {'@type': 'Person', 'name': 'Urei Miura', 'alternateName': '三浦憂',
        'url': BASE + '/', 'jobTitle': 'Doctoral student', 'email': EMAIL,
        'affiliation': {'@type': 'Organization', 'name': 'Yukawa Institute for Theoretical Physics, Kyoto University', 'url': 'https://www.yukawa.kyoto-u.ac.jp/'},
        'sameAs': ['https://github.com/miura-urei']}
    }
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{c['title']}</title><meta name="description" content="{c['description']}">
  <meta name="theme-color" content="#faf9f5">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{BASE}/"><link rel="alternate" hreflang="ja" href="{BASE}/ja.html"><link rel="alternate" hreflang="x-default" href="{BASE}/">
  <meta property="og:type" content="website"><meta property="og:title" content="{c['title']}"><meta property="og:description" content="{c['description']}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'en_US' if lang == 'en' else 'ja_JP'}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="styles.css"><script src="site.js" defer></script>
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body id="top">
<a class="skip-link" href="#main">{c['skip']}</a>
<header class="site-header"><div class="wrap header-inner">
  <a class="wordmark" href="{page}" aria-label="Urei Miura — home">Urei Miura<span aria-hidden="true">.</span></a>
  <nav class="navigation" aria-label="{c['nav']}"><a href="#research">{c['research']}</a><a href="#publications">{c['publications']}</a><a href="#contact">{c['contact']}</a>{languages}</nav>
</div></header>
<main class="wrap" id="main">
  <section class="hero" aria-labelledby="name"><div>
    <div class="eyebrow">{c['field']}</div><h1 id="name">{c['name']}</h1>
    <p class="name-secondary" lang="{'ja' if lang == 'en' else 'en'}">{c['other_name']}</p>
    <p class="lead">{c['lead']}</p><p class="intro">{c['intro']}</p>
    <div class="hero-links"><a class="primary-link" href="#research">{c['view']} <span aria-hidden="true">↓</span></a><a class="text-link" href="#contact">{c['email']} <span aria-hidden="true">↗</span></a></div>
  </div><aside class="identity-panel">{lattice(c)}<div class="affiliation">
    <p class="role">{c['role']}</p><p class="institute">{c['institute']}<br>{c['university']}</p><p class="location">{c['location']}</p>
  </div></aside></section>
  <a class="latest" href="https://arxiv.org/abs/2611.13591"><div><span class="latest-label">{c['latest']}</span><time class="latest-date" datetime="2026-11-10">{c['latest_date']}</time></div><span class="latest-title" lang="en">Topological flat bands from nonlinear periodic motion</span><span aria-hidden="true">↗</span></a>
  <section class="section" id="research" aria-labelledby="research-heading">
    <div class="section-heading"><span class="section-number" aria-hidden="true">01</span><h2 id="research-heading">{c['research']}</h2><p>{c['research_note']}</p></div>
    <div><p class="research-intro">{c['research_intro']}</p>{topics}</div>
  </section>
  <section class="section" id="publications" aria-labelledby="publications-heading">
    <div class="section-heading"><span class="section-number" aria-hidden="true">02</span><h2 id="publications-heading">{c['publications']}</h2><p>{c['pub_note']}</p><p style="margin-top:20px"><a href="publications.bib" download>{c['bib']} ↓</a></p></div>
    <div><div class="publication-toolbar"><div class="publication-filters" role="group" aria-label="{c['filter_label']}" hidden><button type="button" data-filter="all" aria-pressed="true">{c['all']}</button><button type="button" data-filter="journal" aria-pressed="false">{c['journals']}</button><button type="button" data-filter="preprint" aria-pressed="false">{c['preprints']}</button></div><span class="publication-count" id="publication-count" role="status" aria-live="polite">{c['count']}</span></div>
    <ol class="publication-list">{papers}</ol></div>
  </section>
  <section class="section contact-section" id="contact" aria-labelledby="contact-heading">
    <div class="section-heading"><span class="section-number" aria-hidden="true">03</span><h2 id="contact-heading">{c['contact']}</h2><p>{c['contact_note']}</p></div>
    <div><p class="contact-copy">{c['contact_copy']}</p><a class="email" href="mailto:{EMAIL}">{EMAIL}</a><p class="contact-affiliation">{c['affiliation']}</p>
    <div class="external-links"><a href="https://www.yukawa.kyoto-u.ac.jp/{'en-GB/' if lang == 'en' else ''}contents/people/people">{c['directory']} ↗</a><a href="{escape(ARXIV, quote=True)}">arXiv ↗</a><a href="https://github.com/miura-urei">GitHub ↗</a></div></div>
  </section>
</main>
<footer class="site-footer"><div class="wrap footer-inner"><span>© 2026 {c['footer']}</span><span>{c['updated']}</span><a href="#top">{c['top']} ↑</a></div></footer>
</body>
</html>
'''


def bibliography():
    records = []
    for p in PAPERS:
        title = p['title'].replace('–', '--')
        fields = {'title': '{' + title + '}', 'author': ' and '.join(p['authors']), 'year': str(p['year']), 'eprint': p['id'], 'archivePrefix': 'arXiv', 'url': p['arxiv']}
        if p['doi']:
            fields['doi'] = p['doi']
            # Structured APS metadata, not a whole citation in the journal field.
            journal, rest = p['journal'].rsplit(' ', 3)[0], p['journal'].rsplit(' ', 3)
            fields.update(journal=journal, volume=rest[1].rstrip(','), pages=rest[2])
        records.append('@' + ('article' if p['doi'] else 'misc') + '{Miura' + p['id'].replace('.', '') + ',\n' + ',\n'.join(f'  {key} = {{{value}}}' for key, value in fields.items()) + '\n}')
    return '\n\n'.join(records) + '\n'


if __name__ == '__main__':
    for language, filename in [('en', 'index.html'), ('ja', 'ja.html')]:
        (ROOT / filename).write_text(render(language), encoding='utf-8')
    (ROOT / 'publications.bib').write_text(bibliography(), encoding='utf-8')
    (ROOT / 'sitemap.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc><lastmod>{DATA['verified']}</lastmod></url><url><loc>{BASE}/ja.html</loc><lastmod>{DATA['verified']}</lastmod></url></urlset>
''')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
    print(f'Generated English and Japanese pages, BibTeX, and sitemap ({len(PAPERS)} works).')
