import json, os, re
from urllib.parse import unquote

data = json.load(open('/Users/I057265/cultura_e_netlify/_data/portfolio.json'))
base = '/Users/I057265/cultura_e_netlify'

print('=== VERIFICA JSON ===')
for p in data['progetti']:
    cover_path = os.path.join(base, unquote(p['cover']))
    if not os.path.exists(cover_path):
        print('COVER MANCANTE: ' + p['name'] + ' -> ' + cover_path)
    else:
        print('OK cover: ' + p['name'])
    for img in p['images'][:3]:
        img_path = os.path.join(base, unquote(img))
        if not os.path.exists(img_path):
            print('  IMG MANCANTE: ' + img_path)

print('')
print('=== VERIFICA PATH HARDCODED NELLE PAGINE HTML ===')
pages = ['index.html', 'servizi.html', 'portfolio.html', 'chi-siamo.html']
pattern = re.compile(r'projects/[^\s\'"\)>]+')

for page in pages:
    path = os.path.join(base, page)
    if not os.path.exists(path):
        continue
    with open(path, 'r') as f:
        content = f.read()
    matches = pattern.findall(content)
    errori = []
    for match in matches:
        file_path = os.path.join(base, unquote(match))
        if not os.path.exists(file_path):
            errori.append(match)
    if errori:
        print('ERRORI in ' + page + ':')
        for e in errori:
            print('  MANCANTE: ' + e)
    else:
        print('OK: ' + page)

print('')
print('VERIFICA COMPLETATA')
