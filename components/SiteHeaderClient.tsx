'use client';

import { useEffect, useRef } from 'react';
import { usePathname } from 'next/navigation';
import { applyActiveNav } from '@/lib/nav';

type SiteHeaderClientProps = {
  html: string;
};

export default function SiteHeaderClient({ html }: SiteHeaderClientProps) {
  const pathname = usePathname();
  const rootRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    applyActiveNav(pathname, rootRef.current ?? document);
  }, [pathname]);

  return (
    <div
      ref={rootRef}
      suppressHydrationWarning
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
