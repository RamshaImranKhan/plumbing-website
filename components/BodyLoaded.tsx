'use client';

import { useEffect } from 'react';

export default function BodyLoaded() {
  useEffect(() => {
    document.body.classList.add('is-loaded');
  }, []);

  return null;
}
