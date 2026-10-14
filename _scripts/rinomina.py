import os, json, re
from urllib.parse import unquote

base = '/Users/I057265/cultura_e_netlify/projects'
json_path = '/Users/I057265/cultura_e_netlify/_data/portfolio.json'

with open(json_path, 'r') as f:
    data = json.load(f)

def slugify(name):
    replacements = {
        'à':'a','è':'e','é':'e','ì':'i','ò':'o','ù':'u',
        'À':'a','È':'e','É':'e','Ì':'i','Ò':'o','Ù':'u',
        '—':'-','&':'e',' ':'-'
    }
    for k,v in replacements.items():
        name = name.replace(k,v)
    name = name.lower()
    name = re.sub(r'[^a-z0-9\-]', '', name)
    name = re.sub(r'-+', '-', name).strip('-')
    return name

for progetto in data['progetti']:
    year = progetto['year']
    name = progetto['name']
    slug = slugify(name)

    folder_name = None
    if progetto['images']:
        parts = progetto['images'][0].split('/')
        folder_name = unquote(parts[2])

    if not folder_name:
        print('CARTELLA NON TROVATA: ' + name)
        continue

    folder_path = os.path.join(base, year, folder_name)
    if not os.path.isdir(folder_path):
        print('DIRECTORY NON ESISTE: ' + folder_path)
        continue

    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg','.jpeg','.png'))])

    new_images = []
    new_cover = None

    for i, filename in enumerate(files, 1):
        ext = os.path.splitext(filename)[1].lower()
        new_name = slug + '-' + str(i) + ext
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        if old_path != new_path:
            os.rename(old_path, new_path)
            print('  ' + filename + ' -> ' + new_name)
        encoded_folder = folder_name.replace(' ', '%20').replace('&', '%26')
        new_url = 'projects/' + year + '/' + encoded_folder + '/' + new_name
        new_images.append(new_url)
        if i == 1:
            new_cover = new_url

    progetto['images'] = new_images
    progetto['cover'] = new_cover
    print('OK: ' + name + ' (' + str(len(new_images)) + ' immagini)')

with open(json_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('DONE')