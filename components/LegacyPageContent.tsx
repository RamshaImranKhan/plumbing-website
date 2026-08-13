type LegacyPageContentProps = {
  html: string;
};

export default function LegacyPageContent({ html }: LegacyPageContentProps) {
  return (
    <main
      id="main-content"
      suppressHydrationWarning
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
