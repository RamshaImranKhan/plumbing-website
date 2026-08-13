import { getPrivacyModalHtml } from '@/lib/templates';

export default function PrivacyModal() {
  return <div suppressHydrationWarning dangerouslySetInnerHTML={{ __html: getPrivacyModalHtml() }} />;
}
