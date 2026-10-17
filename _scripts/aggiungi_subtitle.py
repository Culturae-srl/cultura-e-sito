import json

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','r') as f:
    data = json.load(f)

subtitles = {
    'La Città dei Bambini e dei Ragazzi': 'Acquario di Genova · Scenografo Christian Taraborelli',
    'Museo Virtuale della Musica Belliniana': 'Museo Belliniano, Catania · Prod. Civita Mostre e Musei',
    'Parco Italia in Miniatura — Pinocchio': 'Scenografo Christian Taraborelli',
    'Gatto con gli Stivali 2': 'CC Porta di Roma',
    'Produzione Karaoke': 'Scenografo Francesco Mari',
    'La TV delle Ragazze RAI': 'RAI · Scenografo Marco Calzavara',
    'Teatrino Topo Gigio RAI': 'RAI · Scenografo Maurizio Zecchin',
    'The Golden Bachelor': 'Prod. Freemantle',
    'Bello di Mamma — Enrico Brignano': 'Spettacolo teatrale · Scenografo Marco Calzavara',
    'In & Out': 'Prod. Stand By Me · Scenografo Marco Calzavara',
    'Toy Room': 'Piazza Barberini, Roma',
    'RIP Amazon Prime': 'Amazon Prime Video',
}

for p in data['progetti']:
    if p['name'] in subtitles:
        p['subtitle'] = subtitles[p['name']]
    else:
        p['subtitle'] = ''

with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('DONE - subtitle aggiunti a ' + str(len(subtitles)) + ' progetti')