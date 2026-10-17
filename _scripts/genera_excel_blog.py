import csv

rows = [
    {
        'Slug': 'eredita-rai-uno',
        'Titolo': "L'Eredità — RAI Uno",
        'Anno': '2019',
        'N. Foto': '9',
        'Committente': 'RAI',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Scenografia televisiva',
        'Note aggiuntive': 'Realizzazione scenografia per il quiz show L\'Eredità in onda su RAI Uno',
    },
    {
        'Slug': 'zucchero-rai-uno',
        'Titolo': 'Zucchero — RAI Uno',
        'Anno': '2019',
        'N. Foto': '15',
        'Committente': 'RAI',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Scenografia televisiva',
        'Note aggiuntive': 'Allestimento scenografico per lo speciale televisivo di Zucchero su RAI Uno',
    },
    {
        'Slug': 'rai-parlamento',
        'Titolo': 'RAI Parlamento',
        'Anno': '2019',
        'N. Foto': '7',
        'Committente': 'RAI',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Scenografia studio televisivo',
        'Note aggiuntive': 'Realizzazione scenografia per lo studio di RAI Parlamento',
    },
    {
        'Slug': 'bancone-ansa',
        'Titolo': 'Bancone ANSA',
        'Anno': '2019',
        'N. Foto': '4',
        'Committente': 'ANSA',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Allestimento studio giornalistico',
        'Note aggiuntive': 'Realizzazione bancone per lo studio dell\'agenzia di stampa ANSA',
    },
    {
        'Slug': 'studio-ansa',
        'Titolo': 'Studio ANSA',
        'Anno': '2019',
        'N. Foto': '2',
        'Committente': 'ANSA',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Allestimento studio giornalistico',
        'Note aggiuntive': 'Allestimento completo dello studio televisivo per ANSA',
    },
    {
        'Slug': 'shrek',
        'Titolo': 'Shrek — Evento',
        'Anno': '2016',
        'N. Foto': '10',
        'Committente': '',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Scenografia evento/spettacolo',
        'Note aggiuntive': 'Scenografia ispirata al personaggio Shrek per evento',
    },
    {
        'Slug': 'expo-2015',
        'Titolo': 'Expo 2015',
        'Anno': '2015',
        'N. Foto': '51',
        'Committente': '',
        'Location': 'Milano',
        'Scenografo': '',
        'Tipo progetto': 'Allestimento espositivo',
        'Note aggiuntive': 'Allestimento per Expo Milano 2015',
    },
    {
        'Slug': 'the-illusionist',
        'Titolo': 'The Illusionist',
        'Anno': '2013-2014',
        'N. Foto': '10',
        'Committente': '',
        'Location': 'Roma',
        'Scenografo': '',
        'Tipo progetto': 'Scenografia spettacolo',
        'Note aggiuntive': 'Scenografia per lo spettacolo The Illusionist',
    },
]

fields = ['Slug','Titolo','Anno','N. Foto','Committente','Location','Scenografo','Tipo progetto','Note aggiuntive']

with open('/Users/I057265/cultura_e_netlify/_scripts/blog_da_compilare.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print('DONE - file salvato in _scripts/blog_da_compilare.csv')