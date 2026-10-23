/* Favour Ogazi — site behaviour: nav, scrollytelling stages, reveals, filters */
(function () {
  var doc = document.documentElement;
  doc.classList.add('js');

  // Photo slots: show the image only once it loads
  document.querySelectorAll('.photo img').forEach(function (img) {
    function ok() { img.parentElement.classList.add('has-img'); }
    function bad() { img.remove(); }
    if (img.complete && img.naturalWidth) ok(); else { img.addEventListener('load', ok); img.addEventListener('error', bad); }
  });

  // Mobile menu
  var nav = document.querySelector('.nav');
  var btn = document.querySelector('.menu-btn');
  if (btn) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? 'Close' : 'Menu';
  });

  // Split words for reveal text
  var wordGroups = [];
  document.querySelectorAll('[data-words]').forEach(function (el) {
    var html = el.innerHTML.trim();
    // keep <em> wrappers: split on spaces outside tags
    var parts = html.split(/(\s+)/);
    el.innerHTML = parts.map(function (p) { return /^\s+$/.test(p) ? p : '<span class="w">' + p + '</span>'; }).join('');
    wordGroups.push({ el: el, section: el.closest('.scrolly'), words: el.querySelectorAll('.w') });
  });

  var progressBar = document.querySelector('.progress');
  var darkSections = Array.prototype.slice.call(document.querySelectorAll('.dark'));
  var sidesWrap = document.querySelector('.sides-wrap');
  var reelSection = document.querySelector('.reel-section');
  var reel = document.querySelector('.reel');
  var prSection = document.querySelector('.pr-section');
  var tl = document.querySelectorAll('[data-steps]');

  function prog(el) {
    var r = el.getBoundingClientRect();
    var span = r.height - innerHeight;
    if (span <= 0) return r.top < 0 ? 1 : 0;
    return Math.min(1, Math.max(0, -r.top / span));
  }
  function setOn(list, idx) { Array.prototype.forEach.call(list, function (el, i) { el.classList.toggle('on', i === idx); }); }

  function update() {
    var y = scrollY;
    if (progressBar) progressBar.style.transform = 'scaleX(' + (y / Math.max(1, doc.scrollHeight - innerHeight)) + ')';

    // Nav: scrolled state and colour based on section under it
    if (nav) {
      nav.classList.toggle('scrolled', y > 24);
      var probe = (nav.offsetHeight || 72) / 2;
      var onDark = darkSections.some(function (s) { var r = s.getBoundingClientRect(); return r.top <= probe && r.bottom > probe; });
      nav.classList.toggle('on-dark', onDark);
    }

    wordGroups.forEach(function (g) {
      var p = g.section ? prog(g.section) : 1;
      var n = Math.round(Math.min(1, p * 1.3) * g.words.length);
      Array.prototype.forEach.call(g.words, function (w, i) { w.classList.toggle('on', i < Math.max(1, n)); });
    });

    if (sidesWrap) {
      var items = sidesWrap.querySelectorAll('.side-list li');
      var panels = sidesWrap.querySelectorAll('.side-panels > div');
      var steps = panels.length;
      var si = Math.min(steps - 1, Math.floor(prog(sidesWrap) * steps));
      sidesWrap.classList.toggle('merged', si === steps - 1 && steps > items.length);
      setOn(items, si < items.length ? si : -1);
      setOn(panels, si);
    }

    if (reelSection && reel) {
      if (innerWidth > 900) {
        var wrap = reel.parentElement;
        var max = reel.scrollWidth - wrap.clientWidth + parseFloat(getComputedStyle(wrap).paddingLeft || 0);
        reel.style.transform = 'translateX(' + (-Math.max(0, max) * prog(reelSection)) + 'px)';
      } else reel.style.transform = '';
    }

    if (prSection) {
      var prItems = prSection.querySelectorAll('.pr-items > div');
      var pi = Math.min(prItems.length - 1, Math.floor(prog(prSection) * prItems.length));
      setOn(prItems, pi);
      setOn(prSection.querySelectorAll('.dots i'), pi);
      var num = prSection.querySelector('.pr-num'); if (num) num.textContent = pi + 1;
    }
  }

  var ticking = false;
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(function () { update(); ticking = false; }); } }
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  update();

  // Reveal on scroll
  var rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else rv.forEach(function (el) { el.classList.add('in'); });

  // Scroll-spy for index lists and chapter navs
  document.querySelectorAll('[data-spy]').forEach(function (navEl) {
    var links = navEl.querySelectorAll('a[href^="#"]');
    var targets = Array.prototype.map.call(links, function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    function spy() {
      var idx = 0;
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top < innerHeight * 0.45) idx = i; });
      setOn(links, idx);
    }
    addEventListener('scroll', spy, { passive: true }); spy();
  });

  // Filters (writing, work)
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var target = document.querySelector(group.getAttribute('data-filter-group'));
    var btns = group.querySelectorAll('button');
    btns.forEach(function (b) {
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        var f = b.getAttribute('data-f');
        target.querySelectorAll('[data-c]').forEach(function (it) {
          it.hidden = !(f === 'all' || (' ' + it.getAttribute('data-c') + ' ').indexOf(' ' + f + ' ') > -1);
        });
      });
    });
  });

  // Copy email
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy');
      var done = function () { var o = b.textContent; b.textContent = 'Copied'; setTimeout(function () { b.textContent = o; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    });
  });

  // Contact form: opens an email draft (until the Supabase form is connected)
  var form = document.getElementById('contact-form');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form);
    var subject = 'Website enquiry: ' + (d.get('topic') || 'Hello');
    var body = 'Name: ' + d.get('name') + '\nEmail: ' + d.get('email') + '\nOrganisation: ' + (d.get('org') || '-') + '\n\n' + d.get('message');
    window.location.href = 'mailto:thefavourogazi@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    var note = document.getElementById('form-note');
    if (note) note.textContent = 'Your email app should open with your message. If it doesn’t, write to thefavourogazi@gmail.com.';
  });

  var yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
})();
