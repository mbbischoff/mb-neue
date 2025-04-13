# MB Neue - Personal Website

A modern, accessible personal website built with Astro.

## Features:

- ✅ Minimal, clean design
- ✅ Fully responsive layout
- ✅ Excellent accessibility (WCAG compliant)
- ✅ Dark/light mode support
- ✅ Optimized font loading
- ✅ SEO-friendly with canonical URLs and OpenGraph data
- ✅ RSS Feed support
- ✅ Markdown & MDX support for blog posts and poems
- ✅ Code quality tools (ESLint, TypeScript, Prettier)

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
├── public/
├── src/
│   ├── components/
│   ├── content/
│   ├── layouts/
│   └── pages/
├── astro.config.mjs
├── README.md
├── package.json
└── tsconfig.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

The `src/content/` directory contains "collections" of related Markdown and MDX documents. Use `getCollection()` to retrieve posts from `src/content/blog/`, and type-check your frontmatter using an optional schema. See [Astro's Content Collections docs](https://docs.astro.build/en/guides/content-collections/) to learn more.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run lint`            | Runs ESLint to check code quality                |
| `npm run typecheck`       | Runs TypeScript type checking                    |
| `npm run format`          | Formats code with Prettier                       |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 🔍 Accessibility Features

This project includes several accessibility enhancements:

- Skip-to-content link for keyboard navigation
- Proper ARIA attributes for navigation elements
- Semantic HTML structure
- Color contrast that meets WCAG standards
- Focus styles for keyboard navigation
- Proper alt text for images
- Responsive design for all screen sizes

## 🛠️ Development

The project uses several tools to ensure code quality:

- **ESLint**: Linting for JavaScript/TypeScript
- **TypeScript**: Static type checking
- **Prettier**: Code formatting

## 📄 License

This project is licensed under Creative Commons Attribution-ShareAlike 4.0.

## Credits

Originally built with the Astro Blog template.
