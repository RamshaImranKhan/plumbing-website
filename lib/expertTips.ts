export type ExpertTip = {
  slug: string;
  title: string;
  image: string;
  alt: string;
};

/** Catalog of expert tip cards available site-wide */
export const EXPERT_TIPS: Record<string, ExpertTip> = {
  'how-to-detect-water-leaks': {
    slug: 'how-to-detect-water-leaks',
    title: 'How to Detect Water Leaks in Your Home',
    image: '/assets/images/blog/leak_2.jpg',
    alt: 'How to Detect Water Leaks in Your Home',
  },
  'clogged-drain-causes-signs-solutions': {
    slug: 'clogged-drain-causes-signs-solutions',
    title: 'Clogged Drain Causes, Warning Signs & How to Fix Them',
    image: '/assets/images/blog/clogged-drain.jpg',
    alt: 'Clogged Drain Causes, Warning Signs and How to Fix Them',
  },
  'water-heater-buying-guide': {
    slug: 'water-heater-buying-guide',
    title: 'The Complete Water Heater Buying & Ownership Guide',
    image: '/assets/images/blog/bfp-water-heater.png',
    alt: 'The Complete Water Heater Buying and Ownership Guide',
  },
  'why-does-my-shower-drain-smell': {
    slug: 'why-does-my-shower-drain-smell',
    title: 'Why Does My Shower Drain Smell?',
    image: '/assets/images/blog/gettyimages-173933139.jpg',
    alt: 'Why Does My Shower Drain Smell?',
  },
  'common-household-plumbing-leaks': {
    slug: 'common-household-plumbing-leaks',
    title: '10 Common Causes of Household Plumbing Leaks',
    image: '/assets/images/blog/01-dont-let-a-small-leak-become-a-big-problem_.jpg',
    alt: '10 Common Causes of Household Plumbing Leaks',
  },
  'dishwasher-troubleshooting-guide': {
    slug: 'dishwasher-troubleshooting-guide',
    title: 'Dishwasher Not Draining, Leaking, or Filling?',
    image: '/assets/images/blog/dishwasher-not-draining.jpg',
    alt: 'Dishwasher Troubleshooting Guide',
  },
  'simple-fast-ways-to-get-rid-of-fruit-flies': {
    slug: 'simple-fast-ways-to-get-rid-of-fruit-flies',
    title: 'Simple & Fast Ways to Get Rid of Fruit Flies',
    image: '/assets/images/blog/getridoffruitflies_blogheader.jpg',
    alt: 'Simple and Fast Ways to Get Rid of Fruit Flies',
  },
  'common-garbage-disposal-problems': {
    slug: 'common-garbage-disposal-problems',
    title: 'Common Garbage Disposal Problems',
    image: '/assets/images/blog/clogged-drain.jpg',
    alt: 'Common Garbage Disposal Problems',
  },
  'keeping-your-garbage-disposal-clean-for-the-holidays': {
    slug: 'keeping-your-garbage-disposal-clean-for-the-holidays',
    title: 'Tips on Keeping Your Garbage Disposal Clean',
    image: '/assets/images/blog/clogged-drain.jpg',
    alt: 'Keeping Your Garbage Disposal Clean',
  },
  'signs-your-water-heater-needs-immediate-attention': {
    slug: 'signs-your-water-heater-needs-immediate-attention',
    title: '10 Signs Your Water Heater Needs Immediate Attention',
    image: '/assets/images/blog/bfp-water-heater.png',
    alt: 'Signs Your Water Heater Needs Immediate Attention',
  },
  'should-you-repair-or-replace-you-water-heater': {
    slug: 'should-you-repair-or-replace-you-water-heater',
    title: 'Should I Repair or Replace My Water Heater?',
    image: '/assets/images/blog/bfp-water-heater.png',
    alt: 'Should I Repair or Replace My Water Heater',
  },
  'can-i-finance-a-new-water-heater': {
    slug: 'can-i-finance-a-new-water-heater',
    title: 'Can I Finance a New Water Heater?',
    image: '/assets/images/blog/bfp-water-heater.png',
    alt: 'Can I Finance a New Water Heater',
  },
  'how-to-get-hair-out-of-your-drains': {
    slug: 'how-to-get-hair-out-of-your-drains',
    title: 'How to Get Hair Out of Your Drains',
    image: '/assets/images/blog/clogged-shower-drain.jpg',
    alt: 'How to Get Hair Out of Your Drains',
  },
  'common-signs-of-a-clogged-drain': {
    slug: 'common-signs-of-a-clogged-drain',
    title: 'Common Signs of a Clogged Drain',
    image: '/assets/images/blog/clogged-drain.jpg',
    alt: 'Common Signs of a Clogged Drain',
  },
  'causes-of-a-clogged-drain': {
    slug: 'causes-of-a-clogged-drain',
    title: 'Causes of a Clogged Drain',
    image: '/assets/images/blog/clogged-drain.jpg',
    alt: 'Causes of a Clogged Drain',
  },
  'drain-cleaner-vs-professional-plumber': {
    slug: 'drain-cleaner-vs-professional-plumber',
    title: 'Drain Cleaner vs. Hiring a Professional Plumber',
    image: '/assets/images/blog/03-call-us-for-expert-drain-unclogging-services.png',
    alt: 'Drain Cleaner vs Professional Plumber',
  },
  'early-warning-signs-of-hidden-plumbing-leaks': {
    slug: 'early-warning-signs-of-hidden-plumbing-leaks',
    title: 'Early Warning Signs of Hidden Plumbing Leaks',
    image: '/assets/images/blog/leak_2.jpg',
    alt: 'Early Warning Signs of Hidden Plumbing Leaks',
  },
  'a-fresh-start-with-modern-filtration-systems': {
    slug: 'a-fresh-start-with-modern-filtration-systems',
    title: "Revitalizing Your Home's Water with Filtration",
    image: '/assets/images/blog/istock-1500226860.jpg',
    alt: 'Modern Water Filtration Systems',
  },
  'water-filtration-emergency-preparedness': {
    slug: 'water-filtration-emergency-preparedness',
    title: 'Water Filtration in Emergency Preparedness',
    image: '/assets/images/blog/istock-1500226860.jpg',
    alt: 'Water Filtration Emergency Preparedness',
  },
  'tracing-your-drinking-waters-journey': {
    slug: 'tracing-your-drinking-waters-journey',
    title: "From Source to Tap: Your Drinking Water's Journey",
    image: '/assets/images/blog/istock-1500226860.jpg',
    alt: 'Tracing Your Drinking Water Journey',
  },
};

