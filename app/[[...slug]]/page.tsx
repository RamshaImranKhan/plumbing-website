import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import LegacyPageContent from '@/components/LegacyPageContent';
import { getAllRoutes, getPage } from '@/lib/content';

type PageProps = {
  params: Promise<{ slug?: string[] }>;
};

function slugToRoute(slug?: string[]): string {
  if (!slug || slug.length === 0) return '/';
  return `/${slug.join('/')}`;
}

export async function generateStaticParams() {
  return getAllRoutes()
    .filter((route) => route !== '/')
    .map((route) => ({ slug: route.slice(1).split('/') }));
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const page = getPage(slugToRoute(slug));
  if (!page) return {};
  return { title: page.title, description: page.description };
}

export default async function Page({ params }: PageProps) {
  const { slug } = await params;
  const route = slugToRoute(slug);
  const page = getPage(route);
  if (!page) notFound();

  return (
    <>
      {page.jsonLd ? (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: page.jsonLd }} />
      ) : null}
      <LegacyPageContent html={page.content} />
    </>
  );
}
