import fs from 'fs';
import path from 'path';

export type PageContent = {
  title: string;
  description: string;
  content: string;
  jsonLd: string | null;
};

const CONTENT = path.join(process.cwd(), 'content');
let cache: Map<string, PageContent> | null = null;

function routeToCandidates(route: string): string[] {
  if (route === '/') return [path.join(CONTENT, 'index.html')];
  const segments = route.split('/').filter(Boolean);
  const joined = path.join(CONTENT, ...segments);
  return [path.join(joined, 'index.html'), `${joined}.html`];
}

function extractTitle(html: string) {
  return html.match(/<title>([^<]*)<\/title>/i)?.[1]?.trim() ?? '';
}

function extractDescription(html: string) {
  return html.match(/<meta\s+name="description"\s+content="([^"]*)"/i)?.[1]?.trim() ?? '';
}

function extractMain(html: string) {
  return html.match(/<main[^>]*>([\s\S]*)<\/main>/i)?.[1]?.trim() ?? '';
}

function extractJsonLd(html: string) {
  return html.match(/<script type="application\/ld\+json">\s*([\s\S]*?)\s*<\/script>/i)?.[1]?.trim() ?? null;
}

function routeBase(route: string) {
  if (route === '/') return '';
  const parts = route.split('/').filter(Boolean);
  parts.pop();
  return parts.length ? `/${parts.join('/')}` : '';
}

function rewriteHtml(html: string, route: string) {
  let result = html;
  result = result.replace(/src="\.\.\/assets\//g, 'src="/assets/');
  result = result.replace(/src="\.\.\/\.\.\/assets\//g, 'src="/assets/');
  result = result.replace(/src="assets\//g, 'src="/assets/');
  result = result.replace(/href="\.\.\/assets\//g, 'href="/assets/');
  result = result.replace(/href="\.\.\/\.\.\/assets\//g, 'href="/assets/');
  result = result.replace(/href="\.\.\/index\.html/g, 'href="/');
  result = result.replace(/href="index\.html/g, 'href="/');
  result = result.replace(/href="\.\.\/services\/index\.html/g, 'href="/services');
  result = result.replace(/href="services\/index\.html/g, 'href="/services');
  result = result.replace(/href="\.\.\/services\//g, 'href="/services/');
  result = result.replace(/href="services\//g, 'href="/services/');
  result = result.replace(/href="\.\.\/resources\//g, 'href="/resources/');
  result = result.replace(/href="resources\//g, 'href="/resources/');
  result = result.replace(/href="([^"]*)\.html([^"]*)"/g, (match, linkPath, hash) => {
    if (linkPath.startsWith('http') || linkPath.startsWith('tel:') || linkPath.startsWith('mailto:')) return match;
    if (linkPath.startsWith('/') || linkPath.startsWith('#')) return `href="${linkPath}${hash}"`;
    const base = routeBase(route);
    const normalized = linkPath.startsWith('../')
      ? `/${linkPath.replace(/^(\.\.\/)+/, '')}`
      : `${base}/${linkPath}`.replace(/\/+/g, '/');
    return `href="${normalized}${hash}"`;
  });
  return result;
}

function loadPage(route: string): PageContent | null {
  for (const filePath of routeToCandidates(route)) {
    if (!fs.existsSync(filePath)) continue;
    const html = fs.readFileSync(filePath, 'utf8');
    return {
      title: extractTitle(html),
      description: extractDescription(html),
      content: rewriteHtml(extractMain(html), route),
      jsonLd: extractJsonLd(html),
    };
  }
  return null;
}

function walkHtml(dir: string, base = ''): string[] {
  const routes: string[] = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const rel = base ? `${base}/${entry.name}` : entry.name;
    if (entry.isDirectory()) {
      routes.push(...walkHtml(path.join(dir, entry.name), rel));
    } else if (entry.name.endsWith('.html')) {
      let route = rel.replace(/\\/g, '/').replace(/\.html$/, '');
      if (route === 'index') route = '';
      else if (route.endsWith('/index')) route = route.slice(0, -6);
      routes.push(route ? `/${route}` : '/');
    }
  }
  return routes;
}

export function getAllRoutes(): string[] {
  return walkHtml(CONTENT);
}

export function getPage(route: string): PageContent | null {
  if (!cache) {
    cache = new Map();
    for (const r of getAllRoutes()) cache.set(r, loadPage(r)!);
  }
  return cache.get(route) ?? loadPage(route);
}