const DEFAULT_TIP_SLUGS = [
  'how-to-detect-water-leaks',
  'clogged-drain-causes-signs-solutions',
  'water-heater-buying-guide',
  'why-does-my-shower-drain-smell',
  'common-household-plumbing-leaks',
  'dishwasher-troubleshooting-guide',
] as const;

/** Per-service tip slugs (3–6 curated). Falls back to DEFAULT_TIP_SLUGS. */
const SERVICE_TIP_MAP: Record<string, string[]> = {
  drains: [
    'clogged-drain-causes-signs-solutions',
    'common-signs-of-a-clogged-drain',
    'causes-of-a-clogged-drain',
    'how-to-get-hair-out-of-your-drains',
    'drain-cleaner-vs-professional-plumber',
    'why-does-my-shower-drain-smell',
  ],
  'drain-cleaning': [
    'clogged-drain-causes-signs-solutions',
    'common-signs-of-a-clogged-drain',
    'causes-of-a-clogged-drain',
    'how-to-get-hair-out-of-your-drains',
    'drain-cleaner-vs-professional-plumber',
    'simple-fast-ways-to-get-rid-of-fruit-flies',
  ],
  'drain-installation': [
    'clogged-drain-causes-signs-solutions',
    'how-to-get-hair-out-of-your-drains',
    'common-signs-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
  ],
  hydrojetting: [
    'clogged-drain-causes-signs-solutions',
    'causes-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
    'common-signs-of-a-clogged-drain',
    'how-to-get-hair-out-of-your-drains',
    'common-household-plumbing-leaks',
  ],
  showers: [
    'why-does-my-shower-drain-smell',
    'how-to-get-hair-out-of-your-drains',
    'clogged-drain-causes-signs-solutions',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'common-signs-of-a-clogged-drain',
  ],
  'shower-repair': [
    'why-does-my-shower-drain-smell',
    'how-to-get-hair-out-of-your-drains',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'clogged-drain-causes-signs-solutions',
    'early-warning-signs-of-hidden-plumbing-leaks',
  ],
  'shower-installation': [
    'why-does-my-shower-drain-smell',
    'how-to-get-hair-out-of-your-drains',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'clogged-drain-causes-signs-solutions',
    'water-heater-buying-guide',
  ],
  bathtubs: [
    'why-does-my-shower-drain-smell',
    'how-to-get-hair-out-of-your-drains',
    'clogged-drain-causes-signs-solutions',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'common-signs-of-a-clogged-drain',
  ],
  sinks: [
    'dishwasher-troubleshooting-guide',
    'clogged-drain-causes-signs-solutions',
    'common-garbage-disposal-problems',
    'simple-fast-ways-to-get-rid-of-fruit-flies',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
  ],
  'sink-repair': [
    'dishwasher-troubleshooting-guide',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'clogged-drain-causes-signs-solutions',
    'common-garbage-disposal-problems',
    'early-warning-signs-of-hidden-plumbing-leaks',
  ],
  'sink-installation': [
    'dishwasher-troubleshooting-guide',
    'common-garbage-disposal-problems',
    'clogged-drain-causes-signs-solutions',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'keeping-your-garbage-disposal-clean-for-the-holidays',
  ],
  faucets: [
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'dishwasher-troubleshooting-guide',
    'clogged-drain-causes-signs-solutions',
    'tracing-your-drinking-waters-journey',
  ],
  toilets: [
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'clogged-drain-causes-signs-solutions',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-signs-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
  ],
  'toilet-repair': [
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'clogged-drain-causes-signs-solutions',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-signs-of-a-clogged-drain',
    'causes-of-a-clogged-drain',
  ],
  'toilet-installation': [
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'clogged-drain-causes-signs-solutions',
    'water-heater-buying-guide',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'tracing-your-drinking-waters-journey',
  ],
  'garbage-disposals': [
    'common-garbage-disposal-problems',
    'keeping-your-garbage-disposal-clean-for-the-holidays',
    'dishwasher-troubleshooting-guide',
    'clogged-drain-causes-signs-solutions',
    'simple-fast-ways-to-get-rid-of-fruit-flies',
    'causes-of-a-clogged-drain',
  ],
  'garbage-disposal-repair': [
    'common-garbage-disposal-problems',
    'keeping-your-garbage-disposal-clean-for-the-holidays',
    'dishwasher-troubleshooting-guide',
    'clogged-drain-causes-signs-solutions',
    'simple-fast-ways-to-get-rid-of-fruit-flies',
    'common-signs-of-a-clogged-drain',
  ],
  'garbage-disposal-installation': [
    'common-garbage-disposal-problems',
    'keeping-your-garbage-disposal-clean-for-the-holidays',
    'dishwasher-troubleshooting-guide',
    'clogged-drain-causes-signs-solutions',
    'simple-fast-ways-to-get-rid-of-fruit-flies',
    'how-to-detect-water-leaks',
  ],
  'water-heaters': [
    'water-heater-buying-guide',
    'signs-your-water-heater-needs-immediate-attention',
    'should-you-repair-or-replace-you-water-heater',
    'can-i-finance-a-new-water-heater',
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
  ],
  'water-heater-repair': [
    'signs-your-water-heater-needs-immediate-attention',
    'should-you-repair-or-replace-you-water-heater',
    'water-heater-buying-guide',
    'can-i-finance-a-new-water-heater',
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
  ],
  'water-heater-installation': [
    'water-heater-buying-guide',
    'can-i-finance-a-new-water-heater',
    'should-you-repair-or-replace-you-water-heater',
    'signs-your-water-heater-needs-immediate-attention',
    'how-to-detect-water-leaks',
    'tracing-your-drinking-waters-journey',
  ],
  'tankless-water-heaters': [
    'water-heater-buying-guide',
    'should-you-repair-or-replace-you-water-heater',
    'can-i-finance-a-new-water-heater',
    'signs-your-water-heater-needs-immediate-attention',
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
  ],
  'leak-detection': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-household-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'dishwasher-troubleshooting-guide',
    'signs-your-water-heater-needs-immediate-attention',
  ],
  'leak-repair': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-household-plumbing-leaks',
    'should-you-repair-or-replace-you-water-heater',
    'clogged-drain-causes-signs-solutions',
    'dishwasher-troubleshooting-guide',
  ],
  'leaking-pipes': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-household-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'signs-your-water-heater-needs-immediate-attention',
    'dishwasher-troubleshooting-guide',
  ],
  'slab-leaks': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-household-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'water-heater-buying-guide',
    'dishwasher-troubleshooting-guide',
  ],
  'pool-leak-detection': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-household-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'tracing-your-drinking-waters-journey',
    'a-fresh-start-with-modern-filtration-systems',
  ],
  'pipe-repair': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'water-heater-buying-guide',
    'signs-your-water-heater-needs-immediate-attention',
  ],
  'piping-repiping': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'water-heater-buying-guide',
    'clogged-drain-causes-signs-solutions',
    'tracing-your-drinking-waters-journey',
  ],
  'frozen-pipes': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'water-heater-buying-guide',
    'signs-your-water-heater-needs-immediate-attention',
  ],
  'water-lines': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'tracing-your-drinking-waters-journey',
    'a-fresh-start-with-modern-filtration-systems',
    'clogged-drain-causes-signs-solutions',
  ],
  sewers: [
    'clogged-drain-causes-signs-solutions',
    'causes-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
    'common-signs-of-a-clogged-drain',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
  ],
  'sewer-line-repair': [
    'clogged-drain-causes-signs-solutions',
    'causes-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
    'common-signs-of-a-clogged-drain',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
  ],
  'sewer-line-replacement': [
    'clogged-drain-causes-signs-solutions',
    'causes-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
  ],
  'trenchless-sewers': [
    'clogged-drain-causes-signs-solutions',
    'causes-of-a-clogged-drain',
    'drain-cleaner-vs-professional-plumber',
    'common-household-plumbing-leaks',
    'how-to-detect-water-leaks',
    'common-signs-of-a-clogged-drain',
  ],
  'water-treatment': [
    'a-fresh-start-with-modern-filtration-systems',
    'water-filtration-emergency-preparedness',
    'tracing-your-drinking-waters-journey',
    'how-to-detect-water-leaks',
    'water-heater-buying-guide',
    'common-household-plumbing-leaks',
  ],
  'brita-pro-filtration': [
    'a-fresh-start-with-modern-filtration-systems',
    'water-filtration-emergency-preparedness',
    'tracing-your-drinking-waters-journey',
    'how-to-detect-water-leaks',
    'water-heater-buying-guide',
    'dishwasher-troubleshooting-guide',
  ],
  'emergency-plumbing': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'signs-your-water-heater-needs-immediate-attention',
    'common-household-plumbing-leaks',
    'dishwasher-troubleshooting-guide',
  ],
  'plumbing-repairs': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'signs-your-water-heater-needs-immediate-attention',
    'dishwasher-troubleshooting-guide',
    'early-warning-signs-of-hidden-plumbing-leaks',
  ],
  'plumbing-installation': [
    'water-heater-buying-guide',
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'a-fresh-start-with-modern-filtration-systems',
    'clogged-drain-causes-signs-solutions',
    'can-i-finance-a-new-water-heater',
  ],
  'plumbing-inspection': [
    'how-to-detect-water-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'common-household-plumbing-leaks',
    'signs-your-water-heater-needs-immediate-attention',
    'clogged-drain-causes-signs-solutions',
    'common-signs-of-a-clogged-drain',
  ],
  'outdoor-plumbing': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'tracing-your-drinking-waters-journey',
    'water-filtration-emergency-preparedness',
  ],
  pumps: [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'water-heater-buying-guide',
    'dishwasher-troubleshooting-guide',
  ],
  'sump-pumps': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'water-filtration-emergency-preparedness',
    'tracing-your-drinking-waters-journey',
  ],
  'water-pumps': [
    'how-to-detect-water-leaks',
    'tracing-your-drinking-waters-journey',
    'a-fresh-start-with-modern-filtration-systems',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'water-heater-buying-guide',
  ],
  'pool-pump-plumbers': [
    'how-to-detect-water-leaks',
    'common-household-plumbing-leaks',
    'early-warning-signs-of-hidden-plumbing-leaks',
    'clogged-drain-causes-signs-solutions',
    'tracing-your-drinking-waters-journey',
    'a-fresh-start-with-modern-filtration-systems',
  ],
};

