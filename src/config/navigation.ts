export interface NavItem {
  href: string;
  label: string;
  icon?: string;
  hideInHeader?: boolean;
}

export const navigation: NavItem[] = [
  { href: '/', label: '⌂︎ Home', hideInHeader: true },
  { href: '/now', label: '⌚︎ Now' },
  { href: '/archive', label: '⌛︎ Then' },
  { href: '/poems', label: '⁂ Poems' },
  { href: '/about', label: '♀ About' },
  { href: '/contact', label: '✉︎ Contact' },
];
