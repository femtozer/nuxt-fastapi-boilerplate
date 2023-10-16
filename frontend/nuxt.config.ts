export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@pinia/nuxt', '@nuxtjs/i18n', '@nuxtjs/tailwindcss', '@nuxtjs/color-mode'],
  vite: {
    vue: {
      script: {
        defineModel: true,
        propsDestructure: true,
      },
    },
  },
  colorMode: {
    classSuffix: '',
  },
  runtimeConfig: {
    baseURL: 'http://localhost:8000/api',
    public: {
      baseURL: 'http://localhost:8000/api',
      appName: 'Todos',
    },
  },
})
