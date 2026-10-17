with open('/Users/I057265/cultura_e_netlify/css/style.css', 'r') as f:
    c = f.read()

old = """.lightbox-caption .lb-year {
  font-size: 12px;
  color: var(--red-light);
  letter-spacing: 1px;
}"""

new = """.lightbox-caption .lb-subtitle {
  font-size: 12px;
  font-style: italic;
  color: rgba(255,255,255,0.7);
  margin-top: 2px;
}

.lightbox-caption .lb-year {
  font-size: 12px;
  color: var(--red-light);
  letter-spacing: 1px;
}"""

if old in c:
    c = c.replace(old, new)
    with open('/Users/I057265/cultura_e_netlify/css/style.css', 'w') as f:
        f.write(c)
    print('CSS OK')
else:
    print('STRINGA NON TROVATA')