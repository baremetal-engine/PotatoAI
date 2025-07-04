import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [
    svelte({
      compilerOptions: {
        // 👇 enables legacy Svelte 3/4 instantiation style
        compatibility: {
          componentApi: 4,
        },
      },
    }),
  ],
  root: './ui',
});
