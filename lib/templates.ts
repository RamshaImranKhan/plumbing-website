import fs from 'fs';
import path from 'path';

function readInclude(name: string): string {
  return fs.readFileSync(path.join(process.cwd(), 'includes', name), 'utf8');
}

function stripHtmlExtension(html: string): string {
  return html
    .replace(/href="([^"]+)\.html([^"]*)"/g, (match, linkPath, hash) => {
      if (
        linkPath.startsWith('http') ||
        linkPath.startsWith('tel:') ||
        linkPath.startsWith('mailto:') ||
        linkPath.startsWith('#')
      ) {
        return match;
      }
      return `href="${linkPath}${hash}"`;
    })
    .replace(/href="services\/index"/g, 'href="/services"')
    .replace(/href="\/services\/index"/g, 'href="/services"');
}

function applyPlaceholders(html: string, active: 'services' | 'resources' | 'about' | null): string {
  return stripHtmlExtension(
    html
      .replace(/\{\{HOME\}\}/g, '/')
      .replace(/\{\{ROOT\}\}/g, '/')
      .replace(/\{\{SVC\}\}/g, '/services/')
      .replace(/\{\{RES\}\}/g, '/resources/')
      .replace(/\{\{AREAS\}\}/g, '/#areas')
      .replace(/\{\{QUOTE\}\}/g, '/#book')
      .replace(/\{\{LOC\}\}/g, '/services')
      .replace(/\{\{ACTIVE_SERVICES\}\}/g, active === 'services' ? ' bfp-nav-btn-active' : '')
      .replace(/\{\{ACTIVE_RESOURCES\}\}/g, active === 'resources' ? ' bfp-nav-btn-active' : '')
      .replace(/\{\{ACTIVE_ABOUT\}\}/g, active === 'about' ? ' bfp-nav-btn-active' : ''),
  );
}

export function getHeaderHtml(active: 'services' | 'resources' | 'about' | null = null): string {
  return applyPlaceholders(readInclude('site-header.html'), active);
}

export function getFooterGridHtml(): string {
  return applyPlaceholders(readInclude('site-footer-grid.html'), null);
}

export function getFooterBottomHtml(): string {
  return applyPlaceholders(readInclude('site-footer-bottom.html'), null);
}

export function getPrivacyModalHtml(): string {
  return applyPlaceholders(readInclude('privacy-consent-modal.html'), null);
}
