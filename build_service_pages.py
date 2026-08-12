"""Update service page main content from BFP source copy (Omaha localized)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHONE = "(402) 922-8334"
PHONE_TEL = "tel:4029228334"

SIDEBAR = """
        <aside class="service-sidebar">
          <div class="sidebar-card">
            <h3><a href="index.html" class="sidebar-more-link">More Services</a></h3>
            <nav class="sidebar-links">
              <a href="showers.html">Showers</a>
              <a href="sinks.html">Sinks</a>
              <a href="faucets.html">Faucets</a>
              <a href="sewers.html">Sewers</a>
              <a href="garbage-disposals.html">Garbage Disposals</a>
              <a href="plumbing-repairs.html">Plumbing Repairs</a>
              <a href="bathtubs.html">Bathtubs</a>
              <a href="toilets.html">Toilets</a>
              <a href="emergency-plumbing.html">Emergency Service</a>
              <a href="drains.html">Drains</a>
            </nav>
          </div>
          <div class="sidebar-card sidebar-cta">
            <h3>{cta_title}</h3>
            <p>{cta_text}</p>
            <a href="{PHONE_TEL}" class="btn btn-primary btn-full">{PHONE}</a>
            <a href="../index.html#quote" class="btn btn-outline btn-full">Get a Quote</a>
          </div>
        </aside>"""

LOCAL_BLOCK = """
          <h2>Why Choose Benjamin Franklin Plumbing for Local Plumbing Services?</h2>
          <p>As a locally owned and operated Benjamin Franklin Plumbing location, we live and work in the Omaha metro communities we serve. We're proud to give back to our neighbors in the best way we can — providing trustworthy plumbing services that make life easier.</p>
          <p>We develop great relationships with our customers because:</p>
          <ul class="service-benefits-list">
            <li>We answer your calls after hours, even during holidays and weekends.</li>
            <li>We tackle any plumbing project; no job is too big or too small.</li>
            <li>We back all our work with satisfaction guarantees.</li>
          </ul>
          <p class="service-note"><em>Check with your local franchise; services may vary by location.</em></p>"""


def faq_block(items: list[tuple[str, str]]) -> str:
    parts = ['          <div class="faq-list">']
    for i, (q, a) in enumerate(items):
        open_attr = " open" if i == 0 else ""
        parts.append(f'            <details class="faq-item"{open_attr}>')
        parts.append(f"              <summary>{q}</summary>")
        parts.append(f"              <p>{a}</p>")
        parts.append("            </details>")
    parts.append("          </div>")
    return "\n".join(parts)


def hero_section(label: str, h1: str, paragraphs: list[str], subhead: str | None = None) -> str:
    sub = f'          <p class="service-hero-subhead"><strong>{subhead}</strong></p>\n' if subhead else ""
    ps = "\n".join(f"          <p>{p}</p>" for p in paragraphs)
    return f"""    <section class="service-hero">
      <div class="container service-hero-inner">
        <div class="service-hero-content">
          <span class="section-label">Our Services · {label}</span>
          <h1>{h1}</h1>
{sub}{ps}
          <p class="service-guarantee"><strong>A 100% satisfaction guarantee</strong> backs all of our {label.lower()} services in Omaha.</p>
          <div class="service-hero-cta">
            <a href="../index.html#quote" class="btn btn-primary btn-lg">Schedule Service</a>
            <a href="{PHONE_TEL}" class="btn btn-outline btn-lg">Call {PHONE}</a>
          </div>
        </div>
        <div class="service-hero-aside">
          <div class="forbes-badge">
            <span class="forbes-stars">★★★★★</span>
            <div><strong>Voted Best Plumbers!</strong><span>Published by Forbes Magazine</span></div>
          </div>
          <div class="zip-lookup-card">
            <h3>Find your local plumber</h3>
            <form id="zipLookupForm" class="zip-form" novalidate>
              <div class="zip-input-group">
                <label for="serviceZip" class="visually-hidden">Zip Code</label>
                <input type="text" id="serviceZip" placeholder="Zip Code" maxlength="5" pattern="[0-9]{{5}}" inputmode="numeric" required>
                <button type="submit" class="btn btn-primary">Go</button>
              </div>
              <p class="zip-message" id="zipMessage" role="status"></p>
            </form>
          </div>
        </div>
      </div>
    </section>"""


def build_main(
    breadcrumb: str,
    label: str,
    h1: str,
    hero_paragraphs: list[str],
    body: str,
    cta_title: str,
    cta_text: str,
    subhead: str | None = None,
) -> str:
    sidebar = SIDEBAR.format(PHONE=PHONE, PHONE_TEL=PHONE_TEL, cta_title=cta_title, cta_text=cta_text)
    return f"""  <main id="main-content" class="service-page">
    <div class="service-breadcrumb">
      <div class="container">
        <a href="../index.html">Home</a> / <a href="index.html">Plumbing Services</a> / <span>{breadcrumb}</span>
      </div>
    </div>

