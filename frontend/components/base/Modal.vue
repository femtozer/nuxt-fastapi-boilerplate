<script setup lang="ts">
const emit = defineEmits(['close'])

const modalBackground = ref()

function closeModal(e: Event): void {
  if (e.target === modalBackground.value)
    emit('close')
}
</script>

<template>
  <div
    ref="modalBackground"
    class="fixed w-full h-full p-6 top-0 left-0 bg-neutral-800/50 dark:bg-neutral-200/50 flex justify-center items-center"
    @click="closeModal"
  >
    <div
      class="rounded-md w-full max-w-2xl box-border p-6 bg-neutral-200 dark:bg-neutral-800"
    >
      <slot />
    </div>
  </div>
</template>
