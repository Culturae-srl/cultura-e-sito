import re

pages = [
    '/Users/I057265/cultura_e_netlify/index.html',
    '/Users/I057265/cultura_e_netlify/servizi.html',
    '/Users/I057265/cultura_e_netlify/chi-siamo.html',
    '/Users/I057265/cultura_e_netlify/portfolio.html',
    '/Users/I057265/cultura_e_netlify/contatti.html',
]

replacements = [
    # section labels
    ('<div class="section-label"', '<div class="section-label fade-in"'),
    # section titles
    ('<h2 class="section-title"', '<h2 class="section-title fade-in"'),
    # service cards
    ('<div class="service-card"', '<div class="service-card fade-in"'),
    # portfolio items
    ('<div class="portfolio-item"', '<div class="portfolio-item fade-in"'),
    # process steps
    ('<div class="process-step"', '<div class="process-step fade-in"'),
    # stat items
    ('<div class="stat-item"', '<div class="stat-item fade-in"'),
    # client cards
    ('<div class="client-card"', '<div class="client-card fade-in"'),
    # sector cards
    ('<div class="sector-card"', '<div class="sector-card fade-in"'),
    # about photo col
    ('<div class="about-photo-col"', '<div class="about-photo-col fade-in-right"'),
    # about text col
    ('<div class="about-text-col"', '<div class="about-text-col fade-in-left"'),
    # section intro
    ('<p class="section-intro"', '<p class="section-intro fade-in"'),
    # cta band
    ('<section class="cta-band"', '<section class="cta-band fade-in"'),
]

for page in pages:
    try:
        with open(page, 'r') as f:
            c = f.read()
        changed = False
        for old, new in replacements:
            if old in c:
                c = c.replace(old, new)
                changed = True
        if changed:
            with open(page, 'w') as f:
                f.write(c)
            print('OK: ' + page.split('/')[-1])
        else:
            print('nessuna modifica: ' + page.split('/')[-1])
    except FileNotFoundError:
        print('NON TROVATO: ' + page)

print('DONE')