{hero_section(label, h1, hero_paragraphs, subhead)}

    <section class="section">
      <div class="container service-layout">
        <article class="service-main">
{body}
{LOCAL_BLOCK}
        </article>
{sidebar}
      </div>
    </section>
  </main>"""


PAGES: dict[str, dict] = {}

# --- PUMPS ---
PAGES["pumps.html"] = {
    "title": "Pump Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Sump pump, well pump, and water pump installation, repair, and maintenance in Omaha. Call (402) 922-8334.",
    "breadcrumb": "Pumps",
    "label": "Pumps",
    "h1": "Pump Services",
    "hero": [
        "Benjamin Franklin Plumbing® of Omaha offers reliable, high-quality pump services to support your water systems and protect your home from potential damage.",
    ],
    "cta_title": "Need Pump Service?",
    "cta_text": "24/7 pump repair and installation in Omaha.",
    "body": """
          <h2>Why Are Pumps and Pump Services Important?</h2>
          <p>Different types of pumps are vital parts of plumbing systems. They carry out various functions:</p>
          <ul class="service-problems-list">
            <li>Increasing pressure to transport water when your typical plumbing system loses functionality</li>
            <li>Delivering water from your well to your home</li>
            <li>Enabling lawn irrigation</li>
            <li>Enabling effective filtration in pools</li>
            <li>Protecting your home from flooding in emergency situations</li>
          </ul>
          <p>Maintaining your water pump is essential for your plumbing system's functionality, and it can save you thousands of dollars in property damage in the event of a flood. We provide professional pump services to keep your plumbing systems running smoothly and protect your home.</p>
          <p>Call our pump installation, repair, and maintenance plumbers for help. Our team is ready to take your call 24/7 and schedule a same-day appointment!</p>

          <h2>Types of Pumps We Service</h2>
          <p>Water pumps serve a variety of purposes. Our professional technicians can install, repair, and maintain the following types that handle water in or around your home.</p>
          <h3>Water Pumps</h3>
          <p>Water pumps are most commonly used to power sprinklers, irrigation systems, or pump water from a well to a home. These are common types of water pumps found in homes:</p>
          <ul class="service-benefits-list">
            <li><strong>Well pumps:</strong> Vital if you rely on well water for your appliances, drinking, and other needs.</li>
            <li><strong>Irrigation system pumps:</strong> Pull water from a source such as a river, lake, or well and deliver it to your irrigation system.</li>
          </ul>
          <h3>Sump Pumps</h3>
          <p>Sump pumps transport water from one place to another. They are typically placed in the lowest part of a home to protect it from flooding:</p>
          <ul class="service-benefits-list">
            <li><strong>Submersible pump:</strong> Fully submerges in a sump pit for quiet operation.</li>
            <li><strong>Pedestal sump pump:</strong> Easier to access for maintenance but operates louder.</li>
            <li><strong>Sewer ejector pump:</strong> Handles wastewater and sewage below main sewer lines.</li>
          </ul>

          <h2>How We Can Service Your Pump</h2>
          <h3>Repair</h3>
          <p>We properly diagnose your pump's complication and restore proper operation. Whether you need a minor repair or a full replacement, our experts can address the issue quickly and efficiently.</p>
          <h3>Installation</h3>
          <p>Our pump installation services ensure your new pump delivers excellent performance with a 100% satisfaction guarantee.</p>

          <h2>Why Choose Benjamin Franklin Plumbing for Local Pump Services?</h2>
          <ul class="service-benefits-list">
            <li><strong>Excellent customer service</strong> with clear explanations of every repair or replacement plan.</li>
            <li><strong>Fair, transparent pricing</strong> before work begins.</li>
            <li><strong>Prompt service</strong> with our on-time guarantee.</li>
            <li><strong>Satisfaction guarantees</strong> on every job.</li>
            <li><strong>No after-hours fees</strong> — available 24/7 for emergencies.</li>
            <li><strong>Expertise</strong> from licensed, highly trained plumbers.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Contact Benjamin Franklin Plumbing for Pump Services</h2>
            <p>Call <a href="tel:4029228334">(402) 922-8334</a> to learn more about our pump installation and repair services. We answer calls 24/7 and are available for same-day appointments!</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="sump-pumps.html">Sump Pumps</a></li>
            <li><a href="water-pumps.html">Water Pumps</a></li>
            <li><a href="pool-pump-plumbers.html">Pool Pump Plumbers</a></li>
          </ul>""",
}

# --- SINKS ---
PAGES["sinks.html"] = {
    "title": "Sink Plumbing Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Kitchen and bathroom sink repair, installation, and replacement in Omaha. Licensed sink plumbers. Call (402) 922-8334.",
    "breadcrumb": "Sinks",
    "label": "Sinks",
    "h1": "Sink Plumbing Services",
    "hero": [
        "We rely on our sinks every day, and fast repair is essential when issues arise. Benjamin Franklin Plumbing® of Omaha is here for you if you need a sink repair, replacement, or new installation.",
        "Our licensed plumbers provide high-quality, prompt, and friendly sink plumbing services you can depend on. Whether your sink needs an upgraded look or isn't functioning properly, we provide sink repair, replacement, and installation services.",
    ],
    "cta_title": "Need Sink Service?",
    "cta_text": "Sink repair and installation in Omaha.",
    "body": """
          <h2>The Types of Sinks We Service</h2>
          <p>Our sink services include replacement, repair, and installation for the following:</p>
          <ul class="service-benefits-list">
            <li>Kitchen sink plumbing</li>
            <li>Bathroom sink plumbing</li>
            <li>Laundry sink plumbing</li>
            <li>Garage sink plumbing</li>
            <li>Outdoor sink plumbing</li>
          </ul>
          <p>And any style of sink, including enamel, ceramic, porcelain, plastic, stone, glass, copper, stainless steel, concrete, and terrazzo.</p>

          <h2>Reliable Sink Plumbing Services</h2>
          <p>Whether you want to upgrade your sink, repair damage, or address a malfunction, we can meet your needs with the following services:</p>

          <h3>Sink Installation and Replacement</h3>
          <p>When you trust us with your sink installation or replacement, we will help you choose the best sink, faucet, and fixtures based on your needs and budget. We carefully examine your space, help you select the right option, and install it so you can enjoy the sink of your dreams.</p>
          <p>Installing or replacing a sink on your own can be a complex process, especially if a garbage disposal or instant water heater is involved. Benjamin Franklin Plumbing® of Omaha has the plumbing experience, electrical expertise, and specialized tools to ensure your sink functions effectively and lasts for years to come. We also ensure your new installation or replacement meets local codes.</p>
          <p>Our technicians carefully consider the depth of your current sink, the type of drainpipe your new sink will use, whether the new sink will cover your existing hole(s) for the faucet or accessories, the presence of water stains and the condition of the surrounding countertop, proper sealing methods and products, and faucet and fixture selection.</p>
          <p>When it comes time to install or replace your sink, we safely remove the old sink and install any additional plumbing hookups needed. We don't leave until we test to make sure your new sink is working just how you want it to.</p>

          <h3>Sink Repair</h3>
          <p>If your existing sink sustains damage or doesn't function properly, we can help. Our technicians will thoroughly inspect your sink, diagnose the precise complication, and offer the best solution. We can handle any sink issue, big or small. Some of our most common repairs include:</p>
          <ul class="service-problems-list">
            <li>Faucet and drain repairs</li>
            <li>Leak detection and repair</li>
            <li>Clog removal and slow draining</li>
            <li>Pipe and supply line replacement</li>
            <li>Garbage disposal connections</li>
            <li>Seal, gasket, and mounting hardware replacement</li>
          </ul>

          <h2>Signs You Need Sink Repair Services</h2>
          <p>Some common signs you need sink repair include:</p>
          <ul class="service-problems-list">
            <li>Persistent clogs</li>
            <li>Slow draining</li>
            <li>Moisture under or around the sink</li>
            <li>Leaks</li>
          </ul>
          <p>Whatever the issue, our professional team will address the complete needs of your sink so that it doesn't persist in the future.</p>

          <h2>Why Trust Benjamin Franklin Plumbing for Sink Services?</h2>
          <ul class="service-benefits-list">
            <li><strong>High-quality service:</strong> Our high-quality services are backed by satisfaction guarantees. Our technicians are highly trained and knowledgeable about the latest plumbing technology and trends.</li>
            <li><strong>Excellent customer service:</strong> We believe in providing a pleasant, stress-free experience. Each of our locations is locally operated, which means your assigned technician lives and works in your community.</li>
            <li><strong>On-time arrival:</strong> We are known as The Punctual Plumber® because of our on-time arrival to every appointment. We value your time, and we will pay you $5 for every minute a technician is late up to $300.</li>
            <li><strong>Fair pricing:</strong> We let you know how much a service costs before starting work, so you don't have to worry about hidden fees or unexpected surprises.</li>
            <li><strong>24/7 availability:</strong> With around-the-clock availability, you can count on us for emergency repair services when your sink needs immediate attention.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Find Sink Plumbing Near You</h2>
            <p>Have your sink serviced correctly the first time! No job is too big or too small for Benjamin Franklin Plumbing® of Omaha. Call <a href="tel:4029228334">(402) 922-8334</a> or request an appointment online.</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="sink-repair.html">Sink Repair Services</a></li>
            <li><a href="sink-installation.html">Sink Installation Services</a></li>
            <li><a href="faucets.html">Faucet Repair</a></li>
          </ul>

          <h2>Sink FAQs</h2>
