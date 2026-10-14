import json

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','r') as f:
    data = json.load(f)

# Alt text descrittivi per ogni progetto
alt_texts = {
    'La Città dei Bambini e dei Ragazzi': 'Scenografia per La Città dei Bambini e dei Ragazzi — allestimento espositivo Roma',
    'Fendi': 'Scenografia e allestimento per evento Fendi — luxury brand activation Roma',
    'Gatto con gli Stivali 2': 'Scenografia per Gatto con gli Stivali 2 — installazione scenotecnica evento cinema',
    'Museo Virtuale della Musica Belliniana': 'Allestimento Museo Virtuale della Musica Belliniana — scenografia culturale',
    'Parco Italia in Miniatura — Pinocchio': 'Scenografia Pinocchio per Parco Italia in Miniatura — installazione scenotecnica',
    'Presepe Piazza di Spagna': 'Allestimento Presepe Piazza di Spagna Roma — scenografia natalizia',
    'Bulgari': 'Scenografia e allestimento per evento BVLGARI — luxury brand activation Roma',
    'Bulldog': 'Allestimento scenografico per Bulldog Gin — brand activation evento',
    'Presentazione Film — Prendi il Volo': 'Scenografia per presentazione film Prendi il Volo — allestimento cinematografico Roma',
    'Produzione Karaoke': 'Scenografia produzione Karaoke — set design televisivo Roma',
    'La TV delle Ragazze RAI': 'Scenografia La TV delle Ragazze RAI — set design produzione televisiva RAI Roma',
    'New Balance': 'Allestimento scenografico New Balance — brand activation sportswear Roma',
    'Peroni': 'Scenografia per evento Peroni — allestimento brand activation birra Roma',
    'RAFFO': 'Allestimento scenografico RAFFO — brand activation evento Roma',
    'Teatrino Topo Gigio RAI': 'Scenografia Teatrino Topo Gigio RAI — set design produzione televisiva RAI',
    'The Golden Bachelor': 'Scenografia The Golden Bachelor — allestimento produzione televisiva Roma',
    'Bello di Mamma — Enrico Brignano': 'Scenografia Bello di Mamma con Enrico Brignano — set design spettacolo teatrale',
    'In & Out': 'Allestimento scenografico In & Out — installazione scenotecnica Roma',
    'RIP Amazon Prime': 'Scenografia RIP Amazon Prime — set design produzione streaming Roma',
    'Studio Nettuno': 'Allestimento Studio Nettuno — scenografia studio televisivo Roma',
    'Toy Room': 'Scenografia Toy Room — allestimento espositivo installazione Roma',
    'Carrozza Western': 'Scenografia Carrozza Western — installazione scenotecnica ambientazione western',
}

for p in data['progetti']:
    nome = p['name']
    if nome in alt_texts:
        p['alt'] = alt_texts[nome]
    else:
        p['alt'] = 'Scenografia e allestimento ' + nome + ' — Cultura è... Roma'

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('DONE - alt text aggiunti a ' + str(len(data['progetti'])) + ' progetti')