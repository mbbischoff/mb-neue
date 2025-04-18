export interface SocialLink {
  href: string;
  rel?: string;
  target?: string;
  ariaLabel: string;
  icon: string;
  label: string;
}

export const socialLinks: SocialLink[] = [
  {
    href: "https://twitter.com/yourusername",
    rel: "me",
    target: "_blank",
    ariaLabel: "X (Twitter)",
    icon: "fa-brands fa-x-twitter",
    label: "twitter"
  },
  {
    href: "https://bsky.app/profile/yourusername",
    rel: "me",
    target: "_blank",
    ariaLabel: "Bluesky",
    icon: "fa-brands fa-bluesky",
    label: "bluesky"
  },
  {
    href: "https://mastodon.social/@yourusername",
    rel: "me",
    target: "_blank",
    ariaLabel: "Mastodon",
    icon: "fa-brands fa-mastodon",
    label: "mastodon"
  },
  {
    href: "https://instagram.com/yourusername",
    target: "_blank",
    ariaLabel: "Instagram",
    icon: "fa-brands fa-instagram",
    label: "instagram"
  },
  {
    href: "https://github.com/yourusername",
    target: "_blank",
    ariaLabel: "GitHub",
    icon: "fa-brands fa-github",
    label: "github"
  },
  {
    href: "https://letterboxd.com/yourusername",
    target: "_blank",
    ariaLabel: "Letterboxd",
    icon: "fa-brands fa-letterboxd",
    label: "letterboxd"
  }
]; 