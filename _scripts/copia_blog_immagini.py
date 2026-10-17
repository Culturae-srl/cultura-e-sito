import os, shutil

repertorio = '/Users/I057265/Culturae_Repertorio'
blog_imgs = '/Users/I057265/cultura_e_netlify/blog/images'

posts = [
    {
        'slug': 'eredita-rai-uno',
        'src': os.path.join(repertorio, 'Eredità Rai Uno'),
    },
    {
        'slug': 'zucchero-rai-uno',
        'src': os.path.join(repertorio, 'zucchero rai uno 2019'),
    },
    {
        'slug': 'rai-parlamento',
        'src': os.path.join(repertorio, 'rai parlamento 2019'),
    },
    {
        'slug': 'bancone-ansa',
        'src': os.path.join(repertorio, 'BANCONE ANSA 2019'),
    },
    {
        'slug': 'studio-ansa',
        'src': os.path.join(repertorio, 'studio ANSA 2019'),
    },
    {
        'slug': 'shrek',
        'src': os.path.join(repertorio, 'shrek'),
    },
    {
        'slug': 'expo-2015',
        'src': os.path.join(repertorio, 'expo 2015'),
    },
    {
        'slug': 'the-illusionist',
        'src': os.path.join(repertorio, 'the illusionist 2013 e 2014'),
    },
]

exts = ('.jpg','.jpeg','.png','.JPG','.JPEG','.PNG')

for post in posts:
    slug = post['slug']
    src_dir = post['src']
    dst_dir = os.path.join(blog_imgs, slug)
    
    if not os.path.isdir(src_dir):
        print('NON TROVATA: ' + src_dir)
        continue
    
    files = sorted([f for f in os.listdir(src_dir) if os.path.splitext(f)[1] in exts])
    
    for i, f in enumerate(files, 1):
        ext = os.path.splitext(f)[1].lower()
        new_name = slug + '-' + str(i) + ext
        shutil.copy2(os.path.join(src_dir, f), os.path.join(dst_dir, new_name))
    
    print('OK: ' + slug + ' (' + str(len(files)) + ' immagini)')

print('DONE')