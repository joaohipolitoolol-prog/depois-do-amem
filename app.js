'use strict';
const checkoutDialog = document.getElementById('checkout-dialog');
document.getElementById('year').textContent = new Date().getFullYear();
document.querySelectorAll('.buy-button').forEach((button) => {
  button.addEventListener('click', () => {
    const configuredUrl = window.AMEM_CONFIG?.checkoutUrl;
    let destination;
    try {
      if (configuredUrl) {
        destination = new URL(configuredUrl);
        if (destination.protocol !== 'https:') destination = undefined;
      }
    } catch { destination = undefined; }
    if (!destination) {
      checkoutDialog.showModal();
      return;
    }
    const current = new URLSearchParams(window.location.search);
    const allowed = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'utm_id', 'src', 'sck', 'fbclid', 'gclid', 'ttclid'];
    allowed.forEach((key) => {
      if (current.has(key) && !destination.searchParams.has(key)) destination.searchParams.set(key, current.get(key));
    });
    window.location.assign(destination.href);
  });
});
document.querySelectorAll('.dialog-close, .dialog-back').forEach((button) => button.addEventListener('click', () => checkoutDialog.close()));
checkoutDialog.addEventListener('click', (event) => {
  if (event.target !== checkoutDialog) return;
  const bounds = checkoutDialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) checkoutDialog.close();
});
