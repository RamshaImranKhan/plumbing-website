'use client';

import Script from 'next/script';

export default function ClientScripts() {
  return (
    <Script
      src="/app.js"
      strategy="afterInteractive"
      onLoad={() => {
        if (typeof window.initApp === 'function') window.initApp();
      }}
    />
  );
}
