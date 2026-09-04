'use strict';
const config = window.AMEM_CONFIG || {};
const phone = typeof config.whatsappNumber === 'string' ? config.whatsappNumber : '';
if (/^[1-9]\d{9,14}$/.test(phone)) {
  document.querySelectorAll('[data-whatsapp]').forEach((link) => {
    const message = `Olá! Acabei de comprar o material ${link.dataset.product} e preciso de ajuda com o acesso. Meu número de pedido é: `;
    link.href = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.closest('[data-support]').hidden = false;
  });
}
const upsellDialog = document.getElementById('upsell-dialog');
document.querySelector('[data-upsell]')?.addEventListener('click', () => {
  let target;
  try {
    if (config.upsellCheckoutUrl) {
      target = new URL(config.upsellCheckoutUrl);
      if (target.protocol !== 'https:') target = undefined;
    }
  } catch { target = undefined; }
  if (!target) { upsellDialog?.showModal(); return; }
  const current = new URLSearchParams(location.search);
  ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_id','src','sck','fbclid','gclid','ttclid'].forEach((key) => {
    if (current.has(key) && !target.searchParams.has(key)) target.searchParams.set(key,current.get(key));
  });
  location.assign(target.href);
});
upsellDialog?.querySelector('.dialog-close')?.addEventListener('click', () => upsellDialog.close());
