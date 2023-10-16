let clickOutsideEvent: (this: HTMLElement, ev: any) => any

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.directive('click-outside', {
    beforeMount(el, binding) {
      clickOutsideEvent = (event) => {
        if (el !== event.target && !el.contains(event.target))
          binding.value(event)
      }
      window.addEventListener('click', clickOutsideEvent)
    },
    unmounted() {
      window.removeEventListener('click', clickOutsideEvent)
    },
  })
})
