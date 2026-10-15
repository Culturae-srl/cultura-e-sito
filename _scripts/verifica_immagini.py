import json, os
from urllib.parse import unquote

data = json.load(open('/Users/I057265/cultura_e_netlify/_data/portfolio.json'))
base = '/Users/I057265/cultura_e_netlify'

for p in data['progetti']:
    # verifica cover
    cover_path = os.path.join(base, unquote(p['cover']))
    if not os.path.exists(cover_path):
        print('COVER MANCANTE: ' + p['name'] + ' -> ' + cover_path)
    else:
        print('OK cover: ' + p['name'])
    # verifica prime 3 immagini
    for img in p['images'][:3]:
        img_path = os.path.join(base, unquote(img))
        if not os.path.exists(img_path):
            print('  IMG MANCANTE: ' + img_path)