function tipCardHtml(tip: ExpertTip): string {
  return `
          <a href="/resources/expert-tips/${tip.slug}" class="blog-card">
            <img src="${tip.image}" alt="${tip.alt}" loading="lazy" width="350" height="296">
            <div class="blog-card-body">
              <h3>${tip.title}</h3>
              <span class="tip-read">Read Post →</span>
            </div>
          </a>`;
}

export function getTipsForService(serviceSlug: string): ExpertTip[] {
  const slugs = SERVICE_TIP_MAP[serviceSlug] ?? [...DEFAULT_TIP_SLUGS];
  const tips = slugs
    .map((slug) => EXPERT_TIPS[slug])
    .filter((tip): tip is ExpertTip => Boolean(tip));

  if (tips.length >= 3) return tips.slice(0, 6);

  return [...DEFAULT_TIP_SLUGS]
    .map((slug) => EXPERT_TIPS[slug])
    .filter((tip): tip is ExpertTip => Boolean(tip));
}

export function buildExpertTipsSectionHtml(serviceSlug: string): string {
  const tips = getTipsForService(serviceSlug);
  const cards = tips.map(tipCardHtml).join('');

  return `
    <section class="section expert-tips-home expert-tips-service" id="expert-tips" aria-label="Tips from the expert">
      <div class="container">
        <div class="expert-tips-home-header">
          <div>
            <span class="section-label">Expert Advice</span>
            <h2>Tips from the Expert</h2>
            <p class="expert-tips-home-lead">Practical plumbing advice from our licensed Omaha team.</p>
          </div>
          <a href="/resources/expert-tips" class="btn btn-view-all">View All +</a>
        </div>
        <div class="blog-posts-grid">${cards}
        </div>
      </div>
    </section>
`;
}

export function injectExpertTipsIntoServiceHtml(html: string, route: string): string {
  if (!route.startsWith('/services')) return html;
  if (html.includes('expert-tips-home') || html.includes('id="expert-tips"')) return html;

  const serviceSlug = route === '/services' ? 'index' : route.replace(/^\/services\//, '');
  // Skip only if somehow empty slug
  if (!serviceSlug) return html;

  // For /services index hub, use default tips
  const slugForTips = serviceSlug === 'index' ? 'plumbing-repairs' : serviceSlug;
  const section = buildExpertTipsSectionHtml(slugForTips);

  if (/<section[^>]*class="[^"]*authority-brands/.test(html)) {
    return html.replace(
      /(<section[^>]*class="[^"]*authority-brands[^"]*"[^>]*>)/i,
      `${section}\n    $1`,
    );
  }

  return `${html}\n${section}`;
}
