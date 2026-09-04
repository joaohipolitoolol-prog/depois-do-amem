'use strict';
(function () {
  const PIXEL_ID = '1793880684979642';

  if (!window.fbq) {
    const fbq = function () {
      if (fbq.callMethod) fbq.callMethod.apply(fbq, arguments);
      else fbq.queue.push(arguments);
    };
    window.fbq = fbq;
    window._fbq = fbq;
    fbq.push = fbq;
    fbq.loaded = true;
    fbq.version = '2.0';
    fbq.queue = [];
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://connect.facebook.net/en_US/fbevents.js';
    document.head.appendChild(script);
  }

  window.fbq('init', PIXEL_ID);
  window.fbq('track', 'PageView');

  window.AMEM_TRACK = Object.freeze({
    pixelId: PIXEL_ID,
    initiateCheckout() {
      if (typeof window.fbq !== 'function') return;
      window.fbq('track', 'InitiateCheckout', {
        value: 27,
        currency: 'BRL',
        content_name: '7 Dias Depois do Amém'
      });
    }
  });
})();
