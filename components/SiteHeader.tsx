import { getHeaderHtml } from '@/lib/templates';
import SiteHeaderClient from '@/components/SiteHeaderClient';

export default function SiteHeader() {
  return <SiteHeaderClient html={getHeaderHtml(null)} />;
}