""" + faq_block([
        (
            "Is it possible to fix a sink leak on my own?",
            "It's best to hire a professional plumber to address a leaking sink. Sink leaks can occur due to several complications, and professionals have the skills, tools, and experience to diagnose the precise issue. Hiring a reputable plumber for your repair needs helps you prevent further damage and the costs it could incur.",
        ),
        (
            "Can I plumb a sink?",
            "Plumbing a sink requires several tools, materials, and professional experience. From cutting the sink opening, applying joint compound, and connecting the water supply and drain pipes, there's a lot that can go wrong. Because of this, we don't recommend that you tackle this job on your own — instead, count on the licensed plumbers at Benjamin Franklin Plumbing® of Omaha.",
        ),
        (
            "How long does a sink installation take?",
            "Most standard sink installations take anywhere between two and six hours. However, this depends on the type of sink and any additional plumbing needed.",
        ),
        (
            "How hard is it to move sink plumbing?",
            "It depends on how far you're relocating your sink and any additional plumbing required. Moving your sink over a few feet will be less intensive than across the room, for example. Regardless, this job is best left to the pros.",
        ),
    ]),
}

# --- WATER HEATERS ---
PAGES["water-heaters.html"] = {
    "title": "Water Heater Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Water heater repair, replacement, and installation in Omaha. Tank and tankless units. Call (402) 922-8334.",
    "breadcrumb": "Water Heaters",
    "label": "Water Heaters",
    "h1": "Water Heater Services",
    "subhead": "Professional Hot Water System Repairs and Replacement Done Right",
    "hero": [
        "On-demand hot water keeps us clean, healthy, and comfortable. When your water heater is on the fritz, you feel it. For reliable, local water heater repairs, count on Benjamin Franklin Plumbing® of Omaha.",
        "Every service is backed by our 100% satisfaction guarantee, so you can get back to enjoying hot water when and where you need it. Don't let water heater problems give you the chills — call us today!",
    ],
    "cta_title": "Need Water Heater Service?",
    "cta_text": "Water heater repair and installation in Omaha.",
    "body": """
          <h2>Hot Water Heater Replacement and Repair</h2>
          <p>If you're dealing with recurring water heater repairs, rising energy bills, or inconsistent water temperatures, it may be time to upgrade your equipment. You can count on our licensed plumbers to assess your current hot water system and make honest, clear recommendations to repair or replace a faulty unit. We service all types of water heaters, including:</p>
          <ul class="service-benefits-list">
            <li>Conventional electric or gas water heaters</li>
            <li>Hybrid or heat pump water heaters</li>
            <li>Solar water heaters</li>
            <li>Combination water heaters</li>
          </ul>

          <h3>Tankless Water Heater Services</h3>
          <p>Tankless water heaters offer unlimited hot water and increased energy efficiency. For many homeowners, upgrading to a tankless system is a smart investment, especially if their old unit is on its way out. Get a tankless water heater installed to enjoy endless hot water in every part of your home.</p>
          <p>Learn more about our <a href="tankless-water-heaters.html">tankless water heater services</a>, including installation, repair, and maintenance.</p>

          <h2>Hot Water Heater Installation</h2>
          <p>Even well-maintained water heaters have a functional lifespan of ten years or less. When it's time to upgrade your existing unit, trust Benjamin Franklin Plumbing® of Omaha for new water heater installation services. We install water heaters from leading manufacturers to ensure safe, long-lasting, and reliable use for years to come. Our work is backed by a 100% satisfaction guarantee, so you know your new water heater is installed correctly.</p>
          <p>See our dedicated pages for <a href="water-heater-installation.html">water heater installation</a> and <a href="water-heater-repair.html">water heater repair</a> services.</p>

          <h2>Find Expert Water Heater Service Near Me</h2>
          <p>From replacement and installation to maintenance and repair, our friendly and professional technicians are ready to help. We provide quality, affordable water heater services around your schedule. We arrive on time and with all the tools we need to get the job done.</p>

          <div class="service-cta-box">
            <h2>Keep Your Hot Water Flowing</h2>
            <p>Call <a href="tel:4029228334">(402) 922-8334</a> or request an appointment online for water heater services from Benjamin Franklin Plumbing® of Omaha.</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="tankless-water-heaters.html">Tankless Water Heaters</a></li>
            <li><a href="water-heater-installation.html">Water Heater Installation</a></li>
            <li><a href="water-heater-repair.html">Water Heater Repair</a></li>
          </ul>

          <h2>Water Heaters FAQs</h2>
