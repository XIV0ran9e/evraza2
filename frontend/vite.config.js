import { fileURLToPath, URL } from 'url'
import { VitePluginFonts } from 'vite-plugin-fonts'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: { isCustomElement: (tag) => tag.startsWith('xaf-') },
      },
    }),
    VitePluginFonts({
      google: {
        families: [
          { name: 'Manrope', styles: 'wght@200;300;400;500;600;700;800' },
          {
            name: 'Poppins',
            styles: 'wght@100;200;300;400;500;600;700;800;900',
          },
        ],
      },
    }),
  ],
  resolve: {
    alias: {
      '~': fileURLToPath(new URL('./src', import.meta.url)),
      process: 'process/browser',
      stream: 'stream-browserify',
      zlib: 'browserify-zlib',
      util: 'util',
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
          @import '~/assets/styles/variables';
          @import '~/assets/styles/mixins';
          @import '~/assets/styles/mixins/adaptivity-mixins';
          @import '~/assets/styles/typography';
        `,
      },
    },
  },
  server: {
    port: 3000,
  },
})
