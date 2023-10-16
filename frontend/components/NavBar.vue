<script setup lang="ts">
import { ref } from 'vue'

const config = useRuntimeConfig()
const colorMode = useColorMode()
const appName = ref(config.public.appName)
const darkMode = ref(colorMode.preference === 'dark')

function setDarkMode(event: Event) {
  colorMode.preference = (event.target as HTMLInputElement).checked ? 'dark' : 'light'
  darkMode.value = colorMode.preference === 'dark'
}
</script>

<template>
  <nav
    class="fixed z-10 h-16 w-full px-5 gap-x-4 box-border bg-neutral-100 text-neutral-600 dark:bg-neutral-800 dark:text-neutral-200 flex items-center justify-between shadow-sm transition-colors duration-300"
  >
    <h1 class="mb-0 flex-auto">
      {{ appName }}
    </h1>
    <LanguagePicker />
    <BaseSlideToggle v-model="darkMode" @input="setDarkMode">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
        />
      </svg>
    </BaseSlideToggle>
  </nav>
</template>