""" + faq_block([
        (
            "How long does a water heater last?",
            "Traditional water heaters usually last between 8 and 10 years, but this varies based on the quality of the equipment, frequency of maintenance, water content, and other factors. Tankless water heaters can last up to 20 years, depending on the care they receive.",
        ),
        (
            "How often should you drain your water heater?",
            "Most manufacturers recommend draining your water heater at least once a year to remove sediment buildup. Some units may need more frequent flushes depending on water hardness levels, overall use, and the age of your tank. Count on our licensed plumbers for water heater flushes.",
        ),
        (
            "How much does water heater replacement cost?",
            "The cost to replace a water heater varies based on numerous factors, including the make and model of the new equipment, the type of power used for the new model, and several other variables. Your Benjamin Franklin Plumbing® of Omaha plumber will provide a detailed estimate and replacement timelines before starting work.",
        ),
    ]),
}

# --- DRAINS ---
PAGES["drains.html"] = {
    "title": "Professional Drain Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Affordable drain cleaning, clearing, and emergency drain services in Omaha. Call (402) 922-8334.",
    "breadcrumb": "Drains",
    "label": "Drains",
    "h1": "Professional Drain Services",
    "subhead": "Affordable Cleaning, Clearing, and Emergency Drain Services",
    "hero": [
        "Your home's plumbing relies on drains to quickly and efficiently remove wastewater. Homeowners rarely think about their drains until something goes wrong.",
        "From proactive cleaning to emergency drain services, Benjamin Franklin Plumbing® of Omaha is the best choice for fast, reliable service when you need it most. Don't flush time or money down the drain — call us today!",
    ],
    "cta_title": "Need Drain Service?",
    "cta_text": "Drain cleaning and clearing in Omaha.",
    "body": """
          <h2>Drain Services to Solve All Your Plumbing Problems</h2>
          <p>Clogged, dirty, or leaking drains are more than inconvenient. Backed-up drains pose a real health hazard that causes waste to back up into your home, exposing your family to bacteria and foul odors. The best way to prevent drain problems is through proactive maintenance and service from a trusted plumbing professional.</p>
          <p>Our most common drain services include:</p>
          <ul class="service-benefits-list">
            <li><a href="drain-cleaning.html">Drain cleaning</a> for kitchen, bathroom, and main line clogs</li>
            <li><a href="hydrojetting.html">Hydrojetting</a> for tough buildup and recurring blockages</li>
            <li><a href="drain-installation.html">Drain installation</a> for remodels and new fixtures</li>
            <li>Camera inspection to locate blockages and identify underlying issues</li>
            <li>Emergency drain services available 24/7</li>
          </ul>
          <p>If you're looking for a thorough drain inspection, replacement, or repair, we can help. Contact Benjamin Franklin Plumbing® of Omaha today to book an appointment.</p>

          <h2>Five Signs You May Need Professional Drain Services</h2>
          <p>Troublesome drains are easy for homeowners to spot but tough to address. If you notice any of these issues, trust Benjamin Franklin Plumbing® of Omaha for professional assistance:</p>
          <ul class="service-problems-list">
            <li>Slow draining in sinks, tubs, or showers</li>
            <li>Pooling water around fixtures or on your property</li>
            <li>Bad odors coming from drains</li>
            <li>Loud noises while draining</li>
            <li>Leaks stemming from the drain or adjacent piping</li>
          </ul>

          <h2>Affordable Drain Services Near Me</h2>
          <p>Benjamin Franklin Plumbing® of Omaha has skilled and experienced plumbers ready to help. We take exceptional pride in our professionalism, experience, and work ethic. We take the time to answer your questions, recommend repairs, and only start work with your permission.</p>

          <div class="service-cta-box">
            <h2>Allow Benjamin Franklin Plumbing to Drain Your Problems Away Today!</h2>
            <p>Every Benjamin Franklin Plumbing location is locally owned and operated, so you'll get a team that's invested in your community. Call <a href="tel:4029228334">(402) 922-8334</a> — we're available for same-day appointments!</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="emergency-plumbing.html">Emergency Plumbing Services</a></li>
            <li><a href="garbage-disposals.html">Garbage Disposal Installation and Repair</a></li>
            <li><a href="sinks.html">Sink Installation and Repair</a></li>
            <li><a href="drain-cleaning.html">Drain Cleaning</a></li>
            <li><a href="hydrojetting.html">Hydrojetting</a></li>
          </ul>""",
}

# --- GARBAGE DISPOSALS ---
PAGES["garbage-disposals.html"] = {
    "title": "Garbage Disposal Service | Benjamin Franklin Plumbing Omaha",
    "meta": "Garbage disposal repair and installation in Omaha kitchens. Licensed plumbers. Call (402) 922-8334.",
    "breadcrumb": "Garbage Disposals",
    "label": "Garbage Disposals",
    "h1": "Garbage Disposal Service",
    "subhead": "Keeping Your Kitchen Humming with Professional Plumbing Help",
    "hero": [
        "A functioning garbage disposal is a modern kitchen essential, making food cleanup quick and easy. When your disposal breaks down, it can lead to unpleasant odors, clogged drains, and a frustrating mess.",
        "If your disposal system is on the fritz, Benjamin Franklin Plumbing® of Omaha is ready to help! We are experts when it comes to garbage disposal systems — from minor repairs to new installations.",
    ],
    "cta_title": "Need Disposal Service?",
    "cta_text": "Garbage disposal repair and installation in Omaha.",
    "body": """
          <h2>Our Garbage Disposal Services</h2>
          <p>At Benjamin Franklin Plumbing® of Omaha, we specialize in garbage disposal repair and installation to keep your system in peak condition. Our licensed technicians have the expertise and equipment to address your garbage disposal needs with lasting solutions.</p>

          <h3>Garbage Disposal Repair</h3>
          <p>Your garbage disposal system will give you several signs when it's time for a repair. If it's making strange noises or failing to grind food properly, don't stick your hand down there. Our skilled plumbers can diagnose and repair various garbage disposal problems, including:</p>
          <ul class="service-problems-list">
            <li><strong>Clogs:</strong> Our plumbers can safely remove obstructions in your garbage disposal and restore proper function.</li>
            <li><strong>Motor issues:</strong> We can repair or replace faulty motors to get your disposal running like new.</li>
            <li><strong>Leaks:</strong> We identify and fix leaks in your system to prevent water damage and unpleasant odors.</li>
            <li><strong>Noisy operation:</strong> Strange noises can be a sign of worn-out blades, impellers, or other components. We can replace them with quality parts.</li>
          </ul>
          <p>Our technicians come equipped with fully stocked trucks, ensuring they have the parts needed for prompt repairs. See our dedicated <a href="garbage-disposal-repair.html">garbage disposal repair</a> page for more details.</p>

          <h3>Garbage Disposal Installation</h3>
          <p>Whether you're installing a new garbage disposal or replacing an old one, our team can handle the job with ease. We can help you pick the most suitable garbage disposal for your needs and budget and then install it quickly and efficiently.</p>
          <p>We use proven techniques and advanced tools to ensure your new garbage disposal is properly connected and functioning optimally. Our experts make sure the garbage disposal integrates seamlessly with your existing system. Learn more about our <a href="garbage-disposal-installation.html">garbage disposal installation</a> services.</p>

          <h2>What Makes Benjamin Franklin Plumbing the Ideal Choice?</h2>
          <ul class="service-benefits-list">
            <li><strong>Excellent work and customer service:</strong> Our team is trained, experienced, and background-checked. With our industry-leading guarantees, we go above and beyond to make sure you are satisfied with our work.</li>
            <li><strong>24/7 emergency plumbing services:</strong> When you need help after hours or during the holidays, our dedicated plumbers will be ready to repair your system.</li>
            <li><strong>On-time guarantee:</strong> As The Punctual Plumber®, we respect your time on every appointment.</li>
            <li><strong>Upfront pricing:</strong> You'll know the cost before we start work — no hidden fees.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Find Reliable Garbage Disposal Repair Near You</h2>
            <p>Say goodbye to kitchen messes with Benjamin Franklin Plumbing® of Omaha as your trusted plumber. Call <a href="tel:4029228334">(402) 922-8334</a> today to find out the Benjamin Franklin Plumbing difference!</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="garbage-disposal-repair.html">Garbage Disposal Repair</a></li>
            <li><a href="garbage-disposal-installation.html">Garbage Disposal Installation</a></li>
            <li><a href="sinks.html">Sink Plumbing Services</a></li>
            <li><a href="drains.html">Drain Services</a></li>
          </ul>""",
}

# --- PIPING & REPIPING ---
PAGES["piping-repiping.html"] = {
    "title": "Piping & Repiping Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Frozen, leaky, and burst pipe repair plus repiping and gas line services in Omaha. Call (402) 922-8334.",
    "breadcrumb": "Piping & Repiping",
    "label": "Piping & Repiping",
    "h1": "Piping & Repiping Services",
    "subhead": "Count on Our Reliable Piping Plumbers to Help You",
    "hero": [
        "Don't let old or damaged pipes disrupt the comfort and safety of your home. At Benjamin Franklin Plumbing® of Omaha, we specialize in expert piping and repiping solutions that give you peace of mind.",
        "Forget about disruptive leaks, foul-tasting water, and the constant worry of plumbing emergencies. Our team is skilled, efficient, and friendly, so you can be certain we handle every aspect of the job professionally.",
    ],
    "cta_title": "Need Pipe Service?",
    "cta_text": "Piping and repiping in Omaha.",
    "body": """
          <h2>Common Piping Issues We Resolve</h2>
          <p>Our expert plumbers are trained to resolve a wide range of piping issues. We use advanced plumbing equipment and technology to minimize disruptions and ensure precise work. We repair:</p>
          <ul class="service-problems-list">
            <li><strong>Frozen pipes:</strong> Our plumbers quickly thaw frozen pipes to stop them from bursting and causing extensive water damage to your home. We also offer insulation solutions to protect your pipes from future freezing during Omaha winters.</li>
            <li><strong>Leaky pipes:</strong> We can efficiently locate and repair leaks, no matter how small. We use proven techniques and quality materials to make sure the repairs last.</li>
            <li><strong>Burst pipes:</strong> Our rapid response team is available to quickly repair burst pipes and mitigate any resulting damage to your home.</li>
          </ul>
          <p>See our dedicated pages for <a href="frozen-pipes.html">frozen pipes</a>, <a href="leaking-pipes.html">leaking pipes</a>, and <a href="pipe-repair.html">pipe repair</a> services.</p>

          <h2>Our Professional Piping and Repiping Solutions</h2>
          <p>Benjamin Franklin Plumbing® of Omaha is a trusted choice for reliable and professional piping and repiping solutions. We take a comprehensive and personalized approach to every job to produce long-lasting results.</p>

          <h3>Inspection for Expert Diagnosis</h3>
          <p>Not sure if you need a repair or a complete repipe plumbing solution? Our skilled technicians can inspect your pipes and recommend the most effective solution. Our inspections involve a thorough analysis of your plumbing system to find the root cause of the issue.</p>

          <h3>Customized Piping Solution</h3>
          <p>At Benjamin Franklin Plumbing, we don't believe in one-size-fits-all. If you need a new plumbing system, we design a solution that is tailored to your home's specific needs. Whether you're remodeling or simply upgrading your existing infrastructure, our systems will work perfectly with your space.</p>

          <h3>Gas Line Solutions</h3>
          <p>We install new gas lines for your water heater, fireplace, outdoor kitchen, or other areas in your home. Our expert technicians perform safe and code-compliant gas line installations. We can also help with sizing your system to determine if it can handle the additional demand of new appliances.</p>

          <h3>Emergency Piping and Repiping</h3>
          <p>We understand that plumbing problems are stressful and can occur at any time. That's why we offer 24/7 emergency service with no overtime charge, even on weekends and holidays. Plus, our on-time guarantee means we value your time as much as you do.</p>

          <div class="service-cta-box">
            <h2>Connect With Our Experts for Reliable Repipe Plumbing Solutions</h2>
            <p>When you need quality piping and repiping services, trust Benjamin Franklin Plumbing® of Omaha. Call <a href="tel:4029228334">(402) 922-8334</a> to schedule an appointment!</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="frozen-pipes.html">Frozen Pipes</a></li>
            <li><a href="leaking-pipes.html">Leaking Pipes</a></li>
            <li><a href="pipe-repair.html">Pipe Repair</a></li>
            <li><a href="leak-detection.html">Leak Detection</a></li>
          </ul>""",
}

# --- SEWERS ---
PAGES["sewers.html"] = {
    "title": "Sewer Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Sewer line repair, trenchless replacement, and emergency sewer services in Omaha. Call (402) 922-8334.",
    "breadcrumb": "Sewers",
    "label": "Sewers",
    "h1": "Sewer Services",
    "hero": [
        "Sewer line problems can disrupt your home, create health hazards, and become costly if left unchecked. Even sewer fumes are harmful to your health due to exposure to hydrogen sulfide.",
        "That's why it's so important to address these issues with care and precision. At Benjamin Franklin Plumbing® of Omaha, our licensed plumbers bring decades of experience and the dedication you need when facing sewer troubles. From routine repairs to urgent emergencies, we're available 24/7.",
    ],
    "cta_title": "Need Sewer Service?",
    "cta_text": "Sewer repair and replacement in Omaha.",
    "body": """
          <h2>Comprehensive Sewer Services for Your Home</h2>
          <p>Every home is different, and so is every sewer system. Our team has the training and expertise to work with all types of residential sewer systems, including sanitary, storm, and combined sewers. We provide a full range of sewer services.</p>

          <h3>Sewer Line Repair</h3>
          <p>We fix cracks, root damage, corrosion, or backups from clogged drains through our residential sewer line services. With camera inspection technology and targeted repairs, we restore proper flow quickly and help prevent future issues. See our <a href="sewer-line-repair.html">sewer line repair</a> page for details.</p>

          <h3>Trenchless Sewer Repair</h3>
          <p>Our trenchless sewer repair minimizes disruption with minimal surface impact — it's a cost-effective alternative to traditional methods. If standard repairs aren't possible or ideal, trenchless sewer repair is the best option. Learn more about our <a href="trenchless-sewers.html">trenchless sewer services</a>.</p>

          <h3>Sewer Line Replacement</h3>
          <p>When repairs aren't possible, our technicians provide full sewer line replacement services to dig up the damaged lines and install new ones. This process is the best option for lines with extensive damage. See our <a href="sewer-line-replacement.html">sewer line replacement and installation</a> services.</p>

          <h3>Emergency Sewer Services</h3>
          <p>We're available 24/7 with no overtime or weekend fees. If you're noticing signs like foul odors, frequent clogs, slow drains, water pooling in your yard, or mold around your plumbing, it may be time to schedule sewer services with our team.</p>

          <h2>Why Choose Benjamin Franklin Plumbing?</h2>
          <ul class="service-benefits-list">
            <li><strong>Trained team:</strong> We have licensed, certified, and insured plumbers ready to handle every job.</li>
            <li><strong>Transparent recommendations:</strong> When possible, we opt for repair over replacement to save you money.</li>
            <li><strong>Friendly, punctual service:</strong> We're The Punctual Plumber®, and we back it up with our on-time guarantee.</li>
            <li><strong>Customer-first approach:</strong> Your home, your comfort, and your budget always come first.</li>
            <li><strong>Trusted reputation:</strong> Our team is known for building lasting relationships with homeowners.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Get Sewer Services You Can Trust</h2>
            <p>Sewer problems can't wait, and neither should you. Call <a href="tel:4029228334">(402) 922-8334</a> or request an appointment online to restore comfort and safety to your home.</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="sewer-line-repair.html">Sewer Line Repair</a></li>
            <li><a href="sewer-line-replacement.html">Sewer Line Replacement &amp; Installation</a></li>
            <li><a href="trenchless-sewers.html">Trenchless Sewer Services</a></li>
            <li><a href="drains.html">Drain Services</a></li>
          </ul>

          <h2>Sewer FAQs</h2>
