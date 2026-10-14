import json
from datetime import date

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','r') as f:
    data = json.load(f)

today = date.today().strftime('%Y-%m-%d')

urls = []

# Pagine principali
urls.append({'loc':'https://cultura-e.it/','lastmod':'2026-10-07','priority':'1.0','changefreq':'monthly'})
urls.append({'loc':'https://cultura-e.it/chi-siamo.html','lastmod':'2026-10-07','priority':'0.8','changefreq':'yearly'})
urls.append({'loc':'https://cultura-e.it/servizi.html','lastmod':'2026-10-07','priority':'0.9','changefreq':'yearly'})
urls.append({'loc':'https://cultura-e.it/portfolio.html','lastmod':today,'priority':'0.9','changefreq':'monthly'})
urls.append({'loc':'https://cultura-e.it/contatti.html','lastmod':'2026-10-08','priority':'0.7','changefreq':'yearly'})
urls.append({'loc':'https://cultura-e.it/privacy.html','lastmod':'2026-10-08','priority':'0.3','changefreq':'yearly'})

# Progetti dal JSON
for p in data['progetti']:
    slug = p['name'].lower()
    for old, new in [(' ','-'),('—','-'),('&','e'),('à','a'),('è','e'),('é','e'),('ì','i'),('ò','o'),('ù','u')]:
        slug = slug.replace(old, new)
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    slug = slug.strip('-')
    urls.append({
        'loc': 'https://cultura-e.it/portfolio.html#' + slug,
        'lastmod': today,
        'priority': '0.6',
        'changefreq': 'yearly'
    })

# Genera XML
lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for u in urls:
    lines.append('  <url>')
    lines.append('    <loc>' + u['loc'] + '</loc>')
    lines.append('    <lastmod>' + u['lastmod'] + '</lastmod>')
    lines.append('    <priority>' + u['priority'] + '</priority>')
    lines.append('    <changefreq>' + u['changefreq'] + '</changefreq>')
    lines.append('  </url>')
lines.append('</urlset>')

with open('/Users/I057265/cultura_e_netlify/sitemap.xml','w') as f:
    f.write('\n'.join(lines) + '\n')

print('DONE - ' + str(len(urls)) + ' URL nella sitemap')
