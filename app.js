document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('is-loaded');
  initMobileNav();
  initBfpNav();
  initMegaToggles();
  initForbesBar();
  initReviewCarousel();
  initQuoteForm();
  initZipLookup();
  initScrollReveal();
  initSmoothHeader();
  initServiceFeaturePanel();
  initBrandCarousel();
  initAreasPanel();
  initServicesMegaScroll();
  initPrivacyConsentModal();
});

function initForbesBar() {
  const bar = document.getElementById('forbesBar');
  const close = document.getElementById('forbesClose');
  if (!bar || !close) return;
  close.addEventListener('click', () => bar.classList.add('hidden'));
}

function initMegaToggles() {
  document.querySelectorAll('.mega-toggle').forEach((btn) => {
    btn.addEventListener('click', (e) => {
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
        updateServicesMegaScrollButtons();
      });
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
  const servicesBtn = document.getElementById('servicesNavBtn');
  const servicesMega = document.getElementById('servicesMega');
  const resourcesBtn = document.getElementById('resourcesNavBtn');
  const resourcesMega = document.getElementById('resourcesMega');
  const aboutBtn = document.getElementById('aboutNavBtn');
  const aboutMega = document.getElementById('aboutMega');
  const megaBackdrop = document.getElementById('megaBackdrop');
  const navBtns = document.querySelectorAll('.bfp-nav-btn[data-menu]');

  function closeAllMegaMenus() {
    if (servicesMega) servicesMega.hidden = true;
    if (resourcesMega) resourcesMega.hidden = true;
    if (aboutMega) aboutMega.hidden = true;
    if (megaBackdrop) {
      megaBackdrop.classList.remove('is-visible');
      window.setTimeout(() => {
        const anyOpen =
          (servicesMega && !servicesMega.hidden) ||
          (resourcesMega && !resourcesMega.hidden) ||
          (aboutMega && !aboutMega.hidden);
        if (!anyOpen) {
          megaBackdrop.hidden = true;
        }
      }, 260);
    }
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'false');
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'false');
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'false');
  }

  function showMegaBackdrop() {
    if (!megaBackdrop) return;
    megaBackdrop.hidden = false;
    window.requestAnimationFrame(() => {
      megaBackdrop.classList.add('is-visible');
    });
  }

  function openServicesMega() {
    document.querySelectorAll('.bfp-dropdown').forEach((d) => { d.hidden = true; });
    document.querySelectorAll('.bfp-nav-btn[data-menu]').forEach((b) => b.setAttribute('aria-expanded', 'false'));
    if (resourcesMega) resourcesMega.hidden = true;
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'false');
    if (aboutMega) aboutMega.hidden = true;
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
    document.querySelectorAll('.bfp-dropdown').forEach((d) => { d.hidden = true; });
    document.querySelectorAll('.bfp-nav-btn[data-menu]').forEach((b) => b.setAttribute('aria-expanded', 'false'));
    if (servicesMega) servicesMega.hidden = true;
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'false');
    if (aboutMega) aboutMega.hidden = true;
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'false');
    if (resourcesMega) resourcesMega.hidden = false;
    showMegaBackdrop();
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'true');
  }

  function openAboutMega() {
    document.querySelectorAll('.bfp-dropdown').forEach((d) => { d.hidden = true; });
    document.querySelectorAll('.bfp-nav-btn[data-menu]').forEach((b) => b.setAttribute('aria-expanded', 'false'));
    if (servicesMega) servicesMega.hidden = true;
    if (servicesBtn) servicesBtn.setAttribute('aria-expanded', 'false');
    if (resourcesMega) resourcesMega.hidden = true;
    if (resourcesBtn) resourcesBtn.setAttribute('aria-expanded', 'false');
    if (aboutMega) aboutMega.hidden = false;
    showMegaBackdrop();
    if (aboutBtn) aboutBtn.setAttribute('aria-expanded', 'true');
  }

  if (servicesBtn && servicesMega) {
    servicesBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = !servicesMega.hidden;
      if (isOpen) {
        closeAllMegaMenus();
      } else {
        openServicesMega();
      }
    });

    servicesMega.addEventListener('click', (e) => e.stopPropagation());

    servicesMega.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeAllMegaMenus);
    });
  }

  if (resourcesBtn && resourcesMega) {
    resourcesBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = !resourcesMega.hidden;
      if (isOpen) {
        closeAllMegaMenus();
      } else {
        openResourcesMega();
      }
    });

    resourcesMega.addEventListener('click', (e) => e.stopPropagation());

    resourcesMega.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeAllMegaMenus);
    });
  }

  if (aboutBtn && aboutMega) {
    aboutBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = !aboutMega.hidden;
      if (isOpen) {
        closeAllMegaMenus();
      } else {
        openAboutMega();
      }
    });

    aboutMega.addEventListener('click', (e) => e.stopPropagation());

    aboutMega.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeAllMegaMenus);
    });
  }

  if (megaBackdrop) {
    megaBackdrop.addEventListener('click', closeAllMegaMenus);
  }

  navBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      closeAllMegaMenus();
      const menuId = btn.getAttribute('data-menu');
      const menu = document.getElementById(menuId);
      if (!menu) return;

      const isOpen = !menu.hidden;
      document.querySelectorAll('.bfp-dropdown').forEach((d) => { d.hidden = true; });
      navBtns.forEach((b) => b.setAttribute('aria-expanded', 'false'));

      if (!isOpen) {
        menu.hidden = false;
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  document.addEventListener('click', () => {
    closeAllMegaMenus();
    document.querySelectorAll('.bfp-dropdown').forEach((d) => { d.hidden = true; });
    document.querySelectorAll('.bfp-nav-btn[data-menu]').forEach((b) => b.setAttribute('aria-expanded', 'false'));
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

function initReviewCarousel() {
  const track = document.getElementById('reviewsTrack');
  const prev = document.getElementById('reviewPrev');
  const next = document.getElementById('reviewNext');
  if (!track || !prev || !next) return;

  const scrollAmount = () => {
    const card = track.querySelector('.review-card');
    return card ? card.offsetWidth + 24 : 364;
  };

  prev.addEventListener('click', () => {
    track.scrollBy({ left: -scrollAmount(), behavior: 'smooth' });
  });

  next.addEventListener('click', () => {
    track.scrollBy({ left: scrollAmount(), behavior: 'smooth' });
  });
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
      '.review-card',
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
    ].join(', ')
  );

  targets.forEach((el, index) => {
    el.classList.add('reveal');
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
  const track = document.getElementById('brandTrack');
  const prev = document.getElementById('brandPrev');
  const next = document.getElementById('brandNext');
  if (!track || !prev || !next) return;

  const scrollAmount = 220;
  prev.addEventListener('click', () => {
    track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
  });
  next.addEventListener('click', () => {
    track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
  });
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
