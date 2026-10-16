import os

new_favicon_tags = '''  <link rel="icon" type="image/x-icon" href="/images/logos/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/logos/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/logos/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/logos/apple-touch-icon.png">'''

old_favicon = '<link rel="icon" href="images/logos/logo.png" type="image/png">'

pages = [
    '/Users/I057265/cultura_e_netlify/index.html',
    '/Users/I057265/cultura_e_netlify/servizi.html',
    '/Users/I057265/cultura_e_netlify/chi-siamo.html',
    '/Users/I057265/cultura_e_netlify/portfolio.html',
    '/Users/I057265/cultura_e_netlify/contatti.html',
    '/Users/I057265/cultura_e_netlify/privacy.html',
    '/Users/I057265/cultura_e_netlify/grazie.html',
]

for page in pages:
    if not os.path.exists(page):
        print('NON TROVATO: ' + page)
        continue
    with open(page, 'r') as f:
        c = f.read()
    if old_favicon in c:
        c = c.replace(old_favicon, new_favicon_tags)
        with open(page, 'w') as f:
            f.write(c)
        print('OK: ' + page.split('/')[-1])
    else:
        print('tag non trovato: ' + page.split('/')[-1])

print('DONE')