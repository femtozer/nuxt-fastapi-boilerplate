import { twMerge } from 'tailwind-merge'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.directive('tw-merge', {
    mounted(el) {
      el.className = twMerge(el.className)
    },
    updated(el) {
      el.className = twMerge(el.className)
    },
  })
})
