export interface NavItem {
	href: string;
	label: string;
	icon: string;
}

export const navigation: NavItem[] = [
	{ href: '/', label: 'Home', icon: 'fa-regular fa-home' },
	{ href: '/now', label: 'Now', icon: 'fa-regular fa-clock' },
	{ href: '/archive', label: 'Archive', icon: 'fa-regular fa-box-archive' },
	{ href: '/poems', label: 'Poems', icon: 'fa-regular fa-feather' },
	{ href: '/about', label: 'About', icon: 'fa-regular fa-user' },
	{ href: '/contact', label: 'Contact', icon: 'fa-regular fa-envelope' },
]; 