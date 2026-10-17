# Contesto Progetto — Cultura è... S.r.l.

## Il Sito
- **URL**: https://cultura-e.it
- **Repository GitHub**: https://github.com/Culturae-srl/cultura-e-sito
- **Hosting**: Netlify (piano gratuito → da aggiornare a Personal $9/mese per rimuovere barra)
- **Dominio**: cultura-e.it registrato su Register.it, nameserver puntati a Netlify (dns1-4.p01.nsone.net)
- **Cartella locale**: /Users/I057265/cultura_e_netlify

---

## Struttura del Sito

### Pagine HTML
- `index.html` — Home con hero carousel, settori, portfolio highlights
- `chi-siamo.html` — Chi siamo
- `servizi.html` — Servizi con sector cards
- `portfolio.html` — Portfolio completo (generato da JSON)
- `contatti.html` — Form contatti (Netlify Forms)
- `privacy.html` — Privacy Policy GDPR
- `grazie.html` — Pagina di ringraziamento dopo form

### Dati
- `_data/portfolio.json` — Fonte dati per tutti i progetti (name, year, cover, images, alt, subtitle)

### JS/CSS
- `css/style.css` — Stile principale
- `js/main.js` — Logica: i18n IT/EN, lightbox, portfolio filter, scroll animations

### Immagini
- `projects/ANNO/NomeProgetto/` — Immagini progetti portfolio (rinominate SEO)
- `images/Selection/` — Immagini hero carousel (rinominate SEO: scenografia-allestimento-roma-1.jpg ecc.)
- `images/logos/` — Loghi clienti e favicon
- `blog/images/SLUG/` — Immagini post blog (rinominate SEO)

---

## Portfolio (22 progetti attivi 2022-2026)

| Nome | Anno | Subtitle |
|------|------|----------|
| La Città dei Bambini e dei Ragazzi | 2022 | Acquario di Genova · Scenografo Christian Taraborelli |
| Fendi | 2022 | |
| Gatto con gli Stivali 2 | 2022 | CC Porta di Roma |
| Museo Virtuale della Musica Belliniana | 2022 | Museo Belliniano, Catania · Prod. Civita Mostre e Musei |
| Parco Italia in Miniatura — Pinocchio | 2022 | Scenografo Christian Taraborelli |
| Presepe Piazza di Spagna | 2022 | |
| Bulgari | 2023 | |
| Bulldog | 2023 | |
| Presentazione Film — Prendi il Volo | 2023 | |
| Produzione Karaoke | 2023 | Scenografo Francesco Mari |
| La TV delle Ragazze RAI | 2024 | RAI · Scenografo Marco Calzavara |
| New Balance | 2024 | |
| Peroni | 2024 | |
| RAFFO | 2024 | |
| Teatrino Topo Gigio RAI | 2024 | RAI · Scenografo Maurizio Zecchin |
| The Golden Bachelor | 2024 | Prod. Freemantle |
| Bello di Mamma — Enrico Brignano | 2025 | Spettacolo teatrale · Scenografo Marco Calzavara |
| In & Out | 2025 | Prod. Stand By Me · Scenografo Marco Calzavara |
| RIP Amazon Prime | 2025 | Amazon Prime Video |
| Studio Nettuno | 2025 | |
| Toy Room | 2025 | Piazza Barberini, Roma |
| Carrozza Western | 2026 | |

---

## Blog (21 storie storiche — IN LAVORAZIONE)

Le immagini sono già copiate e rinominate in `blog/images/SLUG/`.
Il CSV da compilare è in `_scripts/blog_da_compilare.csv`.

