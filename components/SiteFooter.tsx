import { getFooterBottomHtml, getFooterGridHtml } from '@/lib/templates';

export default function SiteFooter() {
  return (
    <footer className="site-footer">
      <div suppressHydrationWarning dangerouslySetInnerHTML={{ __html: getFooterGridHtml() }} />
      <div suppressHydrationWarning dangerouslySetInnerHTML={{ __html: getFooterBottomHtml() }} />
    </footer>
  );
}
