export function detectActiveSection(pathname: string): 'services' | 'resources' | 'about' | null {
  if (pathname.startsWith('/services')) return 'services';
  if (
    pathname.startsWith('/resources/about') ||
    pathname.startsWith('/resources/in-the-media') ||
    pathname.startsWith('/resources/code-of-ethics') ||
    pathname.startsWith('/resources/community-involvement') ||
    pathname.startsWith('/resources/our-guarantees') ||
    pathname.startsWith('/resources/club-membership')
  ) {
    return 'about';
  }
  if (pathname.startsWith('/resources')) return 'resources';
  return null;
}

export function applyActiveNav(pathname: string, root: ParentNode = document) {
  const servicesBtn = root.querySelector('#servicesNavBtn');
  const resourcesBtn = root.querySelector('#resourcesNavBtn');
  const aboutBtn = root.querySelector('#aboutNavBtn');

  [servicesBtn, resourcesBtn, aboutBtn].forEach((btn) => {
    btn?.classList.remove('bfp-nav-btn-active');
  });

  const active = detectActiveSection(pathname);
  if (active === 'services') servicesBtn?.classList.add('bfp-nav-btn-active');
  if (active === 'resources') resourcesBtn?.classList.add('bfp-nav-btn-active');
  if (active === 'about') aboutBtn?.classList.add('bfp-nav-btn-active');
}
