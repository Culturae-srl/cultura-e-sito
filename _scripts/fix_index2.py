import json, re

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','r') as f:
    data = json.load(f)

progetti = {p['name']: p for p in data['progetti']}

with open('/Users/I057265/cultura_e_netlify/index.html','r') as f:
    html = f.read()

nomi_home = ['Fendi','Bulgari','Teatrino Topo Gigio RAI','New Balance','Gatto con gli Stivali 2']

for nome in nomi_home:
    p = progetti[nome]
    new_imgs_str = json.dumps(p['images'], ensure_ascii=False)
    new_cover = p['cover']

    # sostituisce data-images nel blocco con data-name corretto
    pattern = r'(data-name="' + re.escape(nome) + r'"[^>]*data-images=\')'  + r"[^']*" + r"(')"
    replacement = r'\1' + new_imgs_str + r'\2'
    html = re.sub(pattern, replacement, html, flags=re.DOTALL)

    # sostituisce src immagine
    pattern_src = r'(data-name="' + re.escape(nome) + r'"[\s\S]*?<img src=")[^"]*(")'
    replacement_src = r'\1' + new_cover + r'\2'
    html = re.sub(pattern_src, replacement_src, html, flags=re.DOTALL)

with open('/Users/I057265/cultura_e_netlify/index.html','w') as f:
    f.write(html)

print('DONE')