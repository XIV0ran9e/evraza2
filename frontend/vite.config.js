import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '~': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
          @import '~/assets/styles/variables';
          @import '~/assets/styles/mixins';
          @import '~/assets/styles/typography';
        `,
      },
    },
  },
  server: {
    port: 3000,
  },
})
