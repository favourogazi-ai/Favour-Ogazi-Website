/* Favour Ogazi — small, calm behaviour: menu, filters, copy email, contact form */
(function () {
  // Pages open at the top, or at the linked section
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  if (!location.hash) window.scrollTo(0, 0);

  // Mobile menu
  var nav = document.querySelector('.nav');
  var btn = document.querySelector('.menu-btn');
  function setMenu(open) {
    if (!nav || !btn) return;
    nav.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? 'Close' : 'Menu';
  }
  if (btn) {
    btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    document.addEventListener('click', function (e) { if (nav.classList.contains('open') && !nav.contains(e.target)) setMenu(false); });
    nav.querySelectorAll('.nav-links a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  }

  // Filters (work, writing)
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var target = document.querySelector(group.getAttribute('data-filter-group'));
    var buttons = group.querySelectorAll('button');
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        buttons.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        var f = b.getAttribute('data-f');
        target.querySelectorAll('[data-c]').forEach(function (item) {
          item.hidden = !(f === 'all' || (' ' + item.getAttribute('data-c') + ' ').indexOf(' ' + f + ' ') > -1);
        });
      });
    });
  });

  // Copy email
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy'), label = b.textContent;
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () {
        b.textContent = 'Copied'; setTimeout(function () { b.textContent = label; }, 1600);
      }, function () {});
    });
  });

  // Contact form: opens an email draft until the form is connected to a database
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