""" + faq_block([
        (
            "Why does my bathroom smell like sewer?",
            "A sewer-like odor often comes from bacteria growing inside bathroom drains. Clear out any debris, using a brush if necessary, and flush the drains thoroughly to eliminate buildup. Another common cause is a dry P-trap. Running water in the tub, shower, and sink for a minute usually refills the trap and stops the smell.",
        ),
        (
            "Can a sewer line unclog itself?",
            "It's possible, but it's never a good idea to risk it. Even if a sewer line clog manages to clear itself, it's possible that damage either caused or resulted from the clog. It's always best to contact a licensed plumber to inspect your sewer lines if you're dealing with any kind of backup.",
        ),
        (
            "Can you tell me what to do when your sewer backs up?",
            "Call Benjamin Franklin Plumbing® of Omaha for emergency sewer services at (402) 922-8334. Follow the direct advice of your plumber. Wear protective gear if you have to walk through any sewage. Avoid using any plumbing fixtures until your plumber arrives.",
        ),
        (
            "Does home insurance cover sewer lines?",
            "In many cases, home insurance will cover sewer line damage within your property lines if it's caused by a covered natural disaster. Damage due to poor installation, neglect, or lack of maintenance is typically not covered. Contact your insurance provider to confirm your coverage and limitations.",
        ),
    ]),
}

# --- TOILETS ---
PAGES["toilets.html"] = {
    "title": "Toilet Plumbing Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Toilet repair, replacement, and installation in Omaha. 24/7 emergency service. Call (402) 922-8334.",
    "breadcrumb": "Toilets",
    "label": "Toilets",
    "h1": "Toilet Plumbing",
    "subhead": "Toilet Problems Stink — Until You Get Benjamin Franklin Plumbing Involved",
    "hero": [
        "Toilet problems can be a major headache for any homeowner. Even if it's a stubborn clog or complete breakdown, you need a reliable plumber when you are experiencing toilet issues.",
        "Benjamin Franklin Plumbing® of Omaha is here to restore peace and proper flushing to your home. We can also install a new toilet or replace your outdated one. Call us today — our experts are ready to help you schedule an appointment 24/7!",
    ],
    "cta_title": "Need Toilet Service?",
    "cta_text": "Toilet repair and installation in Omaha.",
    "body": """
          <h2>A Professional, Trustworthy Plumber for Toilet Services</h2>
          <p>Benjamin Franklin Plumbing® of Omaha is a trusted provider of professional toilet repair, installation, and replacement. Our skilled plumbers are equipped with the expertise to handle a wide range of toilet services.</p>

          <h2>Toilet Repair Services</h2>
          <p>Is your toilet constantly leaking or failing to flush properly? Don't let a faulty toilet disrupt your household. Our plumbers address various issues, from minor leaks to more complex problems with the flapper, fill valve, or other components. We can diagnose the problem quickly and provide effective repairs using quality parts.</p>
          <p>Our plumbers come prepared with the tools and expertise to get your toilet back in perfect working order. See our dedicated <a href="toilet-repair.html">toilet repair</a> page for more details.</p>

          <h2>Toilet Replacement</h2>
          <p>When repairs are no longer sufficient, or your toilet is outdated, a replacement is an ideal solution. Our experts will help you select a newer, higher-efficiency model that suits your needs and budget.</p>
          <p>We carefully remove your old toilet and make sure it's properly disposed of. Then, we skillfully install your new toilet to make certain it's leak-free and secure. If you only need to replace specific parts, our technicians have you covered.</p>

          <h2>Toilet Installation</h2>
          <p>Whether you're remodeling your bathroom or adding a new one, proper toilet installation is crucial for long-term performance and reliability. Our skilled plumbers can handle everything, from connecting to the water supply and drain lines to leveling and sealing. We take pride in our meticulous workmanship and attention to detail. Our team ensures your new installation is up to code and functions flawlessly.</p>
          <p>Learn more about our <a href="toilet-installation.html">toilet installation services</a>.</p>

          <h2>Emergency Plumbing Services</h2>
          <p>At Benjamin Franklin Plumbing, we want to be there for you when you need it the most. Our technicians can quickly resolve an urgent toilet issue. We offer 24/7 emergency plumbing services at no extra cost for overtime. Our friendly customer service is ready to take your call anytime and will dispatch a plumber to perform the service.</p>

          <div class="service-cta-box">
            <h2>Contact Our Experts for Reliable Toilet Services</h2>
            <p>You can trust the work done by Benjamin Franklin Plumbing® of Omaha because we back all our work with industry-leading guarantees. Call <a href="tel:4029228334">(402) 922-8334</a> — our toilet plumbing professionals take calls 24/7 and are frequently available for same-day appointments.</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="toilet-repair.html">Toilet Repair</a></li>
            <li><a href="toilet-installation.html">Toilet Installation</a></li>
            <li><a href="emergency-plumbing.html">Emergency Plumbing Services</a></li>
          </ul>""",
}

# --- WATER TREATMENT ---
PAGES["water-treatment.html"] = {
    "title": "Home Water Treatment Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Water filtration, softener installation, and water treatment repair in Omaha. Call (402) 922-8334.",
    "breadcrumb": "Water Treatment",
    "label": "Water Treatment",
    "h1": "Home Water Treatment Services",
    "hero": [
        "Enjoy peace of mind with healthier, better-tasting water at home. Benjamin Franklin Plumbing® of Omaha offers water purification services designed to eliminate impurities, address hard water, and make every sip more satisfying.",
        "Your home may have water impurities, hard water, or both — even without you realizing it. Whether you need a new water filtration system or a system repair, we're here for you.",
    ],
    "cta_title": "Need Water Treatment?",
    "cta_text": "Filtration and softener services in Omaha.",
    "body": """
          <h2>Professional Water Treatment Services</h2>
          <p>Whole-house water filtration systems provide on-demand, clean drinking water to reduce exposure to potentially harmful chemicals, improve taste, and address common issues like hard water. Benjamin Franklin Plumbing's expert technicians will thoroughly inspect your current water system, test your water, and determine the best solution based on your home's needs and budget.</p>
          <p>We offer the following water treatment services so you can enjoy safe, clean water:</p>

          <h3>Water Filtration System and Water Softener Installation</h3>
          <p>Whether you want an in-home filtration system or a reverse osmosis system, we provide professional installation services to ensure it works effectively. Our technicians use their expertise to determine your home's precise needs based on specific water impurities.</p>
          <p>We can also determine if hard water impacts your home, recommending the best water softener to protect your pipes and appliances. A water softener helps prevent mineral buildup from clogging your pipes and impacting your health, and our team can install a high-quality, cost-effective solution. With the right water softener, you can enjoy healthier hair and skin, easier cleaning, and greater appliance longevity.</p>
          <p>Learn more about our <a href="brita-pro-filtration.html">Brita PRO® Water Filtration System</a> installation services.</p>

          <h3>Expert Maintenance and Repair</h3>
          <p>We also offer maintenance and repair services to keep your water treatment system in top shape, including:</p>
          <ul class="service-benefits-list">
            <li>Sediment filter cleaning</li>
            <li>Filter replacements</li>
            <li>Bulb replacements</li>
            <li>Sleeve cleaning or replacement</li>
            <li>Resin bed replacement</li>
            <li>Brine tank cleaning</li>
            <li>Control valve repair or replacement</li>
            <li>Motor repair or replacement</li>
          </ul>

          <h2>Signs That Your Water Treatment System Requires Repair</h2>
          <p>Your water filtration or softener system may need attention if you notice any of the following signs:</p>
          <ul class="service-problems-list">
            <li>Mineral buildup</li>
            <li>Spotty dishes</li>
            <li>Leaks</li>
            <li>An unusual water taste, odor, or appearance</li>
            <li>Changes in water pressure</li>
            <li>Unusually dry skin after showering or washing hands</li>
            <li>Unusual noises from your water softener or filtration system unit</li>
            <li>Increased water softener salt usage</li>
            <li>Increased energy consumption</li>
          </ul>

          <h2>Why Trust Benjamin Franklin Plumbing With Your Water Treatment System Needs?</h2>
          <ul class="service-benefits-list">
            <li><strong>Excellent customer service:</strong> Each technician lives and works in the community they serve, offering trustworthy, friendly service.</li>
            <li><strong>Quality results:</strong> We offer satisfaction guarantees and stand behind the quality of our work.</li>
            <li><strong>Honest pricing:</strong> Before we start an installation or repair, we break down the cost for you with no hidden or unexpected fees.</li>
            <li><strong>24/7 availability:</strong> We have technicians available around the clock, including weekends and holidays at no additional cost.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Find Home Water Treatment Services Near You</h2>
            <p>Trust Benjamin Franklin Plumbing® of Omaha for reliable water purification services with a 100% satisfaction guarantee. Call <a href="tel:4029228334">(402) 922-8334</a> to schedule service today!</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="brita-pro-filtration.html">Brita PRO® Water Filtration System</a></li>
            <li><a href="water-heaters.html">Water Heater Services</a></li>
          </ul>

          <h2>Water Purification Service FAQs</h2>
