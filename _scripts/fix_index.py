import json

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','r') as f:
    data = json.load(f)

progetti = {p['name']: p for p in data['progetti']}

with open('/Users/I057265/cultura_e_netlify/index.html','r') as f:
    html = f.read()

# Settori card - background images
html = html.replace(
    "projects/2023/Produzione%20Karaoke/Screenshot%202026-09-13%20at%2018.30.41.jpg",
    "projects/2023/Produzione%20Karaoke/produzione-karaoke-37.jpg"
)
html = html.replace(
    "projects/2022/la%20citta%20dei%20bambini%20e%20dei%20ragazzi/Screenshot%202026-09-13%20at%2015.04.07.jpg",
    "projects/2022/la%20citta%20dei%20bambini%20e%20dei%20ragazzi/la-citta-dei-bambini-e-dei-ragazzi-19.jpg"
)
html = html.replace(
    "projects/2023/Bulgari/Screenshot%202026-09-13%20at%2018.24.25.jpg",
    "projects/2023/Bulgari/bulgari-1.jpg"
)
html = html.replace(
    "projects/2022/Gatto%20con%20gli%20Stivali%202/Screenshot%202026-09-13%20at%2018.25.35.jpg",
    "projects/2022/Gatto%20con%20gli%20Stivali%202/gatto-con-gli-stivali-2-12.jpg"
)

# Portfolio highlights - aggiorna data-images e src con i nuovi path dal JSON
for nome in ['Fendi','Bulgari','Teatrino Topo Gigio RAI','New Balance','Gatto con gli Stivali 2']:
    p = progetti[nome]
    new_imgs = json.dumps(p['images'], ensure_ascii=False)
    # trova e sostituisce il blocco data-images nel html
    # cerchiamo la cover vecchia (qualsiasi vecchio path per quel progetto)
    # usiamo il cover come ancora
    old_cover = None
    for line in html.split('\n'):
        if 'data-images' in line and nome in html[html.find(line)-200:html.find(line)]:
            pass
    # approccio piu semplice: sostituiamo ogni occorrenza dei vecchi filename
    # I vecchi path contengono ancora "Screenshot" o "IMG_" per questi progetti
    pass

# Fendi
html = html.replace(
    'src="projects/2022/Fendi/fendi-1.jpg"',
    'src="' + progetti['Fendi']['cover'] + '"'
)

# Bulgari  
html = html.replace(
    'src="projects/2023/Bulgari/bulgari-1.jpg"',
    'src="' + progetti['Bulgari']['cover'] + '"'
)

# Teatrino
html = html.replace(
    'src="projects/2024/Teatrino%20Topo%20Gigio%20RAI/teatrino-topo-gigio-rai-1.jpg"',
    'src="' + progetti['Teatrino Topo Gigio RAI']['cover'] + '"'
)

# New Balance
html = html.replace(
    'src="projects/2024/New%20Balance/new-balance-1.jpg"',
    'src="' + progetti['New Balance']['cover'] + '"'
)

# Gatto
html = html.replace(
    'src="projects/2022/Gatto%20con%20gli%20Stivali%202/gatto-con-gli-stivali-2-12.jpg"',
    'src="' + progetti['Gatto con gli Stivali 2']['cover'] + '"'
)

with open('/Users/I057265/cultura_e_netlify/index.html','w') as f:
    f.write(html)

print('DONE')