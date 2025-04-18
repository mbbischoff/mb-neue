export interface NavItem {
  href: string;
  label: string;
  icon?: string;
  hideInHeader?: boolean;
}

export const navigation: NavItem[] = [
  { href: '/', label: 'Home', icon: 'fas fa-home', hideInHeader: true },
  { href: '/now', label: 'Now', icon: 'fas fa-clock' },
  { href: '/archive', label: 'Then', icon: 'fas fa-hourglass-end' },
  { href: '/poems', label: 'Poems', icon: 'fas fa-pen-fancy' },
  { href: '/about', label: 'About', icon: 'fas fa-venus' },
  { href: '/contact', label: 'Contact', icon: 'fas fa-hand-peace' },
];
