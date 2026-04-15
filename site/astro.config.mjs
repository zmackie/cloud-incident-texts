import { defineConfig } from "astro/config";

export default defineConfig({
  output: "static",
  // GitHub Pages project site deploys to /<repo-name>/
  // Change to "/" if using a custom domain or organisation root page.
  base: "/cloud-incident-texts",
});
