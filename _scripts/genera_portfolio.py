import json, os

base = '/Users/I057265/cultura_e_netlify/projects'

def get_images(year, folder):
    path = os.path.join(base, year, folder)
    files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.jpg','.jpeg','.png'))])
    return ['projects/' + year + '/' + folder.replace(' ','%20').replace('&','%26').replace('(','%28').replace(')','%29') + '/' + f.replace(' ','%20').replace('(','%28').replace(')','%29').replace('&','%26') for f in files]

def cover(year, folder):
    imgs = get_images(year, folder)
    return imgs[0] if imgs else ''

progetti = [
  {'name':'La Città dei Bambini e dei Ragazzi','year':'2022','cover':cover('2022','la citta dei bambini e dei ragazzi'),'images':get_images('2022','la citta dei bambini e dei ragazzi')},
  {'name':'Fendi','year':'2022','cover':cover('2022','Fendi'),'images':get_images('2022','Fendi')},
  {'name':'Gatto con gli Stivali 2','year':'2022','cover':cover('2022','Gatto con gli Stivali 2'),'images':get_images('2022','Gatto con gli Stivali 2')},
  {'name':'Museo Virtuale della Musica Belliniana','year':'2022','cover':cover('2022','Museo Virtuale della Musica Belliniana'),'images':get_images('2022','Museo Virtuale della Musica Belliniana')},
  {'name':'Parco Italia in Miniatura — Pinocchio','year':'2022','cover':cover('2022','Parco Italia in Miniatura - Pinocchio'),'images':get_images('2022','Parco Italia in Miniatura - Pinocchio')},
  {'name':'Presepe Piazza di Spagna','year':'2022','cover':cover('2022','Presepe Piazza di Spagna'),'images':get_images('2022','Presepe Piazza di Spagna')},
  {'name':'Bulgari','year':'2023','cover':cover('2023','Bulgari'),'images':get_images('2023','Bulgari')},
  {'name':'Bulldog','year':'2023','cover':cover('2023','Bulldog'),'images':get_images('2023','Bulldog')},
  {'name':'Presentazione Film — Prendi il Volo','year':'2023','cover':cover('2023','Presentazione Film - Prendi il Volo'),'images':get_images('2023','Presentazione Film - Prendi il Volo')},
  {'name':'Produzione Karaoke','year':'2023','cover':cover('2023','Produzione Karaoke'),'images':get_images('2023','Produzione Karaoke')},
  {'name':'La TV delle Ragazze RAI','year':'2024','cover':cover('2024','La TV delle Ragazze RAI'),'images':get_images('2024','La TV delle Ragazze RAI')},
  {'name':'New Balance','year':'2024','cover':cover('2024','New Balance'),'images':get_images('2024','New Balance')},
  {'name':'Peroni','year':'2024','cover':cover('2024','Peroni'),'images':get_images('2024','Peroni')},
  {'name':'RAFFO','year':'2024','cover':cover('2024','RAFFO'),'images':get_images('2024','RAFFO')},
  {'name':'Teatrino Topo Gigio RAI','year':'2024','cover':cover('2024','Teatrino Topo Gigio RAI'),'images':get_images('2024','Teatrino Topo Gigio RAI')},
  {'name':'The Golden Bachelor','year':'2024','cover':cover('2024','The Golden Bachelor'),'images':get_images('2024','The Golden Bachelor')},
  {'name':'Bello di Mamma — Enrico Brignano','year':'2025','cover':cover('2025','Bello di Mamma - Enrico Brignano'),'images':get_images('2025','Bello di Mamma - Enrico Brignano')},
  {'name':'In & Out','year':'2025','cover':cover('2025','In & Out'),'images':get_images('2025','In & Out')},
  {'name':'RIP Amazon Prime','year':'2025','cover':cover('2025','RIP Amazon Prime'),'images':get_images('2025','RIP Amazon Prime')},
  {'name':'Studio Nettuno','year':'2025','cover':cover('2025','Studio Nettuno'),'images':get_images('2025','Studio Nettuno')},
  {'name':'Toy Room','year':'2025','cover':cover('2025','Toy Room'),'images':get_images('2025','Toy Room')},
  {'name':'Carrozza Western','year':'2026','cover':cover('2026','Carrozza Western'),'images':get_images('2026','Carrozza Western')},
]

out = {'progetti': progetti}
with open('/Users/I057265/cultura_e_netlify/_data/portfolio.json','w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print('DONE')