""" + faq_block([
        (
            "How much is a reverse osmosis system installation?",
            "How much it costs to install a reverse osmosis system varies based on several factors, including the price of the equipment, the time it takes to complete installation, and other variables. After an initial consultation, we'll provide a detailed estimate so you know exactly how much it will cost and how long it will take.",
        ),
        (
            "Do plumbers fix water softeners?",
            "You bet! We're your local water softener service experts and can repair, install, and replace water softeners from any manufacturer.",
        ),
        (
            "What else should I know about water purification?",
            "Most US homes have hard water, water impurities, or both. While chemical levels likely meet local and federal limits, millions of Americans ingest trace amounts of chlorine, lead, and nitrates from fertilizers and pesticides.",
        ),
        (
            "How does a water softener system improve plumbing performance?",
            "A water softener improves plumbing performance by preventing or minimizing mineral buildup. Hard water can cause minerals such as magnesium and calcium to accumulate inside your home's water appliances, pipes, and fixtures. A water softener removes these minerals to prevent clogs and allow water to flow freely through your pipes.",
        ),
    ]),
}

# --- LEAK DETECTION ---
PAGES["leak-detection.html"] = {
    "title": "Leak Detection Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Professional plumbing leak detection in Omaha. Non-invasive methods. Call (402) 922-8334.",
    "breadcrumb": "Leak Detection",
    "label": "Leak Detection",
    "h1": "Leak Detection Services",
    "hero": [
        "If you notice visible water damage or suspect plumbing leaks around your home, a bigger problem may be brewing. Sometimes, leaking pipes can drip for months before receiving attention.",
        "For quick, reliable, and thorough plumbing leak detection services, count on the licensed plumbers at Benjamin Franklin Plumbing® of Omaha. Our experts will find the leak no matter where it's hiding — behind walls, above ceilings, at the foundation — and quickly make the necessary repair.",
    ],
    "cta_title": "Suspect a Leak?",
    "cta_text": "Leak detection in Omaha.",
    "body": """
          <h2>The Types of Plumbing Leaks We Repair</h2>
          <p>Our team will inspect and repair leaks for all these and more:</p>
          <ul class="service-benefits-list">
            <li>Pipe leaks in walls, floors, and ceilings</li>
            <li><a href="slab-leaks.html">Slab leaks</a> under your home's foundation</li>
            <li>Fixture and faucet leaks</li>
            <li><a href="pool-leak-detection.html">Pool plumbing leaks</a></li>
            <li>Water heater and appliance connection leaks</li>
            <li>Underground and outdoor line leaks</li>
          </ul>

          <h2>Common Signs of Plumbing Leaks</h2>
          <ul class="service-problems-list">
            <li>Unexplained water bill increases</li>
            <li>Loud pipes, even when water isn't being used</li>
            <li>Pools of water collecting in your home or on your property</li>
            <li>Damp carpet</li>
            <li>Mold and mildew</li>
            <li>Inadequate water pressure</li>
            <li>Continually cycling water heater</li>
            <li>Warm spots on your floors</li>
          </ul>

          <h2>Why Choose Benjamin Franklin Plumbing for Leak Detection Services?</h2>
          <ul class="service-benefits-list">
            <li><strong>Local experts:</strong> Benjamin Franklin Plumbing® of Omaha is locally owned and operated, so a local expert familiar with plumbing issues in your area will be investigating your home.</li>
            <li><strong>The Punctual Plumber®:</strong> We know how annoying it is to wait for a service provider to arrive. We'll come when you expect us, or we'll pay you for your time!</li>
            <li><strong>UWIN guarantee:</strong> If you have any issues after our work is complete, we'll make it right for you.</li>
            <li><strong>Non-invasive methods:</strong> Our leak detection methods are non-invasive and accurate. We respect the homes of our customers and treat them as our own.</li>
            <li><strong>24/7 availability:</strong> Need emergency water leak detection? We're on standby 24/7 with no after-hours fees.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Find Plumbing Leak Detection Near Me</h2>
            <p>At the first sign of a water leak in your home, contact Benjamin Franklin Plumbing® of Omaha. Call <a href="tel:4029228334">(402) 922-8334</a> or request an appointment online to get started.</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="leak-repair.html">Leak Repair</a></li>
            <li><a href="slab-leaks.html">Slab Leaks</a></li>
            <li><a href="pool-leak-detection.html">Pool Leak Detection</a></li>
            <li><a href="leaking-pipes.html">Leaking Pipes</a></li>
          </ul>

          <h2>Leak Detection FAQs</h2>
