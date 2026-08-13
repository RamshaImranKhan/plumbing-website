import type { Metadata } from 'next';
import { DM_Sans, Montserrat, Playfair_Display } from 'next/font/google';
import BodyLoaded from '@/components/BodyLoaded';
import SiteHeader from '@/components/SiteHeader';
import SiteFooter from '@/components/SiteFooter';
import PrivacyModal from '@/components/PrivacyModal';
import MobileCta from '@/components/MobileCta';
import BookingModal from '@/components/BookingModal';
import ClientScripts from '@/components/ClientScripts';
import './globals.css';

const dmSans = DM_Sans({
  subsets: ['latin'],
  variable: '--font-dm-sans',
  display: 'swap',
});

const montserrat = Montserrat({
  subsets: ['latin'],
  weight: ['600', '700', '800', '900'],
  variable: '--font-montserrat',
  display: 'swap',
});

const playfair = Playfair_Display({
  subsets: ['latin'],
  weight: ['700', '800'],
  variable: '--font-playfair',
  display: 'swap',
});

export const metadata: Metadata = {
  title: {
    default: 'Benjamin Franklin Plumbing® of Omaha',
    template: '%s',
  },
  description: 'Guaranteed plumbing repair services in Omaha & Council Bluffs. 24/7 emergency service.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${dmSans.variable} ${montserrat.variable} ${playfair.variable}`}>
      <body className={`${dmSans.className} ${playfair.className}`}>
        <BodyLoaded />
        <a href="#main-content" className="skip-link">
          Skip to main content
        </a>
        <SiteHeader />
        {children}
        <SiteFooter />
        <MobileCta />
        <div className="toast-container" id="toastLayer" aria-live="polite" />
        <PrivacyModal />
        <BookingModal />
        <ClientScripts />
      </body>
    </html>
  );
}
