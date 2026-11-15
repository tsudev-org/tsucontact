// Nút "Chép" của khối Cài bằng lệnh. Tệp tĩnh cùng nguồn (CSP script-src 'self'). Không có Clipboard API
// (http, trình duyệt cũ) thì nút giữ ẩn - người dùng vẫn bôi đen chép tay được.
(function () {
  'use strict';
  if (!navigator.clipboard || !window.isSecureContext) return;
  var trangThai = document.getElementById('chep-trang-thai');
  document.querySelectorAll('button[data-chep]').forEach(function (nut) {
    var nguon = document.getElementById(nut.getAttribute('data-chep'));
    if (!nguon) return;
    nut.hidden = false;
    var nhan = nut.firstChild;
    nut.addEventListener('click', function () {
      navigator.clipboard.writeText(nguon.textContent || '').then(function () {
        nhan.nodeValue = 'Đã chép';
        if (trangThai) trangThai.textContent = 'Đã chép lệnh vào bộ nhớ tạm';
        setTimeout(function () { nhan.nodeValue = 'Chép'; }, 2000);
      }, function () {
        if (trangThai) trangThai.textContent = 'Không chép được, hãy bôi đen lệnh rồi chép tay';
      });
    });
  });
})();