""" + faq_block([
        (
            "Can you tell me how to detect a water leak?",
            "If you suspect a water leak in your home, the most reliable solution is to call a plumbing professional. Our experts have special tools and will be able to correctly identify the leak source and any additional damage throughout your home.",
        ),
        (
            "How does leak detection work?",
            "Most leak detection systems use a small turbine or ultrasonic wavelengths to monitor the flow of water through your pipes. These systems use sensors to recognize and record abnormalities in water flow, pressure, gallonage, or temperature changes. When there's an issue identified, our plumbing professionals then use these readings to identify the source of the issue.",
        ),
        (
            "Is leak detection covered by insurance?",
            "Most homeowners insurance will cover water damage due to plumbing leaks. However, this may not include long-term issues that could have been resolved with proper maintenance.",
        ),
    ]),
}

# --- PLUMBING REPAIRS ---
PAGES["plumbing-repairs.html"] = {
    "title": "Plumbing Repair Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Professional plumbing repair services in Omaha. 24/7 emergency repairs. Call (402) 922-8334.",
    "breadcrumb": "Plumbing Repairs",
    "label": "Plumbing Repairs",
    "h1": "Plumbing Repair Services",
    "hero": [
        "Plumbing is integrated into almost every aspect of our day-to-day: cooking, cleaning, drinking, washing, disposing of waste, and so much more. So, when something goes wrong, you need repairs fast.",
        "The licensed plumbers at Benjamin Franklin Plumbing® of Omaha are available 24/7 to provide you with quality repair services whenever you need them most. Don't delay emergency plumbing repairs — call us today!",
    ],
    "cta_title": "Need a Plumber?",
    "cta_text": "24/7 plumbing repairs in Omaha.",
    "body": """
          <h2>The Types of Plumbing Repairs We Provide</h2>
          <p>Our professional plumbing repair services cover nearly every type of plumbing fixture, appliance, or line, including:</p>
          <ul class="service-benefits-list">
            <li><a href="faucets.html">Faucet repair and replacement</a></li>
            <li><a href="toilets.html">Toilet repair and installation</a></li>
            <li><a href="sinks.html">Sink repair and installation</a></li>
            <li><a href="showers.html">Shower repair and installation</a></li>
            <li><a href="drains.html">Drain cleaning and clearing</a></li>
            <li><a href="water-heaters.html">Water heater repair and replacement</a></li>
            <li><a href="garbage-disposals.html">Garbage disposal repair</a></li>
            <li><a href="piping-repiping.html">Pipe repair and repiping</a></li>
            <li><a href="sewers.html">Sewer line repair</a></li>
            <li><a href="leak-detection.html">Leak detection and repair</a></li>
            <li><a href="pumps.html">Pump repair and installation</a></li>
            <li><a href="emergency-plumbing.html">Emergency plumbing repairs</a></li>
          </ul>
          <p>Whether you're dealing with a slow drain, a damaged pipe, or a sudden plumbing emergency, we're here 24/7 to restore your home's comfort.</p>

          <h2>Why Homeowners Choose Benjamin Franklin Plumbing</h2>
          <p>More than half of homeowners say finding a reliable repair person is their biggest challenge. We remove that worry by offering a guaranteed service that prioritizes your needs. Our commitment includes these founding principles:</p>
          <ul class="service-benefits-list">
            <li><strong>Punctuality:</strong> We respect your time, so we arrive on time to scheduled appointments. If we're late, we will pay you $5 for every minute, up to a maximum of $300.</li>
            <li><strong>Straightforward pricing:</strong> We review all available repair options with you up front. No jargon, no hidden fees.</li>
            <li><strong>On-the-spot repairs:</strong> Our highly skilled certified technicians and fully stocked trucks allow us to complete most plumbing repairs on the first visit.</li>
            <li><strong>Skilled, trusted professionals:</strong> Every plumber undergoes meticulous checks and training to deliver high-quality service.</li>
            <li><strong>100% satisfaction guarantee:</strong> We stand behind our work because we want every customer to feel confident and protected.</li>
            <li><strong>Local service backed by a national brand:</strong> Our locally owned operations provide personal, community-focused service backed by the strength and reputation of North America's trusted plumbing brand.</li>
          </ul>

          <h2>What Our Plumbing Repair Process Looks Like</h2>
          <p>Here's what you can expect when you schedule a plumbing repair service from us:</p>
          <ul class="service-problems-list">
            <li><strong>Rapid response:</strong> Our service team arrives promptly to provide support for the client.</li>
            <li><strong>Accurate diagnosis:</strong> Certified technicians utilize advanced technology to assess the problem and provide a precise diagnosis of the issue.</li>
            <li><strong>Solution presentation:</strong> We create a detailed report of all problems identified during the inspection and present repair or replacement solutions tailored to your budget.</li>
            <li><strong>Repair services:</strong> Our experts perform the necessary repairs to ensure a quick resolution and prevent further damage.</li>
            <li><strong>Guaranteed satisfaction:</strong> Our work is covered by a 100% satisfaction guarantee.</li>
          </ul>

          <h2>Plumbing Repairs Done Right the First Time</h2>
          <p>Plumbing issues can be stressful, but getting them fixed shouldn't be. We provide honest guidance and reliable solutions, helping you feel confident about your home's plumbing again. You can count on us to respond quickly, diagnose accurately, communicate openly, treat your home with care, and deliver dependable, lasting repairs.</p>

          <div class="service-cta-box">
            <h2>Need Plumbing Repairs? We're Ready to Help.</h2>
            <p>Schedule a visit from The Punctual Plumber® and get expert plumbing repairs when you need them most. Call <a href="tel:4029228334">(402) 922-8334</a> today.</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="plumbing-inspection.html">Plumbing Inspection &amp; Diagnosis</a></li>
            <li><a href="plumbing-installation.html">Plumbing Installation</a></li>
            <li><a href="emergency-plumbing.html">Emergency Plumbing Services</a></li>
          </ul>

          <h2>Plumbing Repairs FAQs</h2>
