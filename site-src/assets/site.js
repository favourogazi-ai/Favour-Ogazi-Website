/* Favour Ogazi — writing filters, copy email, footer year. Nothing moves. */
(function () {
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

  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy'), label = b.textContent;
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () {
        b.textContent = 'Copied'; setTimeout(function () { b.textContent = label; }, 1600);
      }, function () {});
    });
  });

  var yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
})();
