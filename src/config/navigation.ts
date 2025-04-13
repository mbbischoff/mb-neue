export interface NavItem {
  href: string;
  label: string;
  icon: string;
}

export const navigation = [
  { href: '/', label: 'Home' },
  { href: '/now', label: 'Now' },
  { href: '/archive', label: 'Archive' },
  { href: '/poems', label: 'Poems' },
  { href: '/about', label: 'About' },
  { href: '/contact', label: 'Contact' },
];
