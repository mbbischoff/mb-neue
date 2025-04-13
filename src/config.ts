export const SITE_TITLE = 'mb bischoff';
export const SITE_TITLE_SHORT = 'mb';
export const SITE_DESCRIPTION = 'mb bischoff (she/they) makes apps, posts, & podcasts.';

export interface NavItem {
  href: string;
  label: string;
  icon?: string;
}

export const navigation: NavItem[] = [
  { href: '/', label: '⌂︎ Home' },
  { href: '/now', label: '⌚︎ Now' },
  { href: '/archive', label: '⊞︎ Then' },
  { href: '/poems', label: '⁂ Poems' },
  { href: '/about', label: '♀ About' },
  { href: '/contact', label: '✉︎ Contact' },
];
