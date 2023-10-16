<script setup lang="ts">
defineProps<{ showInvalid: boolean }>()

const value = defineModel<string>()
</script>

<template>
  <input
    v-model="value"
    type="text"
    class="rounded-md p-3 bg-transparent text-neutral-600 dark:text-neutral-200 border-neutral-400 border-2 outline-2 outline-neutral-800 dark:outline-neutral-200"
    :class="{ 'invalid:border-red-500': showInvalid }"
  >
</template>
