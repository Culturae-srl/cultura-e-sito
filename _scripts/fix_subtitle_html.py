with open('/Users/I057265/cultura_e_netlify/portfolio.html', 'r') as f:
    c = f.read()

old = 'return \'<div class="portfolio-item fade-in" data-year="\' + p.year + \'" data-name="\' + p.name + \'" data-images=\\\'' + JSON.stringify(p.images) + \'\\\'>\' +'

new = 'return \'<div class="portfolio-item fade-in" data-year="\' + p.year + \'" data-name="\' + p.name + \'" data-subtitle="\' + (p.subtitle || \'\') + \'" data-images=\\\'' + JSON.stringify(p.images) + \'\\\'>\' +'

if old in c:
    c = c.replace(old, new)
    with open('/Users/I057265/cultura_e_netlify/portfolio.html', 'w') as f:
        f.write(c)
    print('OK')
else:
    print('NON TROVATO - provo con replace diretto')
    # approccio alternativo: trova la riga e sostituiscila
    lines = c.split('\n')
    for i, line in enumerate(lines):
        if 'data-images' in line and 'portfolio-item fade-in' in line and 'data-subtitle' not in line:
            lines[i] = line.replace(
                'data-images=',
                'data-subtitle="\' + (p.subtitle || \'\') + \'" data-images='
            )
            print('OK riga ' + str(i+1))
    c = '\n'.join(lines)
    with open('/Users/I057265/cultura_e_netlify/portfolio.html', 'w') as f:
        f.write(c)
    print('DONE')
