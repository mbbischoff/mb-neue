export interface NavItem {
	href: string;
	label: string;
	icon: string;
}

export const navigation: NavItem[] = [
	{ href: '/', label: 'Home', icon: 'fa-home' },
	{ href: '/now', label: 'Now', icon: 'fa-clock' },
	{ href: '/archive', label: 'Archive', icon: 'fa-box-archive' },
	{ href: '/poems', label: 'Poems', icon: 'fa-feather' },
	{ href: '/about', label: 'About', icon: 'fa-user' },
	{ href: '/contact', label: 'Contact', icon: 'fa-envelope' },
]; 