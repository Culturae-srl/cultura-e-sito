(function () {
  'use strict';

  /* ── i18n ── */
  var T = {
    it: {
      'nav.about':    'Chi Siamo',
      'nav.services': 'Servizi',
      'nav.portfolio':'Portfolio',
      'nav.clients':  'Clienti',
      'nav.contact':  'Contattaci',

      'hero.eyebrow': 'Scenografie & Allestimenti · Roma',
      'hero.h1':      'IMMAGINA<br>UN <span class="accent">GRANDE</span><br>SPETTACOLO.',
      'hero.subtitle':'Noi lo realizziamo.',
      'hero.cta1':    'Scopri i Nostri Lavori',
      'hero.cta2':    'Richiedi un Preventivo',
      'hero.scroll':  'Scorri',
      'hero.tagline': '<span>Passione</span> &nbsp;·&nbsp; <span>Creatività</span> &nbsp;·&nbsp; <span>Professionalità</span>',

      'about.label':  'Chi Siamo',
      'about.p1':     'Cultura è passione che prende forma nello spazio.',
      'about.p2':     'Siamo specializzati nella progettazione e realizzazione di scenografie, allestimenti espositivi e installazioni scenotecniche per eventi culturali, produzioni televisive, presentazioni cinematografiche e progetti di comunicazione di brand. Ogni ambiente che creiamo nasce da un\'idea e diventa un\'esperienza — visiva, emotiva, reale.',
      'about.p3':     'Operiamo come un\'organizzazione a servizio completo: un ecosistema creativo e tecnico capace di rispondere a qualsiasi sfida progettuale con la velocità, la precisione e la cura che ogni progetto merita. Un solo luogo, un team collaudato, mezzi tecnici all\'avanguardia e macchinari evoluti: tutto ciò che serve per trasformare una visione in realtà, senza compromessi.',
      'about.p4':     'Il nostro team riunisce architetti, scenografi, falegnami, macchinisti, disegnatori, realizzatori, stuccatori, elettricisti, serigrafi, modellisti e grafici. Professionalità diverse, un\'unica anima: l\'eccellenza artigianale al servizio della creatività.',
      'about.p5':     'Perché ogni progetto non è solo un lavoro — è una storia che vale la pena raccontare nello spazio.',
      'about.quote':  '"Ci immergiamo nelle sfide del cliente come fossero nostre — ogni dettaglio, ogni materiale, ogni luce racconta una storia."',
      'about.role':   'Fondatore & Direttore Creativo · 40 anni nel settore',
      'about.stat1':  'Anni di Esperienza',
      'about.stat2':  'Progetti Realizzati',
      'about.stat3':  'Brand Partner',
      'about.readmore': 'Scopri di Più',

      'page.about.label': 'Chi Siamo',
      'page.about.h1':    'L\'Arte della<br><span class="accent">Scenografia</span>',
      'page.services.label': 'I Nostri Servizi',
      'page.services.h1': 'Scenografie e Allestimenti:<br><span class="accent">Dalla Progettazione al Montaggio</span>',
      'page.portfolio.label': 'I Nostri Lavori',
      'page.contact.label': 'Contatti',
      'page.contact.h1':  'Richiedi un Preventivo<br><span class="accent">Scenografie Roma</span>',

      'breadcrumb.about':    'Chi Siamo',
      'breadcrumb.services': 'Servizi',
      'breadcrumb.contact':  'Contatti',

      'values.label': 'I Nostri Valori',
      'values.title': 'Cosa ci <span class="accent">Distingue</span>',
      'values.v1.title': 'Eccellenza Artigianale',
      'values.v1.desc':  'Ogni elemento è costruito a mano dai nostri artigiani con materiali di qualità, nel rispetto delle migliori tradizioni scenografiche italiane.',
      'values.v2.title': 'Rispetto delle Tempistiche',
      'values.v2.desc':  'Nel mondo degli eventi e della televisione, il tempo è tutto. Ogni progetto viene pianificato con precisione per rispettare ogni scadenza senza eccezioni.',
      'values.v3.title': 'Approccio Collaborativo',
      'values.v3.desc':  'Lavoriamo fianco a fianco con il cliente in ogni fase del progetto: dal brief iniziale alla consegna finale, siamo un\'estensione del tuo team creativo.',
      'values.v4.title': 'Creatività Senza Limiti',
      'values.v4.desc':  'Dagli spazi più intimi alle grandi installazioni nazionali, non ci sono confini alla nostra capacità di immaginare e realizzare ambienti straordinari.',
      'values.v5.title': 'Servizio Completo',
      'values.v5.desc':  'Dalla progettazione al montaggio, dalla decorazione allo smontaggio: gestiamo l\'intero processo in-house, garantendo coerenza e qualità in ogni passaggio.',
      'values.v6.title': 'Radicati a Roma',
      'values.v6.desc':  'Con sede operativa a Roma, operiamo su tutto il territorio nazionale portando con noi l\'eccellenza artigianale della Capitale e la sua secolare tradizione scenografica.',

      'process.label': 'Come Lavoriamo',
      'process.title': 'Il Nostro <span class="accent">Processo</span>',
      'process.intro': 'Quattro fasi collaudate per trasformare ogni idea in un\'esperienza scenografica reale.',
      'process.s1.title': 'Briefing & Analisi',
      'process.s1.desc':  'Ascoltiamo le vostre esigenze, analizziamo lo spazio e definiamo insieme obiettivi, budget e timeline per una visione condivisa del progetto.',
      'process.s2.title': 'Concept & Progettazione',
      'process.s2.desc':  'Il team creativo sviluppa concept visivi, tavole di ispirazione e rendering 3D che traducono la visione in un progetto esecutivo approvabile.',
      'process.s3.title': 'Realizzazione',
      'process.s3.desc':  'I nostri artigiani e macchinisti trasformano il progetto in elementi scenografici reali, lavorando ogni materiale con cura e precisione assoluta.',
      'process.s4.title': 'Montaggio & Consegna',
      'process.s4.desc':  'Installiamo ogni elemento in location, rispettando i tempi e i più alti standard qualitativi. Al termine, smontaggio rapido e pulizia completa degli spazi.',

      'cta.home.h2':       'Pronto a <span class="accent">Collaborare</span>?',
      'cta.home.p':        'Raccontaci il tuo progetto — dalla fase di concept al montaggio, siamo al tuo fianco.',
      'cta.about.h2':      'Raccontaci il tuo <span class="accent">Progetto</span>',
      'cta.about.p':       'Siamo pronti ad ascoltarti e a trasformare la tua visione in realtà scenografica.',
      'cta.services.h2':   'Inizia il tuo <span class="accent">Progetto</span>',
      'cta.services.p':    'Contattaci per un preventivo gratuito — rispondiamo entro 48 ore.',
      'cta.portfolio.h2':  'Il tuo <span class="accent">Progetto</span> è il prossimo?',
      'cta.portfolio.p':   'Contattaci per discutere la tua idea.',
      'cta.btn.quote':     'Richiedi un Preventivo',
      'cta.btn.work':      'Scopri i Nostri Lavori',
      'cta.btn.workalt':   'Guarda i Nostri Lavori',
      'cta.btn.services':  'I Nostri Servizi',
      'cta.btn.allservices': 'Scopri Tutti i Servizi',
      'cta.btn.allportfolio': 'Vedi tutto il Portfolio',

      'footer.nav.label':     'Navigazione',
      'footer.contact.label': 'Contatti',
      'footer.brand.desc':    'Specialisti in scenografie, allestimenti espositivi e installazioni scenotecniche per eventi culturali, produzioni televisive e brand activation.',
      'footer.copyright':     '&copy; 2026 Cultura è... S.r.l. — Tutti i diritti riservati &nbsp;|&nbsp; P.IVA e CF: 16732861006',
      'footer.addresses':     'Sede Legale: Via Georges Sorel 7 · 00177 Roma &nbsp;·&nbsp; Sede Operativa: Via di Affogalasino 50/52 · 00148 Roma',

      'contact.hours.label': 'Orari',
      'contact.hours.val':   'Lun – Ven: 9:00 – 18:00<br>Sab: 9:00 – 13:00<br>Dom: chiuso',

      'services.label':    'I Nostri Servizi',
      'services.title':    'Dove le idee prendono <span class="accent">forma</span>',
      'services.intro':    'Dalle prime bozze progettuali alla posa finale, gestiamo ogni fase con cura artigianale e precisione tecnica.',
      'services.s1.title': 'Supporto Progettuale',
      'services.s1.desc':  'Ti serve un\'idea su come allestire uno spazio espositivo, un locale o una scenografia? Ti aiutiamo dalla prima concept board fino al progetto esecutivo.',
      'services.s2.title': 'Realizzazione Scenografie',
      'services.s2.desc':  'Possiamo lavorare qualsiasi tipo di materiale con macchinari all\'avanguardia per seguire ogni tipo di esigenza, dai fondali televisivi alle installazioni site-specific.',
      'services.s3.title': 'Decorazione',
      'services.s3.desc':  'Seguiamo le tecniche scenografiche decorative per fondali e pavimenti, tutto in modo artigianale — affresco, effetti speciali, texture trompe-l\'œil e finiture customizzate.',
      'services.s4.title': 'Montaggio e Smontaggio',
      'services.s4.desc':  'Siamo attrezzati per installare le opere scenografiche — sia di nostra realizzazione che di terzi — in qualsiasi tipo di location, in tutta Italia.',

      'services.sector.title':          'Quando il racconto prende <span class="accent">la scena</span>',
      'services.sector.subtitle':       'Televisione, eventi culturali, moda, luxury. Ambiti diversi, un\'unica missione: scenografare lo spazio.',
      'services.sector.tv':             'Produzioni Televisive',
      'services.sector.tv.phrase':      'Scenografie protagoniste dello schermo',
      'services.sector.cultura':        'Esibizioni Culturali',
      'services.sector.cultura.phrase': 'Spazi che ispirano, esperienze che restano',
      'services.sector.lusso':          'Lusso',
      'services.sector.lusso.phrase':   'Ogni dettaglio racconta l\'eccellenza del brand',
      'services.sector.eventi':         'Parchi ed Eventi',
      'services.sector.eventi.phrase':  'Emozioni su misura, costruite per il pubblico',

      'portfolio.label': 'I Nostri Lavori',
      'portfolio.all':   'Tutti',

      'clients.label':        'I Nostri Clienti',
      'clients.title':        'I brand che ci hanno scelto',
      'clients.intro':        'Dal broadcast al luxury, dall\'entertainment all\'istituzionale: collaboriamo con i nomi più importanti del panorama nazionale e internazionale.',
      'clients.rai.sector':   'Televisione Pubblica',
      'clients.ansa.sector':  'Agenzia di Stampa',
      'clients.roma.sector':  'Istituzionale',
      'clients.zetema.sector':'Progetto Cultura',

      'contact.label':           'Contatti',
      'contact.title':           'Parliamo del<br>tuo <span class="accent">progetto</span>',
      'contact.text':            'Che si tratti di una scenografia televisiva, di un allestimento per un brand di lusso o di un\'installazione site-specific, siamo pronti ad ascoltarti e a trasformare la tua visione in realtà.',
      'contact.addr.label':      'Indirizzo',
      'contact.phone.label':     'Telefono',
      'contact.form.title':      'Richiedi un Preventivo',
      'contact.form.nome':       'Nome',
      'contact.form.cognome':    'Cognome',
      'contact.form.project':    'Descrivi il Progetto',
      'contact.form.submit':     'Invia Richiesta',
      'contact.form.ph.nome':    'Il tuo nome',
      'contact.form.ph.cognome': 'Il tuo cognome',
      'contact.form.ph.email':   'nome@azienda.it',
      'contact.form.ph.project': 'Tipo di evento, location, dimensioni approssimative, tempistiche...',
      'contact.form.privacy':    'Ho letto e accetto la <a href="privacy.html" target="_blank">Privacy Policy</a> e acconsento al trattamento dei miei dati personali ai sensi del GDPR.',
    },

    en: {
      'nav.about':    'Who We Are',
      'nav.services': 'Services',
      'nav.portfolio':'Portfolio',
      'nav.clients':  'Clients',
      'nav.contact':  'Contact Us',

      'hero.eyebrow': 'Set Design & Installations · Rome',
      'hero.h1':      'IMAGINE<br>A <span class="accent">GREAT</span><br>SHOW.',
      'hero.subtitle':'We make it happen.',
      'hero.cta1':    'Discover Our Work',
      'hero.cta2':    'Request a Quote',
      'hero.scroll':  'Scroll',
      'hero.tagline': '<span>Passion</span> &nbsp;·&nbsp; <span>Creativity</span> &nbsp;·&nbsp; <span>Professionalism</span>',

      'about.label':  'Who We Are',
      'about.p1':     'Cultura è is passion taking shape in space.',
      'about.p2':     'We specialise in the design and production of sets, exhibition installations, and scenotechnic structures for cultural events, television productions, film premieres, and brand communication projects. Every environment we create begins with an idea and becomes an experience — visual, emotional, real.',
      'about.p3':     'We operate as a full-service organisation: a creative and technical ecosystem able to answer any design challenge with the speed, precision, and care every project deserves. One location, a seasoned team, cutting-edge technology, and state-of-the-art machinery — everything needed to turn a vision into reality, without compromise.',
      'about.p4':     'Our team brings together architects, set designers, carpenters, riggers, draughtspeople, set builders, decorators, electricians, screen-printers, model-makers, and graphic designers. Different skills, one soul: artisanal excellence in the service of creativity.',
      'about.p5':     'Because every project is not just a job — it is a story worth telling in space.',
      'about.quote':  '"We immerse ourselves in our clients\' challenges as if they were our own — every detail, every material, every light tells a story."',
      'about.role':   'Founder & Creative Director · 40 years in the industry',
      'about.stat1':  'Years of Experience',
      'about.stat2':  'Completed Projects',
      'about.stat3':  'Brand Partners',
      'about.readmore': 'Discover More',

      'page.about.label': 'Who We Are',
      'page.about.h1':    'The Art of<br><span class="accent">Set Design</span>',
      'page.services.label': 'Our Services',
      'page.services.h1': 'Sets & Installations:<br><span class="accent">From Design to Delivery</span>',
      'page.portfolio.label': 'Our Work',
      'page.contact.label': 'Contact',
      'page.contact.h1':  'Request a Quote<br><span class="accent">Set Design Rome</span>',

      'breadcrumb.about':    'Who We Are',
      'breadcrumb.services': 'Services',
      'breadcrumb.contact':  'Contact',

      'values.label': 'Our Values',
      'values.title': 'What Sets Us <span class="accent">Apart</span>',
      'values.v1.title': 'Artisanal Excellence',
      'values.v1.desc':  'Every element is hand-built by our craftspeople using quality materials, in keeping with the finest Italian scenographic traditions.',
      'values.v2.title': 'Meeting Every Deadline',
      'values.v2.desc':  'In the world of events and television, time is everything. Every project is planned with precision to meet every deadline, without exception.',
      'values.v3.title': 'Collaborative Approach',
      'values.v3.desc':  'We work side by side with the client at every stage of the project — from the initial brief to the final handover, we are an extension of your creative team.',
      'values.v4.title': 'Boundless Creativity',
      'values.v4.desc':  'From intimate spaces to large-scale national installations, there are no limits to our ability to imagine and build extraordinary environments.',
      'values.v5.title': 'Full Service',
      'values.v5.desc':  'From design to installation, from decoration to dismantling: we manage the entire process in-house, guaranteeing consistency and quality at every step.',
      'values.v6.title': 'Rooted in Rome',
      'values.v6.desc':  'Based in Rome, we operate across Italy, bringing with us the artisanal excellence of the capital and its centuries-old scenographic tradition.',

      'process.label': 'How We Work',
      'process.title': 'Our <span class="accent">Process</span>',
      'process.intro': 'Four proven phases to turn every idea into a real scenographic experience.',
      'process.s1.title': 'Briefing & Analysis',
      'process.s1.desc':  'We listen to your needs, analyse the space, and define objectives, budget, and timeline together for a shared project vision.',
      'process.s2.title': 'Concept & Design',
      'process.s2.desc':  'The creative team develops visual concepts, mood boards, and 3D renders that translate the vision into an approvable executive project.',
      'process.s3.title': 'Production',
      'process.s3.desc':  'Our craftspeople and riggers transform the project into real scenic elements, working every material with absolute care and precision.',
      'process.s4.title': 'Installation & Handover',
      'process.s4.desc':  'We install every element on location, respecting deadlines and the highest quality standards. At the end: swift dismantling and full site clean-up.',

      'cta.home.h2':       'Ready to <span class="accent">Collaborate</span>?',
      'cta.home.p':        'Tell us about your project — from concept to installation, we are by your side.',
      'cta.about.h2':      'Tell Us About Your <span class="accent">Project</span>',
      'cta.about.p':       'We are ready to listen and turn your vision into a scenographic reality.',
      'cta.services.h2':   'Start Your <span class="accent">Project</span>',
      'cta.services.p':    'Contact us for a free quote — we respond within 48 hours.',
      'cta.portfolio.h2':  'Is Your <span class="accent">Project</span> Next?',
      'cta.portfolio.p':   'Contact us to discuss your idea.',
      'cta.btn.quote':     'Request a Quote',
      'cta.btn.work':      'Discover Our Work',
      'cta.btn.workalt':   'View Our Work',
      'cta.btn.services':  'Our Services',
      'cta.btn.allservices': 'Discover All Services',
      'cta.btn.allportfolio': 'View Full Portfolio',

      'footer.nav.label':     'Navigation',
      'footer.contact.label': 'Contact',
      'footer.brand.desc':    'Specialists in set design, exhibition installations, and scenotechnic structures for cultural events, television productions, and brand activation.',
      'footer.copyright':     '&copy; 2026 Cultura è... S.r.l. — All rights reserved &nbsp;|&nbsp; VAT: 16732861006',
      'footer.addresses':     'Registered office: Via Georges Sorel 7 · 00177 Rome &nbsp;·&nbsp; Operational office: Via di Affogalasino 50/52 · 00148 Rome',

      'contact.hours.label': 'Hours',
      'contact.hours.val':   'Mon – Fri: 9:00 – 18:00<br>Sat: 9:00 – 13:00<br>Sun: closed',

      'services.label':    'Our Services',
      'services.title':    'Where ideas take <span class="accent">shape</span>',
      'services.intro':    'From the first concept sketches to the final installation, we manage every phase with artisanal care and technical precision.',
      'services.s1.title': 'Design Support',
      'services.s1.desc':  'Need help setting up an exhibition space, a venue, or a set? We guide you from the first concept board all the way to the executive project.',
      'services.s2.title': 'Set Construction',
      'services.s2.desc':  'We work with any type of material using state-of-the-art machinery — from television backdrops to site-specific installations.',
      'services.s3.title': 'Decoration',
      'services.s3.desc':  'We apply scenic decorative techniques to backdrops and floors, entirely by hand — fresco painting, special effects, trompe-l\'œil textures, and custom finishes.',
      'services.s4.title': 'Installation & Dismantling',
      'services.s4.desc':  'We are fully equipped to install scenic works — our own or third-party — in any type of location across Italy.',

      'services.sector.title':          'When the story takes <span class="accent">the stage</span>',
      'services.sector.subtitle':       'Television, cultural events, fashion, luxury. Different worlds, one mission: we scenograph the space.',
      'services.sector.tv':             'Television Productions',
      'services.sector.tv.phrase':      'Set designs that become the stars of the screen',
      'services.sector.cultura':        'Cultural Exhibitions',
      'services.sector.cultura.phrase': 'Spaces that inspire, experiences that last',
      'services.sector.lusso':          'Luxury',
      'services.sector.lusso.phrase':   'Every detail tells the story of excellence',
      'services.sector.eventi':         'Parks & Events',
      'services.sector.eventi.phrase':  'Tailor-made emotions, crafted for the audience',

      'portfolio.label': 'Our Work',
      'portfolio.all':   'All',

      'clients.label':        'Our Clients',
      'clients.title':        'The brands that chose us',
      'clients.intro':        'From broadcast to luxury, from entertainment to institutional: we work alongside the most prestigious names in the national and international landscape.',
      'clients.rai.sector':   'Public Television',
      'clients.ansa.sector':  'News Agency',
      'clients.roma.sector':  'Institutional',
      'clients.zetema.sector':'Cultural Project',

      'contact.label':           'Contact',
      'contact.title':           'Let\'s talk about<br>your <span class="accent">project</span>',
      'contact.text':            'Whether it\'s a television set, a luxury brand installation, or a site-specific piece, we\'re ready to listen and turn your vision into reality.',
      'contact.addr.label':      'Address',
      'contact.phone.label':     'Phone',
      'contact.form.title':      'Request a Quote',
      'contact.form.nome':       'First Name',
      'contact.form.cognome':    'Last Name',
      'contact.form.project':    'Describe Your Project',
      'contact.form.submit':     'Send Request',
      'contact.form.ph.nome':    'Your first name',
      'contact.form.ph.cognome': 'Your last name',
      'contact.form.ph.email':   'name@company.com',
      'contact.form.ph.project': 'Event type, location, approximate dimensions, timeline...',
      'contact.form.privacy':    'I have read and accept the <a href="privacy.html" target="_blank">Privacy Policy</a> and consent to the processing of my personal data under GDPR.',
    }
  };

  function applyLang(lang) {
    var dict = T[lang];
    if (!dict) return;

    /* textContent */
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) el.textContent = dict[key];
    });

    /* innerHTML (for elements with <br>, <span>, etc.) */
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-html');
      if (dict[key] !== undefined) el.innerHTML = dict[key];
    });

    /* placeholder */
    document.querySelectorAll('[data-i18n-ph]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-ph');
      if (dict[key] !== undefined) el.placeholder = dict[key];
    });

    document.documentElement.lang = lang;
    localStorage.setItem('ce-lang', lang);

    document.querySelectorAll('.lang-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });
  }

  /* ── Language switcher ── */
  document.querySelectorAll('.lang-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      applyLang(btn.getAttribute('data-lang'));
    });
  });

  /* restore saved language */
  var saved = localStorage.getItem('ce-lang');
  if (saved && saved !== 'it') applyLang(saved);

  /* ── Hamburger menu ── */
  var navbar = document.getElementById('navbar');
  var hamburger = document.getElementById('navHamburger');
  if (hamburger && navbar) {
    hamburger.addEventListener('click', function () {
      navbar.classList.toggle('nav-open');
    });
  }
  /* Close nav when any link inside it is clicked */
  document.querySelectorAll('nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (navbar) navbar.classList.remove('nav-open');
    });
  });

  /* ── Navbar scroll ── */
  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 40);
    });
  }

  /* ── Active nav highlight (page-based for multi-page site) ── */
  (function () {
    var path = window.location.pathname;
    var page = path.split('/').pop() || 'index.html';
    document.querySelectorAll('nav ul li a:not(.nav-cta)').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href) return;
      var hrefPage = href.split('#')[0];
      if (hrefPage && hrefPage === page && page !== 'index.html' && page !== '') {
        a.style.color = 'var(--near-black)';
      }
    });
  })();

  /* ── Active nav highlight — IntersectionObserver (only where nav uses anchor links) ── */
  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('nav ul li a:not(.nav-cta)');
  if (sections.length > 0) {
    var hasAnchorNavLinks = Array.from(navLinks).some(function (a) {
      var href = a.getAttribute('href');
      return href && href.indexOf('#') === 0;
    });
    if (hasAnchorNavLinks) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var id = '#' + entry.target.id;
            navLinks.forEach(function (a) {
              a.style.color = a.getAttribute('href') === id ? 'var(--near-black)' : '';
            });
          }
        });
      }, { rootMargin: '-40% 0px -40% 0px' });
      sections.forEach(function (s) { io.observe(s); });
    }
  }

  /* ── Portfolio filter & Lightbox (only on pages with a portfolio grid) ── */
  if (document.getElementById('portfolioGrid')) {
    var filterBtns = document.querySelectorAll('.filter-btn');
    var items = Array.from(document.querySelectorAll('.portfolio-item'));

    if (filterBtns.length > 0) {
      filterBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          filterBtns.forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          var filter = btn.getAttribute('data-filter');
          document.querySelectorAll('.portfolio-item').forEach(function (item) {
            item.classList.toggle('hidden', filter !== 'all' && item.getAttribute('data-year') !== filter);
          });
        });
      });
    }

    /* ── Lightbox (per-project gallery) ── */
    var lightbox  = document.getElementById('lightbox');
    if (lightbox) {
      var lbImg     = document.getElementById('lbImg');
      var lbName    = document.getElementById('lbName');
      var lbYear    = document.getElementById('lbYear');
      var lbCounter = document.getElementById('lbCounter');
      var lbImages  = [];
      var lbIdx     = 0;

      function showLbImage() {
        lbImg.src = lbImages[lbIdx];
        lbImg.alt = lbName.textContent;
        lbCounter.textContent = (lbIdx + 1) + ' / ' + lbImages.length;
        document.getElementById('lbPrev').style.display = lbImages.length > 1 ? '' : 'none';
        document.getElementById('lbNext').style.display = lbImages.length > 1 ? '' : 'none';
      }

      function openProject(item) {
        lbImages = JSON.parse(item.getAttribute('data-images'));
        lbIdx = 0;
        lbName.textContent = item.getAttribute('data-name');
        lbYear.textContent = item.getAttribute('data-year');
        showLbImage();
        lightbox.classList.add('open');
        document.body.style.overflow = 'hidden';
      }

      function closeLb() {
        lightbox.classList.remove('open');
        document.body.style.overflow = '';
      }

      function navLb(dir) {
        lbIdx = (lbIdx + dir + lbImages.length) % lbImages.length;
        showLbImage();
      }

      /* Event delegation — works even when items are loaded async via fetch */
      document.getElementById('portfolioGrid').addEventListener('click', function (e) {
        var item = e.target.closest('.portfolio-item');
        if (item) openProject(item);
      });

      document.getElementById('lbClose').addEventListener('click', closeLb);
      document.getElementById('lbPrev').addEventListener('click', function () { navLb(-1); });
      document.getElementById('lbNext').addEventListener('click', function () { navLb(1); });
      lightbox.addEventListener('click', function (e) { if (e.target === lightbox) closeLb(); });
      document.addEventListener('keydown', function (e) {
        if (!lightbox.classList.contains('open')) return;
        if (e.key === 'Escape')     closeLb();
        if (e.key === 'ArrowLeft')  navLb(-1);
        if (e.key === 'ArrowRight') navLb(1);
      });

      /* Touch swipe for lightbox */
      var lbTouchX = null;
      lightbox.addEventListener('touchstart', function (e) {
        lbTouchX = e.touches[0].clientX;
      }, { passive: true });
      lightbox.addEventListener('touchend', function (e) {
        if (lbTouchX === null) return;
        var dx = e.changedTouches[0].clientX - lbTouchX;
        if (Math.abs(dx) > 40) navLb(dx < 0 ? 1 : -1);
        lbTouchX = null;
      }, { passive: true });
    }
  }

  /* ── Sector card touch interaction (mobile) ── */
  if (window.matchMedia('(hover: none)').matches) {
    var sectorCards = Array.from(document.querySelectorAll('.sector-card'));
    sectorCards.forEach(function (card) {
      card.addEventListener('click', function () {
        var already = card.classList.contains('is-active');
        sectorCards.forEach(function (c) { c.classList.remove('is-active'); });
        if (!already) card.classList.add('is-active');
      });
    });
  }

  /* ── Hero carousel (only on pages with hero slides) ── */
  if (document.querySelectorAll('.hero-slide').length > 0) {
    var heroSlides = Array.from(document.querySelectorAll('.hero-slide'));
    var heroIdx = 0;
    if (heroSlides.length > 1) {
      setInterval(function () {
        heroSlides[heroIdx].classList.remove('active');
        heroIdx = (heroIdx + 1) % heroSlides.length;
        heroSlides[heroIdx].classList.add('active');
      }, 5000);
    }
  }

}());
