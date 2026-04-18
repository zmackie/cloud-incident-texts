import { defineConfig } from "astro/config";

// Base path is deploy-target dependent:
//   - GitHub Pages project site serves at /<repo-name>/    → /cloud-incident-texts
//   - Cloudflare Pages / custom domain root                → /
// The deploy workflow exports SITE_BASE; default matches the GitHub Pages setup.
const base = process.env.SITE_BASE ?? "/cloud-incident-texts";

export default defineConfig({
  output: "static",
  base,
});
