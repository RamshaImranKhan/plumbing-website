import os

SUB_PAGES = [
    {
        "slug": "sump-pumps",
        "title": "Sump Pump Services",
        "parent": "Pumps",
        "parent_slug": "pumps",
        "desc": "Emergency sump pump repair, installation, and maintenance in Omaha. Protect your basement from flooding.",
        "h1": "Sump Pump Services",
        "intro": "Sump pumps protect your home from significant water damage in the event of weather-related flooding or plumbing emergencies. Benjamin Franklin Plumbing® of Omaha is dedicated to helping you keep your sump pump in excellent condition.",
        "sections": [
            ("Maintenance and Repair for All Sump Pumps", "We service submersible and pedestal sump pumps in all makes and models."),
            ("Sump Pump Installation", "We help you select the right pump based on your area's water table, preferences, maintenance expectations, and budget."),
            ("Sump Pump Maintenance", "Regular inspection includes discharge pipe inspection, float switch testing, bearing lubrication, and battery backup testing."),
            ("Sump Pump Repair", "Our team is available 24/7 for emergency repairs including broken float switches, clogged intakes, faulty check valves, and pumps that continuously run."),
        ],
        "faqs": [
            ("Why is your sump pump so loud?", "Pedestal pumps are usually louder than submersible models. Unusual noises could indicate clogs, damaged parts, or improper sizing. Contact our experts for a professional fix."),
            ("How often should you schedule sump pump maintenance?", "Schedule professional inspection at least once a year. Check your pump every three to four months to ensure it's working properly."),
        ],
    },
    {
        "slug": "pool-pump-plumbers",
        "title": "Pool Pump Plumbers",
        "parent": "Pumps",
        "parent_slug": "pumps",
        "desc": "Professional pool pump plumbing installation and repair in Omaha.",
        "h1": "Pool Pump Plumbers",
        "intro": "Pool pumps enable effective filtration and circulation for your swimming pool. Our licensed plumbers can install, repair, and maintain pool pump plumbing systems.",
        "sections": [
            ("Pool Pump Services", "Our technicians diagnose pump complications and restore proper operation quickly and efficiently."),
            ("Installation", "Professional installation ensures your pool pump delivers excellent performance with a 100% satisfaction guarantee."),
        ],
        "faqs": [],
    },
    {
        "slug": "water-pumps",
        "title": "Water Pump Services",
        "parent": "Pumps",
        "parent_slug": "pumps",
        "desc": "Well pump and irrigation water pump installation and repair in Omaha.",
        "h1": "Water Pump Services",
        "intro": "Water pumps power sprinklers, irrigation systems, and deliver water from wells to your home. Maintaining your water pump is essential and can save thousands in property damage.",
        "sections": [
            ("Well Pumps", "Vital if you rely on well water — draws water from your well and delivers it to your home."),
            ("Irrigation System Pumps", "Pulls water from a source and delivers it to your lawn, garden, or irrigation system."),
            ("Repair & Installation", "Our experts properly diagnose complications and restore proper operation with fair, transparent pricing."),
        ],
        "faqs": [],
    },
    {
        "slug": "sink-installation",
        "title": "Sink Installation Services",
        "parent": "Sinks",
        "parent_slug": "sinks",
        "desc": "Professional kitchen, bathroom, and utility sink installation in Omaha.",
        "h1": "Sink Installation Services",
        "intro": "Whether you're renovating or replacing a damaged sink, our plumbers ensure proper placement to prevent future leaks. Count on Benjamin Franklin Plumbing® of Omaha for sink installation and replacement.",
        "sections": [
            ("Types of Sinks We Install", "Kitchen, bathroom, laundry, utility, outdoor, and commercial/bar sinks in materials including stainless steel, porcelain, granite, and copper."),
            ("Sink Replacement", "Signs it's time: leaks, cracks, persistent odors, inadequate water pressure, or cabinet moisture damage."),
            ("Our Installation Process", "Initial inspection, unpacking and prep, expert installation with faucet connections, and final testing — all code-compliant."),
        ],
        "faqs": [
            ("What is the best kitchen sink material?", "Popular options include stainless steel (durable, affordable), ceramic, marble, composite, and copper. Our installers help you choose based on your needs and budget."),
            ("How long do sinks last?", "Most sinks last 15–30 years depending on material and maintenance."),
        ],
    },
    {
        "slug": "sink-repair",
        "title": "Sink Repair Services",
        "parent": "Sinks",
        "parent_slug": "sinks",
        "desc": "Fast sink leak repair and clog removal in Omaha. Licensed sink repair plumbers.",
        "h1": "Sink Repair Services",
        "intro": "We rely on our sinks every day, and fast repair is essential when issues arise. Our licensed plumbers provide high-quality, prompt sink repair services you can depend on.",
        "sections": [
            ("Common Sink Repairs", "We handle persistent clogs, slow draining, moisture under the sink, and leaks of any size."),
            ("Signs You Need Repair", "Persistent clogs, slow draining, moisture under or around the sink, and visible leaks."),
            ("Why Hire a Professional", "Sink leaks can occur due to several complications — professionals have the skills and tools to diagnose the precise issue and prevent further damage."),
        ],
        "faqs": [
            ("Is it possible to fix a sink leak on my own?", "It's best to hire a professional. Plumbers diagnose the precise issue and help prevent further damage and costly repairs."),
        ],
    },
    {
        "slug": "tankless-water-heaters",
        "title": "Tankless Water Heater Services",
        "parent": "Water Heaters",
        "parent_slug": "water-heaters",
        "desc": "Tankless water heater installation, repair, and maintenance in Omaha. Endless hot water, energy efficient.",
        "h1": "Tankless Water Heater Services",
        "intro": "Modern tankless water heaters produce endless hot water and can save money on energy costs. Count on our local licensed plumbers for installation, replacement, and repair.",
        "sections": [
            ("Types We Service", "Non-condensing and condensing tankless units — any size, model, or fuel type (electric or gas)."),
            ("Advantages", "Endless hot water on demand, energy efficient (heat only when needed), and compact size for small spaces."),
            ("Installation & Repair", "Professional installation with proper venting. We inspect all parts, provide straightforward pricing, and exhaust repair options before replacement."),
            ("Maintenance", "Annual flushing and cleaning extends life up to 20 years. Hard water areas may need service twice a year."),
        ],
        "faqs": [
            ("Is a tankless water heater worth it?", "For most homes, yes — endless hot water, lower energy costs, and flexible installation locations."),
            ("How long should a tankless water heater last?", "Most last 15–20 years with proper maintenance, compared to as little as 6–10 years for tank systems."),
        ],
    },
    {
        "slug": "water-heater-installation",
        "title": "Water Heater Installation",
        "parent": "Water Heaters",
        "parent_slug": "water-heaters",
        "desc": "New water heater installation in Omaha. Tank and tankless units from leading manufacturers.",
        "h1": "Water Heater Installation",
        "intro": "Even well-maintained water heaters have a functional lifespan of ten years or less. Trust Benjamin Franklin Plumbing® of Omaha for new water heater installation backed by a 100% satisfaction guarantee.",
        "sections": [
            ("Types We Install", "Conventional electric or gas, hybrid/heat pump, solar, combination, and tankless water heaters."),
            ("Professional Installation", "We install water heaters from leading manufacturers for safe, long-lasting, reliable use for years to come."),
            ("When to Upgrade", "Recurring repairs, rising energy bills, or inconsistent water temperatures may signal it's time for a new unit."),
        ],
        "faqs": [
            ("How much does water heater replacement cost?", "Cost varies by equipment type, power source, and installation complexity. We provide a detailed estimate before starting work."),
        ],
    },
    {
        "slug": "water-heater-repair",
        "title": "Water Heater Repair",
        "parent": "Water Heaters",
        "parent_slug": "water-heaters",
        "desc": "Water heater repair services in Omaha. Fast, reliable hot water restored.",
        "h1": "Water Heater Repair",
        "intro": "On-demand hot water keeps us clean, healthy, and comfortable. When your water heater is on the fritz, count on Benjamin Franklin Plumbing® of Omaha for reliable repair backed by our 100% satisfaction guarantee.",
        "sections": [
            ("Repair Services", "Our licensed plumbers assess your hot water system and make honest recommendations to repair or replace a faulty unit."),
            ("All Types Serviced", "Conventional electric/gas, hybrid, solar, combination, and tankless water heaters."),
            ("Maintenance", "Annual draining removes sediment buildup. Count on our licensed plumbers for water heater flushes."),
        ],
        "faqs": [
            ("How long does a water heater last?", "Traditional units last 8–10 years; tankless units can last up to 20 years with proper care."),
            ("How often should you drain your water heater?", "Most manufacturers recommend draining at least once a year to remove sediment buildup."),
        ],
    },
    {
        "slug": "drain-cleaning",
        "title": "Drain Cleaning",
        "parent": "Drains",
        "parent_slug": "drains",
        "desc": "Professional drain cleaning services in Omaha. Clear clogs and restore flow.",
        "h1": "Drain Cleaning Services",
        "intro": "Slow or clogged drains disrupt your daily routine. Benjamin Franklin Plumbing® of Omaha provides professional drain cleaning to clear blockages and keep your plumbing flowing smoothly.",
        "sections": [
            ("Expert Drain Cleaning", "Our licensed plumbers use professional tools to clear stubborn clogs in kitchen, bathroom, and main line drains."),
            ("Camera Inspection", "We can inspect pipes with camera technology to locate blockages and identify underlying issues."),
            ("Preventive Maintenance", "Regular drain cleaning helps prevent backups, odors, and costly repairs."),
        ],
        "faqs": [],
    },
    {
        "slug": "drain-installation",
        "title": "Drain Installation",
        "parent": "Drains",
        "parent_slug": "drains",
        "desc": "New drain installation for kitchens, bathrooms, and remodels in Omaha.",
        "h1": "Drain Installation Services",
        "intro": "Whether you're remodeling or adding new fixtures, proper drain installation is essential. Our team ensures code-compliant installation with upfront pricing.",
        "sections": [
            ("New Drain Lines", "Installation for kitchen sinks, bathroom fixtures, laundry rooms, and outdoor drains."),
            ("Remodel Support", "We work with your renovation timeline to install drains that integrate seamlessly with new fixtures."),
        ],
        "faqs": [],
    },
    {
        "slug": "hydrojetting",
        "title": "Hydrojetting",
        "parent": "Drains",
        "parent_slug": "drains",
        "desc": "High-pressure hydrojetting drain cleaning in Omaha for tough clogs and sewer lines.",
        "h1": "Hydrojetting Services",
        "intro": "Hydrojetting uses high-pressure water to scour pipe walls and remove grease, roots, and buildup that snaking can't clear. Ideal for recurring clogs and main sewer lines.",
        "sections": [
            ("When You Need Hydrojetting", "Recurring clogs, slow drains throughout the home, or tree root intrusion in sewer lines."),
            ("Safe & Effective", "Our trained technicians use professional hydrojetting equipment to clean pipes without damaging them."),
        ],
        "faqs": [],
    },
    {
        "slug": "garbage-disposal-installation",
        "title": "Garbage Disposal Installation",
        "parent": "Garbage Disposals",
        "parent_slug": "garbage-disposals",
        "desc": "Garbage disposal installation in Omaha kitchens. Licensed plumbers.",
        "h1": "Garbage Disposal Installation",
        "intro": "Upgrade your kitchen with a new garbage disposal installed by licensed professionals. We handle electrical hookups, plumbing connections, and testing.",
        "sections": [
            ("Professional Installation", "Proper installation prevents leaks, jams, and electrical issues down the road."),
            ("Replacement", "Replacing an old or broken unit? We remove the old disposal and install your new one same-day."),
        ],
        "faqs": [],
    },
    {
        "slug": "garbage-disposal-repair",
        "title": "Garbage Disposal Repair",
        "parent": "Garbage Disposals",
        "parent_slug": "garbage-disposals",
        "desc": "Garbage disposal repair in Omaha. Fix jams, leaks, and motor issues.",
        "h1": "Garbage Disposal Repair",
        "intro": "A malfunctioning garbage disposal is a kitchen headache. Our plumbers diagnose and repair jams, leaks, dull blades, and motor failures quickly.",
        "sections": [
            ("Common Repairs", "Clearing jams, resetting units, fixing leaks, and replacing worn components."),
            ("When to Replace", "If repair costs approach replacement, we'll give you honest advice on the best option."),
        ],
        "faqs": [],
    },
    {
        "slug": "frozen-pipes",
        "title": "Frozen Pipes",
        "parent": "Piping & Repiping",
        "parent_slug": "piping-repiping",
        "desc": "Frozen pipe repair and prevention in Omaha. 24/7 emergency service.",
        "h1": "Frozen Pipe Services",
        "intro": "Omaha winters can freeze exposed pipes and cause bursts. Benjamin Franklin Plumbing® offers emergency frozen pipe thawing, repair, and prevention advice.",
        "sections": [
            ("Emergency Thawing", "24/7 response to thaw frozen pipes and prevent bursting."),
            ("Burst Pipe Repair", "If a pipe has burst, we repair or replace damaged sections quickly."),
            ("Winterization Tips", "Insulate exposed pipes and know your main shut-off valve before cold weather hits."),
        ],
        "faqs": [],
    },
    {
        "slug": "leaking-pipes",
        "title": "Leaking Pipes",
        "parent": "Piping & Repiping",
        "parent_slug": "piping-repiping",
        "desc": "Leaking pipe detection and repair in Omaha. Stop water damage fast.",
        "h1": "Leaking Pipe Repair",
        "intro": "Hidden or visible pipe leaks cause water damage and high bills. Our plumbers locate leaks and provide durable repairs for copper, PEX, and PVC lines.",
        "sections": [
            ("Leak Detection", "Non-destructive methods to find leaks in walls, floors, and underground lines."),
            ("Pipe Repair", "Targeted repairs or section replacement with upfront pricing."),
        ],
        "faqs": [],
    },
    {
        "slug": "pipe-repair",
        "title": "Pipe Repair",
        "parent": "Piping & Repiping",
        "parent_slug": "piping-repiping",
        "desc": "Residential pipe repair in Omaha. Copper, PEX, and PVC pipe services.",
        "h1": "Pipe Repair Services",
        "intro": "From minor pinhole leaks to corroded sections, our licensed plumbers repair all types of residential piping with quality materials and workmanship.",
        "sections": [
            ("All Pipe Types", "Copper, PEX, PVC, and galvanized pipe repair and replacement."),
            ("Repiping", "Whole-home repiping when aging pipes require comprehensive replacement."),
        ],
        "faqs": [],
    },
    {
        "slug": "sewer-line-repair",
        "title": "Sewer Line Repair",
        "parent": "Sewers",
        "parent_slug": "sewers",
        "desc": "Sewer line repair in Omaha. Fix clogs, cracks, and root intrusion.",
        "h1": "Sewer Line Repair",
        "intro": "Sewer line problems cause backups, odors, and yard damage. Benjamin Franklin Plumbing® of Omaha provides professional sewer line repair with camera inspection and upfront pricing.",
        "sections": [
            ("Expert Repair", "We diagnose clogs, cracks, bellied pipes, and root intrusion using modern inspection tools."),
            ("Minimal Disruption", "Our team works efficiently to restore your sewer line with as little disruption as possible."),
        ],
        "faqs": [],
    },
    {
        "slug": "sewer-line-replacement",
        "title": "Sewer Line Replacement and Installation",
        "parent": "Sewers",
        "parent_slug": "sewers",
        "desc": "Sewer line replacement and new installation in Omaha.",
        "h1": "Sewer Line Replacement and Installation",
        "intro": "When repair isn't enough, we provide full sewer line replacement and new installation for homes and properties throughout Omaha metro.",
        "sections": [
            ("Full Replacement", "Complete sewer line replacement when aging or damaged pipes can't be repaired."),
            ("New Installation", "New sewer line installation for renovations, additions, and new construction."),
        ],
        "faqs": [],
    },
    {
        "slug": "trenchless-sewers",
        "title": "Trenchless Sewers",
        "parent": "Sewers",
        "parent_slug": "sewers",
        "desc": "Trenchless sewer repair and replacement in Omaha. Less digging, less mess.",
        "h1": "Trenchless Sewer Services",
        "intro": "Trenchless technology repairs or replaces sewer lines with minimal excavation — preserving your yard, driveway, and landscaping.",
        "sections": [
            ("Pipe Lining", "Creates a new pipe inside the existing line without full trenching."),
            ("Pipe Bursting", "Replaces damaged sewer pipe by pulling new pipe through the old line."),
        ],
        "faqs": [],
    },
    {
        "slug": "toilet-repair",
        "title": "Toilet Repair",
        "parent": "Toilets",
        "parent_slug": "toilets",
        "desc": "Toilet repair in Omaha. Fix running toilets, clogs, and leaks.",
        "h1": "Toilet Repair Services",
        "intro": "Running toilets, clogs, and leaks waste water and cause frustration. Our licensed plumbers fix all toilet problems quickly with upfront pricing.",
        "sections": [
            ("Common Repairs", "Clog removal, flapper and fill valve replacement, wax ring leaks, and running toilet fixes."),
            ("Emergency Service", "Available 24/7 for urgent toilet backups and overflows."),
        ],
        "faqs": [],
    },
    {
        "slug": "toilet-installation",
        "title": "Toilet Installation",
        "parent": "Toilets",
        "parent_slug": "toilets",
        "desc": "New toilet installation and replacement in Omaha bathrooms.",
        "h1": "Toilet Installation Services",
        "intro": "Upgrading your bathroom? We install all toilet types including standard, comfort-height, and water-efficient models with proper sealing and testing.",
        "sections": [
            ("Replacement", "Remove old toilet and install your new unit same-day."),
            ("New Installation", "Install toilets in remodels, additions, and new bathrooms."),
        ],
        "faqs": [],
    },
    {
        "slug": "brita-pro-filtration",
        "title": "Brita PRO® Water Filtration System",
        "parent": "Water Treatment",
        "parent_slug": "water-treatment",
        "desc": "Brita PRO water filtration system installation in Omaha.",
        "h1": "Brita PRO® Water Filtration System",
        "intro": "Improve your home's water quality with professional Brita PRO® water filtration system installation from Benjamin Franklin Plumbing® of Omaha.",
        "sections": [
            ("Whole-Home Filtration", "Reduce contaminants and improve taste throughout your home."),
            ("Professional Installation", "Licensed plumbers ensure proper installation and system performance."),
        ],
        "faqs": [],
    },
    {
        "slug": "leak-repair",
        "title": "Leak Repair",
        "parent": "Leak Detection",
        "parent_slug": "leak-detection",
        "desc": "Professional leak repair in Omaha. Fix pipe and fixture leaks fast.",
        "h1": "Leak Repair Services",
        "intro": "Once a leak is detected, fast repair prevents water damage and high bills. Our plumbers provide durable leak repairs for pipes, fixtures, and connections.",
        "sections": [
            ("All Leak Types", "Pipe leaks, fixture leaks, slab leaks, and hidden wall leaks."),
            ("Upfront Pricing", "Detailed estimates before work begins — no surprise fees."),
        ],
        "faqs": [],
    },
    {
        "slug": "pool-leak-detection",
        "title": "Pool Leak Detection",
        "parent": "Leak Detection",
        "parent_slug": "leak-detection",
        "desc": "Pool leak detection services in Omaha.",
        "h1": "Pool Leak Detection",
        "intro": "Losing pool water? Our team helps locate pool plumbing leaks using professional detection methods to find the source quickly.",
        "sections": [
            ("Detection", "Identify leaks in pool plumbing, returns, and equipment connections."),
            ("Repair Coordination", "Once located, we provide repair options to stop water loss."),
        ],
        "faqs": [],
    },
    {
        "slug": "slab-leaks",
        "title": "Slab Leaks",
        "parent": "Leak Detection",
        "parent_slug": "leak-detection",
        "desc": "Slab leak detection and repair in Omaha. Protect your foundation.",
        "h1": "Slab Leak Services",
        "intro": "Slab leaks occur under your home's foundation and can cause serious damage. We use non-destructive detection and provide repair or rerouting options.",
        "sections": [
            ("Detection", "Acoustic and thermal methods to locate leaks under concrete slabs."),
            ("Repair Options", "Targeted repair, repiping, or rerouting based on damage and budget."),
        ],
        "faqs": [],
    },
    {
        "slug": "plumbing-installation",
        "title": "Plumbing Installation",
        "parent": "Plumbing Repairs",
        "parent_slug": "plumbing-repairs",
        "desc": "Residential plumbing installation in Omaha. New fixtures and systems.",
        "h1": "Plumbing Installation Services",
        "intro": "From new fixtures to whole-home plumbing, Benjamin Franklin Plumbing® of Omaha handles professional installation backed by a 100% satisfaction guarantee.",
        "sections": [
            ("Fixture Installation", "Sinks, faucets, toilets, showers, disposals, and water heaters."),
            ("System Installation", "Water lines, drain lines, and plumbing for remodels and new construction."),
        ],
        "faqs": [],
    },
    {
        "slug": "plumbing-inspection",
        "title": "Plumbing Inspection & Diagnosis",
        "parent": "Plumbing Repairs",
        "parent_slug": "plumbing-repairs",
        "desc": "Plumbing inspection and diagnosis in Omaha. Find problems early.",
        "h1": "Plumbing Inspection & Diagnosis",
        "intro": "Not sure what's wrong? Our licensed plumbers perform thorough inspections and diagnoses to identify issues before they become expensive emergencies.",
        "sections": [
            ("Whole-Home Inspection", "Check pipes, fixtures, water heater, and drains for issues."),
            ("Detailed Diagnosis", "Clear explanation of findings with recommended repair options."),
        ],
        "faqs": [],
    },
    {
        "slug": "shower-installation",
        "title": "Shower Installation",
        "parent": "Showers",
        "parent_slug": "showers",
        "desc": "Shower installation in Omaha. New showers and tub-to-shower conversions.",
        "h1": "Shower Installation Services",
        "intro": "Transform your bathroom with professional shower installation. We handle valve connections, drain lines, and fixture mounting to code.",
        "sections": [
            ("New Showers", "Install walk-in showers, tub-to-shower conversions, and shower/tub combos."),
            ("Fixture Selection", "Help choosing heads, valves, and enclosures for your space and budget."),
        ],
        "faqs": [],
    },
    {
        "slug": "shower-repair",
        "title": "Shower Repair",
        "parent": "Showers",
        "parent_slug": "showers",
        "desc": "Shower repair in Omaha. Fix leaks, valves, and low pressure.",
        "h1": "Shower Repair Services",
        "intro": "Leaky shower valves, low pressure, and dripping heads are no match for our licensed plumbers. We diagnose and repair all shower plumbing issues.",
        "sections": [
            ("Valve Repair", "Fix dripping, stuck, or leaking shower valves and cartridges."),
            ("Drain & Leak Repair", "Clear clogs and fix leaks in shower pans and drain connections."),
        ],
        "faqs": [],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Benjamin Franklin Plumbing Omaha</title>
  <meta name="description" content="{desc} Call (402) 922-8334.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <div class="forbes-bar" id="forbesBar"><p>Named Forbes' Top Ranked Plumbing Company of 2024!</p><button type="button" class="forbes-close" id="forbesClose" aria-label="Dismiss">×</button></div>
  <header class="bfp-header" role="banner">
    <div class="container bfp-header-inner">
      <a href="../index.html" class="bfp-brand"><span class="bfp-logo-mark">🧑‍🔧</span><span class="bfp-logo-text"><strong>Benjamin Franklin</strong><em>The Punctual Plumber</em></span></a>
      <div class="bfp-location"><strong>OMAHA</strong><a href="../index.html#services">Update Location</a></div>
      <nav class="bfp-nav-pill">
        <a href="../index.html#services" class="bfp-nav-link bfp-nav-btn-active">Services</a>
        <a href="../index.html#quote" class="btn btn-book btn-book-nav">Book Now</a>
      </nav>
      <div class="bfp-header-right">
        <div class="bfp-emergency"><span>Call us 24/7!</span><a href="tel:4029228334">(402) 922-8334</a></div>
        <button class="nav-toggle bfp-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
      </div>
    </div>
    <nav class="nav-mobile bfp-mobile-nav" id="navMobile" hidden><a href="../index.html">Home</a><a href="../index.html#quote" class="btn btn-book">Book Now</a></nav>
  </header>
  <main id="main-content" class="service-page">
    <div class="service-breadcrumb"><div class="container"><a href="../index.html">Home</a> / <a href="../index.html#services">Services</a> / <a href="{parent_slug}.html">{parent}</a> / <span>{title}</span></div></div>
    <section class="service-hero">
      <div class="container service-hero-inner">
        <div class="service-hero-content">
          <span class="section-label">{parent} · {title}</span>
          <h1>{h1}</h1>
          <p>{intro}</p>
          <p class="service-guarantee"><strong>100% satisfaction guarantee</strong> on all services.</p>
          <div class="service-hero-cta">
            <a href="../index.html#quote" class="btn btn-primary btn-lg">Schedule Service</a>
            <a href="tel:4029228334" class="btn btn-outline btn-lg">Call (402) 922-8334</a>
          </div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container service-layout">
        <article class="service-main">
          {sections_html}
          {faqs_html}
          <div class="service-cta-box">
            <h2>Schedule Service in Omaha</h2>
            <p>Contact Benjamin Franklin Plumbing® of Omaha for prompt, professional service.</p>
            <a href="../index.html#quote" class="btn btn-primary btn-lg">Get a Quote</a>
          </div>
        </article>
        <aside class="service-sidebar">
          <div class="sidebar-card">
            <h3>{parent} Services</h3>
            <nav class="sidebar-links">{parent_links}</nav>
          </div>
          <div class="sidebar-card sidebar-cta">
            <h3>Need Help Now?</h3>
            <a href="tel:4029228334" class="btn btn-primary btn-full">(402) 922-8334</a>
          </div>
        </aside>
      </div>
    </section>
  </main>
  <footer class="site-footer"><div class="container"><div class="footer-brand"><strong>Benjamin Franklin Plumbing® of Omaha</strong><p>14302 C Circle, Omaha, NE 68144</p></div></div></footer>
  <div class="mobile-cta"><a href="tel:4029228334" class="mobile-cta-call">Call</a><a href="../index.html#quote" class="mobile-cta-book">Book Now</a></div>
  <script src="../app.js"></script>
</body>
</html>'''

PARENT_LINKS = {
    "pumps": [
        ("sump-pumps", "Sump Pumps"),
        ("pool-pump-plumbers", "Pool Pump Plumbers"),
        ("water-pumps", "Water Pumps"),
        ("pumps", "All Pump Services"),
    ],
    "sinks": [
        ("sink-installation", "Sink Installation"),
        ("sink-repair", "Sink Repair"),
        ("sinks", "All Sink Services"),
    ],
    "water-heaters": [
        ("tankless-water-heaters", "Tankless Water Heaters"),
        ("water-heater-installation", "Water Heater Installation"),
        ("water-heater-repair", "Water Heater Repair"),
        ("water-heaters", "All Water Heater Services"),
    ],
    "drains": [
        ("drain-cleaning", "Drain Cleaning"),
        ("drain-installation", "Drain Installation"),
        ("hydrojetting", "Hydrojetting"),
        ("drains", "All Drain Services"),
    ],
    "garbage-disposals": [
        ("garbage-disposal-installation", "Garbage Disposal Installation"),
        ("garbage-disposal-repair", "Garbage Disposal Repair"),
        ("garbage-disposals", "All Garbage Disposal Services"),
    ],
    "piping-repiping": [
        ("frozen-pipes", "Frozen Pipes"),
        ("leaking-pipes", "Leaking Pipes"),
        ("pipe-repair", "Pipe Repair"),
        ("piping-repiping", "All Piping Services"),
    ],
    "sewers": [
        ("sewer-line-repair", "Sewer Line Repair"),
        ("sewer-line-replacement", "Sewer Line Replacement"),
        ("trenchless-sewers", "Trenchless Sewers"),
        ("sewers", "All Sewer Services"),
    ],
    "toilets": [
        ("toilet-repair", "Toilet Repair"),
        ("toilet-installation", "Toilet Installation"),
        ("toilets", "All Toilet Services"),
    ],
    "water-treatment": [
        ("brita-pro-filtration", "Brita PRO Filtration"),
        ("water-treatment", "All Water Treatment"),
    ],
    "leak-detection": [
        ("leak-repair", "Leak Repair"),
        ("pool-leak-detection", "Pool Leak Detection"),
        ("slab-leaks", "Slab Leaks"),
        ("leak-detection", "All Leak Detection"),
    ],
    "plumbing-repairs": [
        ("plumbing-installation", "Plumbing Installation"),
        ("plumbing-inspection", "Plumbing Inspection"),
        ("plumbing-repairs", "All Plumbing Repairs"),
    ],
    "showers": [
        ("shower-installation", "Shower Installation"),
        ("shower-repair", "Shower Repair"),
        ("showers", "All Shower Services"),
    ],
}

os.makedirs("services", exist_ok=True)

for page in SUB_PAGES:
    sections_html = ""
    for heading, body in page["sections"]:
        sections_html += f"<h2>{heading}</h2><p>{body}</p>\n"

    faqs_html = ""
    if page["faqs"]:
        faqs_html = "<h2>FAQs</h2><div class=\"faq-list\">\n"
        for i, (q, a) in enumerate(page["faqs"]):
            open_attr = " open" if i == 0 else ""
            faqs_html += f'<details class="faq-item"{open_attr}><summary>{q}</summary><p>{a}</p></details>\n'
        faqs_html += "</div>\n"

    links = PARENT_LINKS[page["parent_slug"]]
    parent_links = ""
    for slug, label in links:
        active = ' class="active"' if slug == page["slug"] else ""
        parent_links += f'<a href="{slug}.html"{active}>{label}</a>\n'

    html = TEMPLATE.format(
        title=page["title"],
        desc=page["desc"],
        parent=page["parent"],
        parent_slug=page["parent_slug"],
        h1=page["h1"],
        intro=page["intro"],
        sections_html=sections_html,
        faqs_html=faqs_html,
        parent_links=parent_links,
    )
    path = os.path.join("services", page["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Created", path)

print("Done")
