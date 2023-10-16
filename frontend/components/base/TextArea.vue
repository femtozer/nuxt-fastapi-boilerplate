<script setup lang="ts">
const value = defineModel<string>()
</script>

<template>
  <textarea
    v-model="value"
    class="rounded-md p-3 bg-transparent text-neutral-600 dark:text-neutral-200 border-neutral-400 border-2 outline-2 outline-neutral-800 dark:outline-neutral-200"
  />
</template>
