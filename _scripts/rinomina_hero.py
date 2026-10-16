import os

base = '/Users/I057265/cultura_e_netlify/images/Selection'

# Mappa vecchio nome -> nuovo nome SEO
rinomina = {
    '54c38353-a9cf-4a4f-b18b-8287ba28d979.jpg': 'scenografia-allestimento-roma-1.jpg',
    '9ef004f2-9a4a-4580-8948-828a252fdb60.jpg': 'scenografia-allestimento-roma-2.jpg',
    '83a1e727-52d9-4127-a144-f5258c13f54e.jpg': 'scenografia-allestimento-roma-3.jpg',
    'c9b60221-a981-4792-abba-2d10d52f4e27.jpg': 'scenografia-allestimento-roma-4.jpg',
    '6275c31d-afdf-4645-9245-0612d4877d5e.jpg': 'scenografia-allestimento-roma-5.jpg',
    'b089fe0e-5fe4-4901-ba63-398541528f63.jpg': 'scenografia-allestimento-roma-6.jpg',
    '10f0edaa-ab32-4564-85df-5ce8b86002c9.jpg': 'scenografia-allestimento-roma-7.jpg',
    '2a71f892-0012-46ae-86f3-1724a8991b05.jpg': 'scenografia-allestimento-roma-8.jpg',
    '26fc5384-697d-45e2-afe1-01f2deba6300.jpg': 'scenografia-allestimento-roma-9.jpg',
    'Screenshot 2026-09-13 at 18.43.53.png':    'scenografia-allestimento-roma-10.png',
}

for old, new in rinomina.items():
    old_path = os.path.join(base, old)
    new_path = os.path.join(base, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(old + ' -> ' + new)
    else:
        print('NON TROVATO: ' + old)

print('DONE')