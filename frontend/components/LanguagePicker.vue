<script setup lang="ts">
const { locale } = useI18n()
const locales = [
  {
    code: 'en',
    name: 'English',
  },
  {
    code: 'fr',
    name: 'Français',
  },
]
</script>

<template>
  <BaseDropdown
    v-model="locale"
    :options="locales"
    button-class="text-neutral-600 bg-neutral-100 hover:bg-neutral-200 dark:text-white dark:bg-neutral-800 dark:hover:bg-neutral-700"
    :label-property="(value) => value?.name"
    :value-property="(value) => value?.code"
  />
</template>
