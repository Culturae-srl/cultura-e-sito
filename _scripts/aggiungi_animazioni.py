css_animations = '''

/* ── SCROLL ANIMATIONS ── */
.fade-in {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}
.fade-in-left {
  opacity: 0;
  transform: translateX(-30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-in-left.visible {
  opacity: 1;
  transform: translateX(0);
}
.fade-in-right {
  opacity: 0;
  transform: translateX(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-in-right.visible {
  opacity: 1;
  transform: translateX(0);
}
'''

js_animations = '''

/* ── SCROLL FADE-IN ── */
(function() {
  var els = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
  if (!els.length) return;
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  els.forEach(function(el) { observer.observe(el); });
}());
'''

# Aggiungi CSS
with open('/Users/I057265/cultura_e_netlify/css/style.css', 'a') as f:
    f.write(css_animations)
print('CSS OK')

# Aggiungi JS
with open('/Users/I057265/cultura_e_netlify/js/main.js', 'a') as f:
    f.write(js_animations)
print('JS OK')

print('DONE')