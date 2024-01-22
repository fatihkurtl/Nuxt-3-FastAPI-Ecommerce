// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      // appUrl: process.env.NUXT_PUBLIC_APP_URL ?? 'http://localhost:3000',
      apiUrl: process.env.NUXT_PUBLIC_API_BASE_URL ?? 'http://127.0.0.1:8000',
    },
  },
  modules: [
    '@pinia/nuxt',
    '@pinia-plugin-persistedstate/nuxt',
  ],
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap' },
      ],
      script: [
        { src: 'js/bootstrap.bundle.min.js' },
        { src: 'js/custom.js' },
        { src: 'js/tiny-slider.js' },
      ]
    },
  },
  css: [
    '~/assets/css/bootstrap.min.css',
    '~/assets/css/style.css',
    '~/assets/css/tiny-slider.css',
    '~/assets/scss/style.scss',
    '@fortawesome/fontawesome-svg-core/styles.css',
  ],
})