| Slug | Titolo | Anno | N. Foto | Stato |
|------|--------|------|---------|-------|
| eredita-rai-uno | L'Eredità — RAI Uno | 2019 | 9 | ⏳ CSV da compilare |
| zucchero-rai-uno | Zucchero — RAI Uno | 2019 | 15 | ⏳ CSV da compilare |
| rai-parlamento | RAI Parlamento | 2019 | 7 | ⏳ CSV da compilare |
| bancone-ansa | Bancone ANSA | 2019 | 4 | ⏳ CSV da compilare |
| studio-ansa | Studio ANSA | 2019 | 2 | ⏳ CSV da compilare |
| shrek | Shrek — Evento | 2016 | 10 | ⏳ CSV da compilare |
| expo-2015 | Expo 2015 | 2015 | 51 | ⏳ CSV da compilare |
| the-illusionist | The Illusionist | 2013-2014 | 10 | ⏳ CSV da compilare |
| kandu-2018 | KANDU — Città dei Mestieri | 2018 | 195 | ⏳ CSV da compilare |
| villaggio-natale-luneur | Villaggio di Natale — Luneur | 2017 | 46 | ⏳ CSV da compilare |
| volarium-cinecitta-world | Volarium — Cinecittà World | ? | 17 | ⏳ CSV da compilare |
| facciamo-che-io-ero | Facciamo che io ero... | 2017 | 126 | ⏳ CSV da compilare |
| quirinale-2012 | Primo Giorno di Scuola — Quirinale | 2012 | 4 | ⏳ CSV da compilare |
| sfilata-hotel-de-russie | Sfilata Hotel De Russie | ? | 3 | ⏳ CSV da compilare |
| soggetti-migranti | Soggetti Migranti | ? | 10 | ⏳ CSV da compilare |
| dive-cinema-italiano | Dive del Cinema Italiano | 2010 | 12 | ⏳ CSV da compilare |
| rds-academy | RDS Academy | ? | 9 | ⏳ CSV da compilare |
| alien-revenge | Alien Revenge | ? | 4 | ⏳ CSV da compilare |
| bookshop-mondadori | Bookshop Mondadori | ? | 23 | ⏳ CSV da compilare |
| sagome-lungotevere | Sagome sul Lungotevere | ? | 11 | ⏳ CSV da compilare |
| roccia-jeep | Roccia Jeep | 2015-2019 | 8 | ⏳ CSV da compilare |

---

## Script _scripts/

| Script | Funzione |
|--------|----------|
| `genera_portfolio.py` | Rigenera portfolio.json dai file fisici |
| `aggiungi_alt.py` | Aggiunge alt text SEO al JSON |
| `aggiungi_subtitle.py` | Aggiunge subtitle ai progetti nel JSON |
| `fix_index2.py` | Aggiorna data-images e src nell'index.html |
| `aggiorna_sitemap.py` | Rigenera sitemap.xml con tutti i progetti |
| `verifica_immagini.py` | Verifica che tutti i path immagini esistano |
| `rinomina.py` | Rinomina immagini progetti con nomi SEO |
| `rinomina_hero.py` | Rinomina immagini hero con nomi SEO |
| `fix_hero.py` | Aggiorna path immagini hero nelle pagine HTML |
| `fix_favicon.py` | Aggiorna tag favicon in tutte le pagine |
| `aggiungi_animazioni.py` | Aggiunge CSS/JS animazioni scroll fade-in |
| `aggiungi_classi_animazioni.py` | Aggiunge classi fade-in agli elementi HTML |
| `copia_blog_immagini.py` | Copia immagini blog (prime 8 storie) |
| `copia_blog_immagini2.py` | Copia immagini blog (13 nuove storie) |
| `genera_excel_blog2.py` | Genera CSV con 21 storie blog da compilare |
| `blog_da_compilare.csv` | CSV con dati blog da completare |

---

## Procedura standard aggiornamento portfolio

```bash
python3 /Users/I057265/cultura_e_netlify/_scripts/genera_portfolio.py
python3 /Users/I057265/cultura_e_netlify/_scripts/aggiungi_alt.py
python3 /Users/I057265/cultura_e_netlify/_scripts/fix_index2.py
python3 /Users/I057265/cultura_e_netlify/_scripts/aggiorna_sitemap.py
python3 /Users/I057265/cultura_e_netlify/_scripts/verifica_immagini.py
# se tutto OK:
git add -A && git commit -m 'messaggio' && git push
```

---

## SEO — Fatto
- ✅ Immagini rinominate con nomi SEO-friendly
- ✅ Alt text descrittivi su tutte le immagini
- ✅ Sitemap.xml con 28 URL (6 pagine + 22 progetti)
- ✅ Meta title, description, OG tags su tutte le pagine
- ✅ Schema.org JSON-LD su tutte le pagine
- ✅ Favicon multi-size (16, 32, 180px + .ico)
- ✅ Animazioni scroll fade-in
- ✅ Cookie banner GDPR
- ✅ Subtitle in corsivo nel lightbox portfolio

## SEO — Da fare
- ⏳ Google Search Console — inviare sitemap
- ⏳ Blog con 21 storie storiche
- ⏳ Social media nel footer
- ⏳ Google Analytics
- ⏳ Pagine dedicate per ogni progetto portfolio

---

## Repertorio storico
- **Percorso**: /Users/I057265/Culturae_Repertorio
- Contiene progetti dal 2010 al 2021 non ancora sul sito
- Le immagini sono già copiate in blog/images/ e rinominate

---

## Note tecniche
- Sito HTML statico puro (no framework, no build step)
- i18n IT/EN gestito via JS (data-i18n attributes)
- Portfolio caricato dinamicamente da _data/portfolio.json
- Lightbox con galleria immagini e subtitle
- Form contatti gestito da Netlify Forms
- Cookie banner GDPR con localStorage
