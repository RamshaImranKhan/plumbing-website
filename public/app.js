function initApp() {
  if (window.__appInit) return;
  window.__appInit = true;

  document.body.classList.add('is-loaded');
  const inits = [
    initMobileNav,
    initBfpNav,
    initMegaToggles,
    initForbesBar,
    initReviewCredits,
    initZipLookup,
    initScrollReveal,
    initSmoothHeader,
    initServiceFeaturePanel,
    initBrandCarousel,
    initAreasPanel,
    initServicesMegaScroll,
    initPrivacyConsentModal,
  ];
  inits.forEach((fn) => {
    try {
      fn();
    } catch (err) {
      console.error(`Init failed: ${fn.name}`, err);
    }
  });
}

window.initApp = initApp;

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}

function initForbesBar() {
  const bar = document.getElementById('forbesBar');
  const close = document.getElementById('forbesClose');
  if (!bar || !close) return;
  close.addEventListener('click', () => bar.classList.add('hidden'));
}

function initMegaToggles() {
  document.addEventListener('click', (e) => {
    const btn = e.target instanceof Element ? e.target.closest('.mega-toggle') : null;
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();
    const group = btn.closest('.mega-group');
    const sub = group?.querySelector('.mega-sub');
    if (!sub) return;

    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!expanded));
    btn.textContent = expanded ? '+' : '−';
    sub.classList.toggle('collapsed', expanded);

    window.requestAnimationFrame(() => {
      if (typeof window.updateServicesMegaScrollButtons === 'function') {
        window.updateServicesMegaScrollButtons();
      }
    });
  });
}

function initServicesMegaScroll() {
  const viewport = document.getElementById('servicesMegaScroll');
  const upBtn = document.getElementById('servicesScrollUp');
  const downBtn = document.getElementById('servicesScrollDown');
  const mega = document.getElementById('servicesMega');
  if (!viewport || !upBtn || !downBtn) return;

  const scrollStep = () => Math.max(120, Math.round(viewport.clientHeight * 0.65));

  const updateButtons = () => {
    const maxScroll = viewport.scrollHeight - viewport.clientHeight;
    const canScroll = maxScroll > 4;
    upBtn.disabled = !canScroll || viewport.scrollTop <= 4;
    downBtn.disabled = !canScroll || viewport.scrollTop >= maxScroll - 4;
  };

  upBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    viewport.scrollBy({ top: -scrollStep(), behavior: 'smooth' });
  });

  downBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    viewport.scrollBy({ top: scrollStep(), behavior: 'smooth' });
  });

  viewport.addEventListener('scroll', updateButtons, { passive: true });
  window.addEventListener('resize', updateButtons);

  if (mega) {
    const observer = new MutationObserver(() => {
      if (!mega.hidden) {
        window.requestAnimationFrame(updateButtons);
      }
    });
    observer.observe(mega, { attributes: true, attributeFilter: ['hidden'] });
  }

  window.updateServicesMegaScrollButtons = updateButtons;
  updateButtons();
}

function initBfpNav() {
  if (window.__bfpNavInit) return;
  window.__bfpNavInit = true;

  function getEls() {
    return {
      servicesBtn: document.getElementById('servicesNavBtn'),
      servicesMega: document.getElementById('servicesMega'),
      resourcesBtn: document.getElementById('resourcesNavBtn'),
      resourcesMega: document.getElementById('resourcesMega'),
      aboutBtn: document.getElementById('aboutNavBtn'),
      aboutMega: document.getElementById('aboutMega'),
      megaBackdrop: document.getElementById('megaBackdrop'),
    };
  }

  function closeAllMegaMenus() {
    const { servicesMega, resourcesMega, aboutMega, megaBackdrop, servicesBtn, resourcesBtn, aboutBtn } = getEls();
    if (servicesMega) servicesMega.hidden = true;
    if (resourcesMega) resourcesMega.hidden = true;
    if (aboutMega) aboutMega.hidden = true;
    if (megaBackdrop) {
      megaBackdrop.classList.remove('is-visible');
      window.setTimeout(() => {
        const { servicesMega: s, resourcesMega: r, aboutMega: a, megaBackdrop: b } = getEls();
        const anyOpen = (s && !s.hidden) || (r && !r.hidden) || (a && !a.hidden);
        if (!anyOpen && b) b.hidden = true;
      }, 260);
    }
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'false');
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'false');
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'false');
  }

  function showMegaBackdrop() {
    const { megaBackdrop } = getEls();
    if (!megaBackdrop) return;
    megaBackdrop.hidden = false;
    window.requestAnimationFrame(() => megaBackdrop.classList.add('is-visible'));
  }

  function openServicesMega() {
    const { servicesMega, resourcesMega, aboutMega, servicesBtn, resourcesBtn, aboutBtn } = getEls();
    if (resourcesMega) resourcesMega.hidden = true;
    if (aboutMega) aboutMega.hidden = true;
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'false');
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'false');
    if (servicesMega) servicesMega.hidden = false;
    showMegaBackdrop();
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'true');
    const servicesScroll = document.getElementById('servicesMegaScroll');
    if (servicesScroll) servicesScroll.scrollTop = 0;
    window.requestAnimationFrame(() => {
      if (typeof window.updateServicesMegaScrollButtons === 'function') {
        window.updateServicesMegaScrollButtons();
      }
    });
  }

  function openResourcesMega() {
    const { servicesMega, resourcesMega, aboutMega, servicesBtn, resourcesBtn, aboutBtn } = getEls();
    if (servicesMega) servicesMega.hidden = true;
    if (aboutMega) aboutMega.hidden = true;
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'false');
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'false');
    if (resourcesMega) resourcesMega.hidden = false;
    showMegaBackdrop();
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'true');
  }

  function openAboutMega() {
    const { servicesMega, resourcesMega, aboutMega, servicesBtn, resourcesBtn, aboutBtn } = getEls();
    if (servicesMega) servicesMega.hidden = true;
    if (resourcesMega) resourcesMega.hidden = true;
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'false');
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'false');
    if (aboutMega) aboutMega.hidden = false;
    showMegaBackdrop();
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'true');
  }

  function toggleMega(menu) {
    const { servicesMega, resourcesMega, aboutMega } = getEls();
    const openMap = {
      services: { el: servicesMega, open: openServicesMega },
      resources: { el: resourcesMega, open: openResourcesMega },
      about: { el: aboutMega, open: openAboutMega },
    };
    const target = openMap[menu];
    if (!target.el) return;
    if (!target.el.hidden) closeAllMegaMenus();
    else target.open();
  }

  document.addEventListener('click', (e) => {
    const target = e.target;
    if (!(target instanceof Element)) return;

    if (target.closest('#servicesNavBtn')) {
      e.preventDefault();
      e.stopPropagation();
      toggleMega('services');
      return;
    }
    if (target.closest('#resourcesNavBtn')) {
      e.preventDefault();
      e.stopPropagation();
      toggleMega('resources');
      return;
    }
    if (target.closest('#aboutNavBtn')) {
      e.preventDefault();
      e.stopPropagation();
      toggleMega('about');
      return;
    }
    if (target.closest('#megaBackdrop')) {
      closeAllMegaMenus();
      return;
    }
    if (target.closest('.services-mega, .resources-mega, .about-mega')) {
      if (target.closest('a')) closeAllMegaMenus();
      return;
    }
    closeAllMegaMenus();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAllMegaMenus();
  });
}

