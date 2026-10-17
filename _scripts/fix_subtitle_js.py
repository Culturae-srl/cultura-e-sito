with open('/Users/I057265/cultura_e_netlify/js/main.js', 'r') as f:
    c = f.read()

# Aggiungi variabile lbSubtitle
old1 = """      var lbName    = document.getElementById('lbName');
      var lbYear    = document.getElementById('lbYear');"""

new1 = """      var lbName     = document.getElementById('lbName');
      var lbSubtitle = document.getElementById('lbSubtitle');
      var lbYear     = document.getElementById('lbYear');"""

# Popola lbSubtitle in openProject
old2 = """        lbName.textContent = item.getAttribute('data-name');
        lbYear.textContent = item.getAttribute('data-year');"""

new2 = """        lbName.textContent = item.getAttribute('data-name');
        if (lbSubtitle) lbSubtitle.textContent = item.getAttribute('data-subtitle') || '';
        lbYear.textContent = item.getAttribute('data-year');"""

if old1 in c:
    c = c.replace(old1, new1)
    print('var OK')
else:
    print('var NON TROVATA')

if old2 in c:
    c = c.replace(old2, new2)
    print('openProject OK')
else:
    print('openProject NON TROVATO')

with open('/Users/I057265/cultura_e_netlify/js/main.js', 'w') as f:
    f.write(c)

print('DONE')