<script setup lang="ts">
import { computed } from 'vue'

const { outline = false } = defineProps<{ outline?: boolean }>()

defineEmits(['click'])

const buttonClass = computed(() => {
  return outline
    ? 'bg-transparent border-neutral-800 text-neutral-600 hover:bg-neutral-800 hover:text-neutral-200 dark:border-neutral-200 dark:text-neutral-200 dark:hover:bg-neutral-200 dark:hover:text-neutral-600'
    : 'bg-neutral-800 text-neutral-200 border-neutral-800 hover:bg-neutral-700 hover:border-neutral-700 dark:bg-neutral-200 dark:text-neutral-600 dark:border-neutral-200 dark:hover:bg-neutral-300 dark:hover:border-neutral-300'
})
</script>

<template>
  <button
    class="px-3 py-1 rounded-md cursor-pointer border-[1px] hover:shadow-md transition duration-300"
    :class="buttonClass"
    @click="$emit('click')"
  >
    <div class="flex justify-center">
      <slot />
    </div>
  </button>
</template>