function initMobileNav() {
  const toggle = document.getElementById('navToggle');
  const nav = document.getElementById('navMobile');
  if (!toggle || !nav) return;

  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');

    if (open) {
      nav.hidden = false;
      window.requestAnimationFrame(() => nav.classList.add('is-open'));
      return;
    }

    nav.classList.remove('is-open');
    window.setTimeout(() => {
      if (!nav.classList.contains('is-open')) {
        nav.hidden = true;
      }
    }, 420);
  };

  toggle.addEventListener('click', () => {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setOpen(false));
  });
}

function initReviewCredits() {
  const credits = document.getElementById('reviewsCredits');
  const track = document.getElementById('reviewsCreditsTrack');
  let viewport = credits?.querySelector('.reviews-credits-viewport');
  if (!credits || !track || !viewport || credits.dataset.reviewsInit === 'true') return;

  if (!viewport.parentElement?.classList.contains('reviews-credits-body')) {
    const body = document.createElement('div');
    body.className = 'reviews-credits-body';

    const upBtn = document.createElement('button');
    upBtn.type = 'button';
    upBtn.className = 'reviews-scroll-btn reviews-scroll-up';
    upBtn.setAttribute('aria-label', 'Scroll reviews up');
    upBtn.innerHTML = '↑';

    const downBtn = document.createElement('button');
    downBtn.type = 'button';
    downBtn.className = 'reviews-scroll-btn reviews-scroll-down';
    downBtn.setAttribute('aria-label', 'Scroll reviews down');
    downBtn.innerHTML = '↓';

    viewport.parentNode?.insertBefore(body, viewport);
    body.append(upBtn, viewport, downBtn);

    const hint = document.createElement('p');
    hint.className = 'reviews-scroll-hint';
    hint.textContent = 'Reviews auto-scroll — scroll or use arrows to browse';
    body.after(hint);

    viewport.setAttribute('tabindex', '0');
    viewport.setAttribute('role', 'region');
    viewport.setAttribute('aria-label', 'Scrollable customer reviews');
  }

  viewport = credits.querySelector('.reviews-credits-viewport');
  const upBtn = credits.querySelector('.reviews-scroll-up');
  const downBtn = credits.querySelector('.reviews-scroll-down');
  if (!viewport) return;

  credits.dataset.reviewsInit = 'true';

  const buildCredit = (review) => {
    const article = document.createElement('article');
    article.className = 'review-credit';
    const stars = '★'.repeat(review.stars || 5);
    article.innerHTML = `
      <div class="review-credit-stars" aria-hidden="true">${stars}</div>
      <p>"${review.text}"</p>
      <footer>${review.author}</footer>
    `;
    return article;
  };

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const scrollSpeed = 48;
  let loopHeight = 0;
  let rafId = null;
  let lastTimestamp = 0;
  let pauseUntil = 0;
  let programmaticScroll = false;
  let isAutoAnimating = false;
  let isInView = true;

  const getScrollStep = () => {
    const card = track.querySelector('.review-credit');
    if (!card) return 180;
    const styles = window.getComputedStyle(track);
    const gap = parseFloat(styles.rowGap || styles.gap || '64') || 64;
    return card.getBoundingClientRect().height + gap;
  };

  const pauseAuto = (ms = 5000) => {
    pauseUntil = Date.now() + ms;
  };

  const prepareLoop = () => {
    const originals = [...track.querySelectorAll('.review-credit')];
    if (!originals.length) return;

    if (track.children.length === originals.length) {
      originals.forEach((entry) => track.appendChild(entry.cloneNode(true)));
    }

    loopHeight = track.scrollHeight / 2;
    if (viewport.scrollTop >= loopHeight) {
      programmaticScroll = true;
      viewport.scrollTop -= loopHeight;
      programmaticScroll = false;
    }
  };

  const normalizeScroll = () => {
    if (loopHeight <= 0) return;
    programmaticScroll = true;
    if (viewport.scrollTop >= loopHeight) viewport.scrollTop -= loopHeight;
    if (viewport.scrollTop < 0) viewport.scrollTop += loopHeight;
    programmaticScroll = false;
  };

  const tick = (timestamp) => {
    if (!lastTimestamp) lastTimestamp = timestamp;
    const delta = (timestamp - lastTimestamp) / 1000;
    lastTimestamp = timestamp;

    if (!reducedMotion && isInView && loopHeight > 0 && Date.now() > pauseUntil) {
      isAutoAnimating = true;
      programmaticScroll = true;
      viewport.scrollTop += scrollSpeed * delta;
      normalizeScroll();
      programmaticScroll = false;
    } else {
      isAutoAnimating = false;
    }

    rafId = requestAnimationFrame(tick);
  };

  const startCredits = () => {
    prepareLoop();

    window.addEventListener('resize', prepareLoop);

    if (rafId) cancelAnimationFrame(rafId);
    lastTimestamp = 0;
    rafId = requestAnimationFrame(tick);
  };

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        isInView = entries.some((entry) => entry.isIntersecting);
      },
      { threshold: 0.15 }
    );
    observer.observe(credits);
  }

  const scrollByStep = (direction) => {
    pauseAuto();
    viewport.classList.add('is-user-scrolling');
    viewport.scrollBy({ top: direction * getScrollStep(), behavior: reducedMotion ? 'auto' : 'smooth' });
    window.setTimeout(() => {
      normalizeScroll();
      viewport.classList.remove('is-user-scrolling');
    }, reducedMotion ? 0 : 420);
  };

  upBtn?.addEventListener('click', () => scrollByStep(-1));
  downBtn?.addEventListener('click', () => scrollByStep(1));

  viewport.addEventListener('scroll', () => {
    if (programmaticScroll || isAutoAnimating) return;
    pauseAuto();
    normalizeScroll();
  }, { passive: true });

  viewport.addEventListener('wheel', () => pauseAuto(), { passive: true });

  viewport.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      scrollByStep(-1);
    }
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      scrollByStep(1);
    }
  });

  let dragStartY = 0;
  let dragStartScroll = 0;
  let dragging = false;

  viewport.addEventListener('pointerdown', (e) => {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    dragging = true;
    dragStartY = e.clientY;
    dragStartScroll = viewport.scrollTop;
    pauseAuto();
    viewport.setPointerCapture(e.pointerId);
    viewport.classList.add('is-user-scrolling');
  });

  viewport.addEventListener('pointermove', (e) => {
    if (!dragging) return;
    programmaticScroll = true;
    viewport.scrollTop = dragStartScroll - (e.clientY - dragStartY);
    programmaticScroll = false;
  });

  const endDrag = () => {
    if (!dragging) return;
    dragging = false;
    viewport.classList.remove('is-user-scrolling');
    normalizeScroll();
    pauseAuto();
  };

  viewport.addEventListener('pointerup', endDrag);
  viewport.addEventListener('pointercancel', endDrag);

  fetch('/api/reviews')
    .then((response) => (response.ok ? response.json() : Promise.reject()))
    .then((reviews) => {
      track.innerHTML = '';
      reviews.forEach((review) => track.appendChild(buildCredit(review)));
      startCredits();
    })
    .catch(() =>
      fetch('/data/reviews.json')
        .then((response) => (response.ok ? response.json() : Promise.reject()))
        .then((reviews) => {
          track.innerHTML = '';
          reviews.forEach((review) => track.appendChild(buildCredit(review)));
          startCredits();
        })
        .catch(startCredits)
    );
}