""" + faq_block([
        (
            "How can I tell if I need plumbing repair?",
            "Aside from the most obvious signs like visible leaks or no water, watch for slow drains, discolored water, unusual odors, low water pressure, running toilets, and unexplained increases in your water bill. If you notice any of these, it's time to call a plumber.",
        ),
        (
            "Does homeowners insurance cover plumbing repairs?",
            "Most homeowners insurance will cover the structural damage caused by a sudden or unexpected plumbing issue (like a water heater causing a soaked basement), but not the service call to stop the leak. Review your policy or consult with your insurance provider to learn exactly what's covered.",
        ),
        (
            "What is the average cost of plumbing repairs?",
            "On average, plumbing repairs cost between $150–$500. However, your bill will depend on the repair type, labor needed, and whether your plumbing repair company charges by the hour or by the job. When you hire our experts, we'll assess the damage and provide you with a straightforward pricing guide before we even begin.",
        ),
        (
            "Can you tell me how to turn off the water for plumbing repairs?",
            "Locate your main shut-off valve (usually indoors in utility areas like your garage, laundry room, or basement, and near your water heater). If you can't find it indoors, check outside near the street or your water meter. Turn a gate valve clockwise until it stops, or turn a ball valve lever clockwise 90 degrees. Then run faucets on the lowest level until they're empty to relieve pressure.",
        ),
    ]),
}

# --- SHOWERS ---
PAGES["showers.html"] = {
    "title": "Shower Plumbing Services | Benjamin Franklin Plumbing Omaha",
    "meta": "Shower repair, installation, and replacement in Omaha. Licensed shower plumbers. Call (402) 922-8334.",
    "breadcrumb": "Showers",
    "label": "Showers",
    "h1": "Shower Plumbing Services",
    "hero": [
        "Whether you're dealing with everyday wear or planning a bathroom upgrade, getting your shower back to full function takes more than a quick fix.",
        "At Benjamin Franklin Plumbing® of Omaha, we handle everything from minor leaks and broken shower faucets to complete shower installations. Create a better shower experience — call us today to schedule service!",
    ],
    "cta_title": "Need Shower Service?",
    "cta_text": "Shower repair and installation in Omaha.",
    "body": """
          <h2>Our Comprehensive Shower Plumbing Services</h2>
          <p>Whatever part of your shower plumbing needs repair or installation, we have you covered. From faucets and valves to drains and water lines, our licensed plumbers handle every aspect of shower plumbing. We work with all shower types to ensure reliable performance, water efficiency, and a design that fits your space seamlessly.</p>

          <h3>Shower Repair</h3>
          <p>A broken shower can be more than an inconvenience — it can also cause damage to your home through leaks and pipe damage. When you hire our plumbers for shower repair, we'll fix the issue and help increase efficiency with eco-friendly low-flow or aerating showerheads.</p>
          <p>We handle all shower plumbing repairs, including bathtub and shower repair, water pressure fixes, faucet repair and replacement, showerhead repair and replacement, leaky pipes and fixtures, clogged drains, shower and tub retrofitting, water pipe relocation, low-flow showerheads and faucets, walk-in bathtub connections, and high-tech and green options. See our <a href="shower-repair.html">shower repair</a> page for details.</p>

          <h3>Shower Installation</h3>
          <p>New shower installations take proper plumbing, the right fixtures, and a precise fit to keep everything working smoothly. With so many sizes, styles, and materials available, you can truly customize your installation. Our experts simplify the process by evaluating your bathroom layout, plumbing system, and design goals to recommend the best shower solution for your space and budget. Learn more about our <a href="shower-installation.html">shower installation services</a>.</p>

          <h3>Shower Replacement</h3>
          <p>When replacing or remodeling your shower, we start by reviewing your current plumbing and layout. Our experts walk you through all available options that fit your space. If needed, we can re-pipe or adjust plumbing to support your new setup. Once your shower and plumbing are ready, we'll remove your old shower, install the new one, and test it to make sure it's working properly.</p>

          <h2>The Types of Showers We Service</h2>
          <p>We work with all brands and types of showers. From space-saving bathroom upgrades to versatile setups that enhance functionality, our solutions include:</p>
          <ul class="service-benefits-list">
            <li>Stand-up showers</li>
            <li>Bathtub and shower combos</li>
            <li>Hot tubs</li>
            <li>Whirlpool tubs</li>
            <li>Walk-in tubs</li>
          </ul>
          <p>Our residential shower services include shower plumbing installation, shower drain plumbing, shower vent plumbing, shower and tub plumbing, shower fixture plumbing, and outdoor shower plumbing.</p>

          <h2>Why Hire Benjamin Franklin Plumbing for Shower Services?</h2>
          <ul class="service-benefits-list">
            <li><strong>Quality plumbing and guarantees:</strong> We've built a loyal customer base through quality plumbing, industry-leading satisfaction guarantees, and straightforward pricing.</li>
            <li><strong>The Punctual Plumber®:</strong> We respect your time. If we're late, we pay you $5 per minute that you wait — up to $300.</li>
            <li><strong>24/7 emergency services:</strong> No after-hours fees, and we arrive with fully stocked vehicles for on-the-spot repairs.</li>
            <li><strong>Local expertise:</strong> Our plumbers live in the communities they serve, supporting them daily.</li>
          </ul>

          <div class="service-cta-box">
            <h2>Find Shower Plumbers Near You</h2>
            <p>Have a damaged shower, or looking to remodel yours altogether? Count on Benjamin Franklin Plumbing® of Omaha. Call <a href="tel:4029228334">(402) 922-8334</a> or request an appointment online to get started!</p>
            <a href="tel:4029228334" class="btn btn-primary btn-lg">Call Now</a>
          </div>

          <h2>Related Services</h2>
          <ul class="service-benefits-list">
            <li><a href="shower-repair.html">Shower Repair</a></li>
            <li><a href="shower-installation.html">Shower Installation</a></li>
            <li><a href="water-heaters.html">Water Heater Services</a></li>
            <li><a href="drain-cleaning.html">Drain Cleaning Services</a></li>
            <li><a href="bathtubs.html">Bathtub Services</a></li>
          </ul>

          <h2>Shower Service FAQs</h2>
""" + faq_block([
        (
            "Can you put shower plumbing on exterior walls?",
            "Technically, yes, but we don't recommend it. Placing plumbing pipes in exterior-facing walls can cause them to freeze and burst in cold climates. This can damage your pipes, home, and shower. When plumbing a shower, always hire an expert. At Benjamin Franklin Plumbing, we'll install all piping to suit your home and protect your plumbing long-term.",
        ),
        (
            "Can I use CPVC for shower plumbing?",
            "Yes. CPVC piping is a durable option that withstands high water temperatures and performs well in long-term shower plumbing. However, depending on where you live, building codes may restrict the use of CPVC pipes. That's why you should always hire a plumber when remodeling or installing a shower.",
        ),
        (
            "Can I use PEX for shower plumbing?",
            "Yes, PEX piping can be a great option for shower plumbing because it's flexible and doesn't sweat under high humidity. However, it may not be suitable for outdoor showers because UV rays can degrade PEX over time and compromise performance.",
        ),
        (
            "Can I use PVC for shower plumbing?",
            "PVC piping is cost-effective, lightweight, and resistant to corrosion, making it ideal for certain plumbing applications. It is suitable for the drain lines in your shower, but it isn't recommended for hot water supply lines. Our plumbers will help you choose the best piping materials based on safety, performance, and code compliance.",
        ),
    ]),
}


def patch_file(slug: str, cfg: dict) -> None:
    path = ROOT / "services" / slug
    content = path.read_text(encoding="utf-8")

    content = re.sub(r"<title>.*?</title>", f"<title>{cfg['title']}</title>", content, count=1)
    content = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{cfg["meta"]}">',
        content,
        count=1,
    )

    main = build_main(
        cfg["breadcrumb"],
        cfg["label"],
        cfg["h1"],
        cfg["hero"],
        cfg["body"],
        cfg["cta_title"],
        cfg["cta_text"],
        cfg.get("subhead"),
    )

    content = re.sub(
        r'  <main id="main-content".*?</main>',
        main,
        content,
        count=1,
        flags=re.DOTALL,
    )
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"updated {slug}")


if __name__ == "__main__":
    for slug in PAGES:
        patch_file(slug, PAGES[slug])
