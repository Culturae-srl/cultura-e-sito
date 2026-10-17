import csv

rows = [
    {'Slug':'eredita-rai-uno','Titolo':"L'Eredità — RAI Uno",'Anno':'2019','N. Foto':'9','Committente':'RAI','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia televisiva','Note aggiuntive':"Realizzazione scenografia per il quiz show L'Eredità in onda su RAI Uno"},
    {'Slug':'zucchero-rai-uno','Titolo':'Zucchero — RAI Uno','Anno':'2019','N. Foto':'15','Committente':'RAI','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia televisiva','Note aggiuntive':'Allestimento scenografico per lo speciale televisivo di Zucchero su RAI Uno'},
    {'Slug':'rai-parlamento','Titolo':'RAI Parlamento','Anno':'2019','N. Foto':'7','Committente':'RAI','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia studio televisivo','Note aggiuntive':'Realizzazione scenografia per lo studio di RAI Parlamento'},
    {'Slug':'bancone-ansa','Titolo':'Bancone ANSA','Anno':'2019','N. Foto':'4','Committente':'ANSA','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento studio giornalistico','Note aggiuntive':"Realizzazione bancone per lo studio dell'agenzia di stampa ANSA"},
    {'Slug':'studio-ansa','Titolo':'Studio ANSA','Anno':'2019','N. Foto':'2','Committente':'ANSA','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento studio giornalistico','Note aggiuntive':'Allestimento completo dello studio televisivo per ANSA'},
    {'Slug':'shrek','Titolo':'Shrek — Evento','Anno':'2016','N. Foto':'10','Committente':'','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia evento','Note aggiuntive':'Scenografia ispirata al personaggio Shrek per evento'},
    {'Slug':'expo-2015','Titolo':'Expo 2015','Anno':'2015','N. Foto':'51','Committente':'','Location':'Milano','Scenografo':'','Tipo progetto':'Allestimento espositivo','Note aggiuntive':'Allestimento per Expo Milano 2015'},
    {'Slug':'the-illusionist','Titolo':'The Illusionist','Anno':'2013-2014','N. Foto':'10','Committente':'','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia spettacolo','Note aggiuntive':'Scenografia per lo spettacolo The Illusionist'},
    {'Slug':'kandu-2018','Titolo':'KANDU — Città dei Mestieri','Anno':'2018','N. Foto':'195','Committente':'','Location':'Roma','Scenografo':'Christian Taraborelli','Tipo progetto':'Allestimento parco tematico per bambini','Note aggiuntive':'Realizzazione di una intera città in miniatura per bambini con oltre 20 ambientazioni: barbiere, pizzeria, ospedale, vigili del fuoco, banca, teatro e molte altre'},
    {'Slug':'villaggio-natale-luneur','Titolo':'Villaggio di Natale — Luneur','Anno':'2017','N. Foto':'46','Committente':'Luneur Park','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento parco tematico natalizio','Note aggiuntive':'Realizzazione del Villaggio di Natale per il parco divertimenti Luneur di Roma'},
    {'Slug':'volarium-cinecitta-world','Titolo':'Volarium — Cinecittà World','Anno':'','N. Foto':'17','Committente':'Cinecittà World','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento parco divertimenti','Note aggiuntive':'Realizzazione allestimento scenografico per il Volarium di Cinecittà World'},
    {'Slug':'facciamo-che-io-ero','Titolo':'Facciamo che io ero...','Anno':'2017','N. Foto':'126','Committente':'','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia televisiva','Note aggiuntive':'Scenografia per il programma televisivo Facciamo che io ero'},
    {'Slug':'quirinale-2012','Titolo':'Primo Giorno di Scuola — Quirinale','Anno':'2012','N. Foto':'4','Committente':'Presidenza della Repubblica','Location':'Roma — Quirinale','Scenografo':'','Tipo progetto':'Allestimento istituzionale','Note aggiuntive':'Allestimento scenografico per la cerimonia del Primo Giorno di Scuola al Palazzo del Quirinale'},
    {'Slug':'sfilata-hotel-de-russie','Titolo':'Sfilata Hotel De Russie','Anno':'','N. Foto':'3','Committente':'Hotel De Russie','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento evento moda','Note aggiuntive':'Allestimento scenografico per sfilata di moda presso Hotel De Russie Roma'},
    {'Slug':'soggetti-migranti','Titolo':'Soggetti Migranti','Anno':'','N. Foto':'10','Committente':'','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento espositivo','Note aggiuntive':'Allestimento per la mostra Soggetti Migranti'},
    {'Slug':'dive-cinema-italiano','Titolo':'Dive del Cinema Italiano','Anno':'2010','N. Foto':'12','Committente':'','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento espositivo','Note aggiuntive':'Allestimento per la mostra Dive del Cinema Italiano'},
    {'Slug':'rds-academy','Titolo':'RDS Academy','Anno':'','N. Foto':'9','Committente':'RDS','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento studio radiofonico','Note aggiuntive':'Allestimento scenografico per RDS Academy'},
    {'Slug':'alien-revenge','Titolo':'Alien Revenge','Anno':'','N. Foto':'4','Committente':'','Location':'Roma','Scenografo':'','Tipo progetto':'Scenografia evento','Note aggiuntive':'Scenografia per evento Alien Revenge'},
    {'Slug':'bookshop-mondadori','Titolo':'Bookshop Mondadori','Anno':'','N. Foto':'23','Committente':'Mondadori','Location':'Roma','Scenografo':'','Tipo progetto':'Allestimento bookshop','Note aggiuntive':'Allestimento scenografico per bookshop Mondadori'},
    {'Slug':'sagome-lungotevere','Titolo':'Sagome sul Lungotevere','Anno':'','N. Foto':'11','Committente':'','Location':'Roma — Lungotevere','Scenografo':'','Tipo progetto':'Installazione pubblica','Note aggiuntive':'Installazione di sagome scenografiche sul Lungotevere di Roma'},
    {'Slug':'roccia-jeep','Titolo':'Roccia Jeep','Anno':'2015-2019','N. Foto':'8','Committente':'Jeep','Location':'','Scenografo':'','Tipo progetto':'Allestimento brand activation','Note aggiuntive':'Realizzazione roccia scenografica per brand activation Jeep'},
]

fields = ['Slug','Titolo','Anno','N. Foto','Committente','Location','Scenografo','Tipo progetto','Note aggiuntive']

with open('/Users/I057265/cultura_e_netlify/_scripts/blog_da_compilare.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print('DONE - ' + str(len(rows)) + ' storie nel CSV')