function initQuoteForm() {
  const form = document.getElementById('quoteForm');
  const toastLayer = document.getElementById('toastLayer');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.fullName.value.trim();
    const phone = form.phone.value.trim();
    const email = form.email.value.trim();
    const address = form.address.value.trim();
    const message = form.message.value.trim();

    if (!name || !phone || !email || !address || !message) {
      showToast('Please fill in all required fields.', toastLayer);
      return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      showToast('Please enter a valid email address.', toastLayer);
      return;
    }

    showToast('Thank you! Your request has been submitted. We\'ll contact you shortly.', toastLayer, 'success');
    form.reset();
  });
}

function showToast(message, container, type = '') {
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast${type ? ` ${type}` : ''}`;
  toast.setAttribute('role', 'status');
  toast.textContent = message;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = '0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 5000);
}

function initZipLookup() {
  const form = document.getElementById('zipLookupForm');
  const zipInput = document.getElementById('serviceZip');
  const message = document.getElementById('zipMessage');
  const success = document.getElementById('zipSuccess');
  if (!form || !zipInput || !message) return;

  const omahaMetroPrefixes = ['680', '681', '683', '515', '684', '686'];

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const zip = zipInput.value.trim();

    if (!/^\d{5}$/.test(zip)) {
      message.textContent = 'Please enter a valid 5-digit zip code.';
      message.className = 'zip-message error';
      if (success) success.hidden = true;
      return;
    }

    const prefix = zip.substring(0, 3);
    if (omahaMetroPrefixes.includes(prefix)) {
      message.textContent = '';
      message.className = 'zip-message';
      if (success) success.hidden = false;
    } else {
      message.textContent = 'Unfortunately, we do not currently service your zip code. Call (402) 922-8334 to confirm.';
      message.className = 'zip-message error';
      if (success) success.hidden = true;
    }
  });
}

function initScrollReveal() {
  const targets = document.querySelectorAll(
    [
      '.service-card',
      '.trust-item',
      '.stat-card',
      '.offer-card',
      '.offer-coupon',
      '.reviews-credits',
      '.faq-item',
      '.about-text',
      '.about-stats',
      '.tip-card',
      '.membership-card-inner',
      '.local-stat',
      '.zip-lookup-card',
      '.why-choose-list',
      '.service-expand',
      '.services-col',
      '.blog-card',
      '.brand-card',
      '.areas-intro-copy',
      '.areas-intro-media',
      '.service-feature-wrap',
      '.service-hero-feature',
      '.page-feature-image',
      '.services-hero-image',
      '.sidebar-card',
      '.service-main > h2',
      '.authority-brands-header',
      '.expert-tips-home-header .section-label',
      '.expert-tips-home-header h2',
      '.expert-tips-home-header .expert-tips-home-lead',
      '.expert-tips-home-header .btn-view-all',
      '.faq-intro .section-label',
      '.faq-intro h2',
      '.faq-intro p',
      '.faq-intro .btn-outline',
    ].join(', ')
  );

  targets.forEach((el, index) => {
    el.classList.add('reveal');

    const tipsGrid = el.closest('.expert-tips-home .blog-posts-grid');
    if (tipsGrid) {
      const cards = [...tipsGrid.querySelectorAll('.blog-card')];
      const cardIndex = cards.indexOf(el);
      if (cardIndex >= 0) {
        el.style.setProperty('--reveal-delay', `${cardIndex * 90}ms`);
        return;
      }
    }

    const tipsHeader = el.closest('.expert-tips-home-header');
    if (tipsHeader) {
      const headerEls = [
        tipsHeader.querySelector('.section-label'),
        tipsHeader.querySelector('h2'),
        tipsHeader.querySelector('.expert-tips-home-lead'),
        tipsHeader.querySelector('.btn-view-all'),
      ].filter(Boolean);
      const headerIndex = headerEls.indexOf(el);
      if (headerIndex >= 0) {
        el.style.setProperty('--reveal-delay', `${headerIndex * 80}ms`);
        return;
      }
    }

    const faqList = el.closest('.faq-list');
    if (faqList) {
      const items = [...faqList.querySelectorAll('.faq-item')];
      const itemIndex = items.indexOf(el);
      if (itemIndex >= 0) {
        el.style.setProperty('--reveal-delay', `${itemIndex * 70}ms`);
        return;
      }
    }

    const faqIntro = el.closest('.faq-intro');
    if (faqIntro) {
      const introEls = [
        faqIntro.querySelector('.section-label'),
        faqIntro.querySelector('h2'),
        faqIntro.querySelector('p'),
        faqIntro.querySelector('.btn-outline'),
      ].filter(Boolean);
      const introIndex = introEls.indexOf(el);
      if (introIndex >= 0) {
        el.style.setProperty('--reveal-delay', `${introIndex * 80}ms`);
        return;
      }
    }

    el.style.setProperty('--reveal-delay', `${Math.min(index % 6, 5) * 60}ms`);
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -32px 0px' }
  );

  targets.forEach((el) => observer.observe(el));
}

function initSmoothHeader() {
  const header = document.querySelector('.bfp-header');
  if (!header) return;

  const onScroll = () => {
    header.classList.toggle('is-scrolled', window.scrollY > 80);
  };

  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

function initServiceFeaturePanel() {
  const panel = document.getElementById('plumbing-services-panel');
  const image = document.getElementById('serviceFeatureImage');
  const buttons = document.querySelectorAll('.service-feature-btn');
  if (!panel || !image || !buttons.length) return;

  function setActive(btn) {
    buttons.forEach((b) => b.classList.remove('is-active'));
    btn.classList.add('is-active');
    const src = btn.dataset.image;
    const alt = btn.dataset.alt;
    if (!src && !alt) return;

    image.classList.add('is-fading');
    window.setTimeout(() => {
      if (src) image.src = src;
      if (alt) image.alt = alt;
      image.classList.remove('is-fading');
    }, 180);
  }

  buttons.forEach((btn) => {
    btn.addEventListener('mouseenter', () => setActive(btn));
    btn.addEventListener('focus', () => setActive(btn));
  });

  buttons[0].classList.add('is-active');
}

function initBrandCarousel() {
  const section = document.querySelector('.authority-brands');
  const viewport = document.getElementById('brandViewport') || section?.querySelector('.authority-brands-viewport');
  const track = document.getElementById('brandTrack');
  const prev = document.getElementById('brandPrev');
  const next = document.getElementById('brandNext');
  if (!section || !viewport || !track) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const speed = 40;
  let offset = 0;
  let loopWidth = 0;
  let stepWidth = 0;
  let isDragging = false;
  let isHovering = false;
  let isInView = true;
  let dragStartX = 0;
  let dragStartOffset = 0;
  let rafId = null;
  let lastTime = null;
  let pauseUntil = 0;
  let controlsBound = track.dataset.controlsBound === 'true';

  const buildCard = (brand, index, eager = false) => {
    const card = document.createElement('a');
    card.className = 'brand-card';
    card.href = brand.href;

    if (brand.external) {
      card.target = '_blank';
      card.rel = 'noopener noreferrer';
    }

    const img = document.createElement('img');
    img.src = brand.logo.startsWith('/') ? brand.logo : `/${brand.logo}`;
    img.alt = brand.alt;
    img.width = 120;
    img.height = 80;
    img.decoding = 'async';
    img.loading = eager || index < 5 ? 'eager' : 'lazy';

    const label = document.createElement('span');
    label.textContent = brand.name;

    card.append(img, label);
    return card;
  };

  const buildSet = (brands, startIndex, eager = false) => {
    const set = document.createElement('div');
    set.className = 'authority-brands-set';

    brands.forEach((brand, index) => {
      set.appendChild(buildCard(brand, eager ? 0 : startIndex + index, eager));
    });

    return set;
  };

  const waitForImages = (container) => {
    const images = [...container.querySelectorAll('img')];
    return Promise.all(
      images.map(
        (img) =>
          new Promise((resolve) => {
            if (img.complete) {
              resolve();
              return;
            }
            img.addEventListener('load', resolve, { once: true });
            img.addEventListener('error', resolve, { once: true });
          })
      )
    );
  };

  const updateMetrics = () => {
    const firstSet = track.querySelector('.authority-brands-set');
    if (!firstSet) return;

    const gap = 20;
    section.style.setProperty('--brand-gap', `${gap}px`);

    const width = window.innerWidth;
    let visible = 1;
    if (width >= 1200) visible = 5;
    else if (width >= 768) visible = 3;
    else if (width >= 480) visible = 2;

    const cardWidth = (viewport.clientWidth - gap * (visible - 1)) / visible;
    section.style.setProperty('--brand-card-width', `${cardWidth}px`);

    loopWidth = firstSet.offsetWidth + gap;
    stepWidth = cardWidth + gap;
  };

  const applyOffset = () => {
    if (loopWidth > 0) {
      offset = ((offset % loopWidth) + loopWidth) % loopWidth;
    }
    track.style.transform = `translate3d(${-offset}px, 0, 0)`;
  };

  const pauseAuto = (ms = 1800) => {
    pauseUntil = Date.now() + ms;
  };

  const tick = (time) => {
    if (lastTime !== null && !reducedMotion && isInView && loopWidth > 0 && !isDragging && !isHovering && Date.now() > pauseUntil) {
      const delta = Math.min((time - lastTime) / 1000, 0.05);
      offset += speed * delta;
      applyOffset();
    }

    lastTime = time;
    rafId = window.requestAnimationFrame(tick);
  };

  const startMotion = () => {
    updateMetrics();
    applyOffset();
    if (!rafId) {
      lastTime = null;
      rafId = window.requestAnimationFrame(tick);
    }
  };

  const nudge = (direction) => {
    pauseAuto(2000);
    offset += direction * stepWidth;
    applyOffset();
  };

  const bindControls = () => {
    if (controlsBound) return;
    controlsBound = true;
    track.dataset.controlsBound = 'true';

    prev?.addEventListener('click', () => nudge(-1));
    next?.addEventListener('click', () => nudge(1));

    viewport.addEventListener('mouseenter', () => {
      isHovering = true;
    });
    viewport.addEventListener('mouseleave', () => {
      isHovering = false;
      lastTime = null;
    });

    viewport.addEventListener('pointerdown', (event) => {
      if (event.pointerType === 'mouse' && event.button !== 0) return;
      isDragging = true;
      dragStartX = event.clientX;
      dragStartOffset = offset;
      pauseAuto(2500);
      viewport.classList.add('is-dragging');
      viewport.setPointerCapture(event.pointerId);
    });

    viewport.addEventListener('pointermove', (event) => {
      if (!isDragging) return;
      offset = dragStartOffset - (event.clientX - dragStartX);
      applyOffset();
    });

    const finishDrag = () => {
      if (!isDragging) return;
      isDragging = false;
      viewport.classList.remove('is-dragging');
      pauseAuto(1500);
      lastTime = null;
    };

    viewport.addEventListener('pointerup', finishDrag);
    viewport.addEventListener('pointercancel', finishDrag);

    window.addEventListener('resize', () => {
      if (track.dataset.loaded === 'true') {
        updateMetrics();
        applyOffset();
      }
    });

    if ('IntersectionObserver' in window) {
      const viewObserver = new IntersectionObserver(
        (entries) => {
          isInView = entries.some((entry) => entry.isIntersecting);
          if (isInView) lastTime = null;
        },
        { threshold: 0.1 }
      );
      viewObserver.observe(section);
    }
  };

  const renderBrands = (brands) => {
    track.replaceChildren();

    const firstSet = buildSet(brands, 0);
    const secondSet = buildSet(brands, brands.length, true);
    secondSet.setAttribute('aria-hidden', 'true');

    track.append(firstSet, secondSet);

    Promise.all([waitForImages(firstSet), waitForImages(secondSet)]).then(() => {
      track.dataset.loaded = 'true';
      track.setAttribute('aria-busy', 'false');
      bindControls();
      startMotion();
    });
  };

  const loadBrands = () => {
    if (track.dataset.loaded === 'true') {
      bindControls();
      startMotion();
      return;
    }

    fetch('/api/brands')
      .then((response) => (response.ok ? response.json() : Promise.reject()))
      .then(renderBrands)
      .catch(() =>
        fetch('/data/brands.json')
          .then((response) => (response.ok ? response.json() : Promise.reject()))
          .then(renderBrands)
          .catch(() => {
            track.setAttribute('aria-busy', 'false');
          })
      );
  };

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        if (!entries.some((entry) => entry.isIntersecting)) return;
        observer.disconnect();
        loadBrands();
      },
      { rootMargin: '240px 0px' }
    );
    observer.observe(section);
    return;
  }

  loadBrands();
}

function initAreasPanel() {
  const list = document.getElementById('areasTownList');
  if (!list || list.children.length) return;

  const dataEl = document.getElementById('areasTownsData');
  let towns = null;

  if (dataEl) {
    try {
      towns = JSON.parse(dataEl.textContent);
    } catch (_) {
      towns = null;
    }
  }

  const render = (items) => {
    list.innerHTML = items
      .map((town) => `<li class="areas-town">${town}</li>`)
      .join('');
  };

  if (towns?.length) {
    render(towns);
    return;
  }

  fetch('areas-towns.json')
    .then((res) => res.json())
    .then(render)
    .catch(() => {
      list.innerHTML = '<li class="areas-town">Omaha</li><li class="areas-town">Bellevue</li><li class="areas-town">Papillion</li><li class="areas-town">Council Bluffs</li>';
    });
}

const PRIVACY_CONSENT_KEY = 'bfpPrivacyConsent';

function initPrivacyConsentModal() {
  const modal = document.getElementById('privacyModal');
  const functional = document.getElementById('functionalCookies');
  const rejectBtn = document.getElementById('privacyReject');
  const confirmBtn = document.getElementById('privacyConfirm');
  if (!modal) return;

  const openModal = () => {
    modal.hidden = false;
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('privacy-modal-open');
    window.requestAnimationFrame(() => modal.classList.add('is-visible'));
    modal.querySelector('.privacy-modal-close')?.focus();
  };

  const closeModal = () => {
    modal.classList.remove('is-visible');
    window.setTimeout(() => {
      modal.hidden = true;
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('privacy-modal-open');
    }, 300);
  };

  const saveConsent = (functionalEnabled) => {
    localStorage.setItem(
      PRIVACY_CONSENT_KEY,
      JSON.stringify({
        functional: functionalEnabled,
        doNotSell: !functionalEnabled,
        updated: new Date().toISOString(),
      })
    );
    closeModal();
  };

  const stored = localStorage.getItem(PRIVACY_CONSENT_KEY);
  if (stored && functional) {
    try {
      const prefs = JSON.parse(stored);
      functional.checked = Boolean(prefs.functional);
    } catch (_) {
      /* ignore invalid stored value */
    }
  }

  document.querySelectorAll('.js-privacy-choices').forEach((link) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      openModal();
    });
  });

  modal.querySelectorAll('[data-privacy-close]').forEach((el) => {
    el.addEventListener('click', closeModal);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.hidden) closeModal();
  });

  rejectBtn?.addEventListener('click', () => {
    if (functional) functional.checked = false;
    saveConsent(false);
  });

  confirmBtn?.addEventListener('click', () => {
    saveConsent(Boolean(functional?.checked));
  });

  document.querySelectorAll('.privacy-switch').forEach((label) => {
    label.addEventListener('click', (e) => e.stopPropagation());
  });

  const hash = window.location.hash.replace('#', '');
  if (hash === 'privacy-choices' || hash === 'your-privacy-choices') {
    openModal();
    history.replaceState(null, '', window.location.pathname + window.location.search);
  }
}

function initBookingModal() {
  if (window.__bookingModalInit) return;

  const omahaMetroPrefixes = ['680', '681', '683', '515', '684', '686'];
  const services = [
    'Emergency Plumbing',
    'Drain Cleaning',
    'Water Heater Repair',
    'Water Heater Installation',
    'Leak Detection',
    'Toilet Repair',
    'Faucet Repair',
    'Garbage Disposal',
    'Sewer Line Repair',
    'Plumbing Inspection',
    'Other / Not Sure',
  ];

  const modal = document.createElement('div');
  modal.className = 'booking-modal';
  modal.id = 'bookingModal';
  modal.hidden = true;
  modal.setAttribute('aria-hidden', 'true');
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.setAttribute('aria-labelledby', 'bookingModalTitle');

  modal.innerHTML = `
    <div class="booking-modal-backdrop" data-booking-close tabindex="-1"></div>
    <div class="booking-modal-panel" role="document">
      <div class="booking-modal-header">
        <img class="booking-modal-logo" src="/assets/logos/brands/benjamin-franklin.png" alt="Benjamin Franklin Plumbing" width="120" height="48">
        <div class="booking-modal-heading">
          <p class="booking-modal-location">Benjamin Franklin Plumbing – Omaha</p>
          <h2 id="bookingModalTitle">Book Online Now</h2>
        </div>
        <button type="button" class="booking-modal-close" data-booking-close aria-label="Close booking form">×</button>
      </div>

      <ol class="booking-steps" aria-label="Booking progress">
        <li class="booking-step is-active" data-step="1"><span class="booking-step-icon" aria-hidden="true">${stepIcon('location')}</span><span class="booking-step-label">Location</span></li>
        <li class="booking-step" data-step="2"><span class="booking-step-icon" aria-hidden="true">${stepIcon('service')}</span><span class="booking-step-label">Service</span></li>
        <li class="booking-step" data-step="3"><span class="booking-step-icon" aria-hidden="true">${stepIcon('schedule')}</span><span class="booking-step-label">Schedule</span></li>
        <li class="booking-step" data-step="4"><span class="booking-step-icon" aria-hidden="true">${stepIcon('contact')}</span><span class="booking-step-label">Contact</span></li>
        <li class="booking-step" data-step="5"><span class="booking-step-icon" aria-hidden="true">${stepIcon('additional')}</span><span class="booking-step-label">Additional</span></li>
      </ol>

      <form class="booking-form" id="bookingForm" novalidate>
        <div class="booking-pane is-active" data-pane="1">
          <div class="booking-illustration">
            <img src="/assets/images/bfp-van-orange.png" alt="" width="280" height="160" loading="lazy">
          </div>
          <h3 class="booking-pane-title">Where are you?</h3>
          <p class="booking-pane-desc">Enter your zip or postal code so we can check if we provide service in your area.</p>
          <div class="form-group">
            <label for="bookingZip">Zip Code <span class="req">*</span></label>
            <input type="text" id="bookingZip" name="zip" inputmode="numeric" maxlength="5" pattern="\\d{5}" required autocomplete="postal-code">
            <p class="booking-field-msg" id="bookingZipMsg" role="status"></p>
          </div>
        </div>

        <div class="booking-pane" data-pane="2" hidden>
          <h3 class="booking-pane-title">What service do you need?</h3>
          <p class="booking-pane-desc">Select the plumbing service that best matches your request.</p>
          <div class="form-group">
            <label for="bookingService">Service <span class="req">*</span></label>
            <select id="bookingService" name="service" required>
              <option value="">Choose a service…</option>
              ${services.map((s) => `<option value="${s}">${s}</option>`).join('')}
            </select>
          </div>
        </div>

        <div class="booking-pane" data-pane="3" hidden>
          <h3 class="booking-pane-title">When works for you?</h3>
          <p class="booking-pane-desc">Pick your preferred appointment date and time window.</p>
          <div class="form-row">
            <div class="form-group">
              <label for="bookingDate">Preferred Date <span class="req">*</span></label>
              <input type="date" id="bookingDate" name="date" required>
            </div>
            <div class="form-group">
              <label for="bookingTime">Preferred Time <span class="req">*</span></label>
              <select id="bookingTime" name="time" required>
                <option value="">Select a time…</option>
                <option value="morning">Morning (8am – 12pm)</option>
                <option value="afternoon">Afternoon (12pm – 4pm)</option>
                <option value="evening">Evening (4pm – 8pm)</option>
                <option value="asap">As Soon As Possible</option>
              </select>
            </div>
          </div>
        </div>

        <div class="booking-pane" data-pane="4" hidden>
          <h3 class="booking-pane-title">How can we reach you?</h3>
          <p class="booking-pane-desc">Tell us who to contact and where the service is needed.</p>
          <div class="form-row">
            <div class="form-group">
              <label for="bookingName">Full Name <span class="req">*</span></label>
              <input type="text" id="bookingName" name="name" required autocomplete="name">
            </div>
            <div class="form-group">
              <label for="bookingPhone">Phone <span class="req">*</span></label>
              <input type="tel" id="bookingPhone" name="phone" required autocomplete="tel">
            </div>
          </div>
          <div class="form-group">
            <label for="bookingEmail">Email <span class="req">*</span></label>
            <input type="email" id="bookingEmail" name="email" required autocomplete="email">
          </div>
          <div class="form-group">
            <label for="bookingAddress">Street Address <span class="req">*</span></label>
            <input type="text" id="bookingAddress" name="address" required autocomplete="street-address">
          </div>
        </div>

        <div class="booking-pane" data-pane="5" hidden>
          <h3 class="booking-pane-title">Anything else we should know?</h3>
          <p class="booking-pane-desc">Share details about your plumbing issue or special instructions.</p>
          <div class="form-group">
            <label for="bookingNotes">Additional Details</label>
            <textarea id="bookingNotes" name="notes" rows="4" placeholder="Describe your plumbing issue…"></textarea>
          </div>
          <label class="checkbox-label">
            <input type="checkbox" id="bookingConsent" name="consent">
            <span>I consent to receive marketing SMS from BFP. Msg &amp; data rates may apply.</span>
          </label>
        </div>

        <div class="booking-modal-footer">
          <a href="tel:4029228334" class="booking-emergency">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.01-.24 11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.56 1 1 0 01-.25 1.01l-2.2 2.22z"/></svg>
            Emergency
          </a>
          <div class="booking-footer-actions">
            <button type="button" class="btn btn-booking-back" id="bookingBack" hidden>Back</button>
            <button type="button" class="btn btn-booking-continue" id="bookingContinue" disabled>Continue</button>
            <button type="submit" class="btn btn-booking-submit" id="bookingSubmit" hidden>Submit Booking</button>
          </div>
        </div>
      </form>
    </div>
  `;

  document.body.appendChild(modal);
  window.__bookingModalInit = true;

  const form = modal.querySelector('#bookingForm');
  const panes = [...modal.querySelectorAll('.booking-pane')];
  const steps = [...modal.querySelectorAll('.booking-step')];
  const backBtn = modal.querySelector('#bookingBack');
  const continueBtn = modal.querySelector('#bookingContinue');
  const submitBtn = modal.querySelector('#bookingSubmit');
  const zipInput = modal.querySelector('#bookingZip');
  const zipMsg = modal.querySelector('#bookingZipMsg');
  const dateInput = modal.querySelector('#bookingDate');
  let currentStep = 1;

  const today = new Date().toISOString().split('T')[0];
  dateInput.min = today;

  const openModal = () => {
    modal.hidden = false;
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('booking-modal-open');
    window.requestAnimationFrame(() => modal.classList.add('is-visible'));
    goToStep(1);
    modal.querySelector('.booking-modal-close')?.focus();
  };

  const closeModal = () => {
    modal.classList.remove('is-visible');
    window.setTimeout(() => {
      modal.hidden = true;
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('booking-modal-open');
    }, 300);
  };

  const validateZip = () => {
    const zip = zipInput.value.trim();
    if (!/^\d{5}$/.test(zip)) {
      zipMsg.textContent = 'Please enter a valid 5-digit zip code.';
      zipMsg.className = 'booking-field-msg is-error';
      return false;
    }

    const prefix = zip.substring(0, 3);
    if (!omahaMetroPrefixes.includes(prefix)) {
      zipMsg.textContent = 'We may not service this area. Call (402) 922-8334 to confirm.';
      zipMsg.className = 'booking-field-msg is-error';
      return false;
    }

    zipMsg.textContent = 'Great — we service your area!';
    zipMsg.className = 'booking-field-msg is-success';
    return true;
  };

  const paneValid = (step) => {
    const pane = panes[step - 1];
    const fields = [...pane.querySelectorAll('input, select, textarea')].filter((el) => el.required);

    for (const field of fields) {
      if (field.type === 'email' && field.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value.trim())) {
        return false;
      }
      if (!field.checkValidity() || !field.value.trim()) return false;
    }

    if (step === 1) return validateZip();
    return true;
  };

  const updateContinueState = () => {
    const valid = paneValid(currentStep);
    continueBtn.disabled = !valid;
    submitBtn.disabled = !valid;
  };

  const goToStep = (step) => {
    currentStep = step;
    panes.forEach((pane, index) => {
      const active = index + 1 === step;
      pane.classList.toggle('is-active', active);
      pane.hidden = !active;
    });
    steps.forEach((el, index) => {
      el.classList.toggle('is-active', index + 1 === step);
      el.classList.toggle('is-complete', index + 1 < step);
    });

    backBtn.hidden = step === 1;
    continueBtn.hidden = step === 5;
    submitBtn.hidden = step !== 5;
    updateContinueState();

    const focusTarget = panes[step - 1].querySelector('input, select, textarea');
    if (focusTarget && modal.classList.contains('is-visible')) focusTarget.focus();
  };

  zipInput.addEventListener('input', () => {
    zipMsg.textContent = '';
    zipMsg.className = 'booking-field-msg';
    updateContinueState();
  });

  form.addEventListener('input', updateContinueState);
  form.addEventListener('change', updateContinueState);

  continueBtn.addEventListener('click', () => {
    if (!paneValid(currentStep)) return;
    goToStep(Math.min(currentStep + 1, 5));
  });

  backBtn.addEventListener('click', () => {
    goToStep(Math.max(currentStep - 1, 1));
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!paneValid(5)) return;

    const toastLayer = document.getElementById('toastLayer') || (() => {
      const layer = document.createElement('div');
      layer.className = 'toast-container';
      layer.id = 'toastLayer';
      layer.setAttribute('aria-live', 'polite');
      document.body.appendChild(layer);
      return layer;
    })();
    showToast('Thank you! Your booking request has been submitted. We\'ll contact you shortly.', toastLayer, 'success');
    form.reset();
    zipMsg.textContent = '';
    zipMsg.className = 'booking-field-msg';
    closeModal();
  });

  modal.querySelectorAll('[data-booking-close]').forEach((el) => {
    el.addEventListener('click', closeModal);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.hidden) closeModal();
  });

  const bookingTriggers =
    'a.btn-book, a.mobile-cta-book, a.btn-hero-book, [data-book-open], a[href*="#quote"], a[href*="#book"]';

  const handleBookingTrigger = (e) => {
    const trigger = e.target.closest(bookingTriggers);
    if (!trigger) return false;
    e.preventDefault();
    e.stopPropagation();
    openModal();
    return true;
  };

  document.addEventListener('click', (e) => {
    handleBookingTrigger(e);
  }, true);

  window.addEventListener('hashchange', () => {
    const hash = window.location.hash.replace('#', '');
    if (hash === 'quote' || hash === 'book') {
      openModal();
      history.replaceState(null, '', window.location.pathname + window.location.search);
    }
  });

  const hash = window.location.hash.replace('#', '');
  if (hash === 'quote' || hash === 'book') {
    openModal();
    history.replaceState(null, '', window.location.pathname + window.location.search);
  }
}

function stepIcon(type) {
  const icons = {
    location: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s7-4.5 7-11a7 7 0 10-14 0c0 6.5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    service: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>',
    schedule: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    contact: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    additional: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>',
  };
  return icons[type] || '';
}
