import os, shutil

repertorio = '/Users/I057265/Culturae_Repertorio'
blog_imgs = '/Users/I057265/cultura_e_netlify/blog/images'
exts = ('.jpg','.jpeg','.png','.JPG','.JPEG','.PNG')

posts = [
    {'slug': 'kandu-2018', 'src': os.path.join(repertorio, 'KANDU 2018')},
    {'slug': 'kandu-2018', 'src': os.path.join(repertorio, 'CULTURA E 2022 2026/KANDU 2018 SCENOGRAFO CHRISTIAN TARABORELLI')},
    {'slug': 'villaggio-natale-luneur', 'src': os.path.join(repertorio, 'VILLAGGIO DI NATALE LUNEUR ANNO 2017')},
    {'slug': 'volarium-cinecitta-world', 'src': os.path.join(repertorio, 'VOLARIUM CINECITTA WORLD')},
    {'slug': 'facciamo-che-io-ero', 'src': os.path.join(repertorio, 'facciamo che io ero 2017')},
    {'slug': 'quirinale-2012', 'src': os.path.join(repertorio, 'primo giorno di scuola Quirinale 2012')},
    {'slug': 'sfilata-hotel-de-russie', 'src': os.path.join(repertorio, 'sfilata hotel derussie roma')},
    {'slug': 'soggetti-migranti', 'src': os.path.join(repertorio, 'soggetti migranti')},
    {'slug': 'dive-cinema-italiano', 'src': os.path.join(repertorio, 'eventi locali/Dive del cinema Italiano 2010')},
    {'slug': 'rds-academy', 'src': os.path.join(repertorio, 'eventi locali/RDS academy')},
    {'slug': 'alien-revenge', 'src': os.path.join(repertorio, 'eventi locali/alien revange')},
    {'slug': 'bookshop-mondadori', 'src': os.path.join(repertorio, 'eventi locali/bookshop mondadori')},
    {'slug': 'sagome-lungotevere', 'src': os.path.join(repertorio, 'eventi locali/sagome sul lungotevere')},
    {'slug': 'roccia-jeep', 'src': os.path.join(repertorio, 'CULTURA E 2022 2026/ROCCIA JEEP ANNI 2015-2019')},
]

# Per KANDU raccogliamo tutte le immagini da tutte le sottocartelle
def get_all_images(src_dir):
    images = []
    for root, dirs, files in os.walk(src_dir):
        for f in sorted(files):
            if os.path.splitext(f)[1] in exts:
                images.append(os.path.join(root, f))
    return sorted(images)

# Contatore per kandu (due sorgenti diverse)
kandu_counter = 1

processed = {}

for post in posts:
    slug = post['slug']
    src_dir = post['src']
    dst_dir = os.path.join(blog_imgs, slug)

    if not os.path.isdir(src_dir):
        print('NON TROVATA: ' + src_dir)
        continue

    if slug == 'kandu-2018':
        # gestione speciale: due cartelle sorgente
        files = get_all_images(src_dir)
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            new_name = slug + '-' + str(kandu_counter) + ext
            shutil.copy2(f, os.path.join(dst_dir, new_name))
            kandu_counter += 1
        print('OK kandu da ' + src_dir.split('/')[-1] + ' (' + str(len(files)) + ' immagini)')
    else:
        if slug not in processed:
            processed[slug] = 1
        files = get_all_images(src_dir)
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            new_name = slug + '-' + str(processed[slug]) + ext
            shutil.copy2(f, os.path.join(dst_dir, new_name))
            processed[slug] += 1
        print('OK: ' + slug + ' (' + str(len(files)) + ' immagini)')

print('DONE')