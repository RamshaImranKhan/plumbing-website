export {};

declare global {
  interface Window {
    initApp?: () => void;
  }
}
