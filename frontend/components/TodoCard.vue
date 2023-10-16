<script setup lang="ts">
import { computed } from 'vue'
import { TodoPriority } from '@/interfaces/todo.interface'
import type { ITodo } from '@/interfaces/todo.interface'

const { todo } = defineProps<{
  todo: ITodo
}>()

defineEmits(['click'])

const priorityClass = computed(() => {
  switch (todo.priority) {
    case TodoPriority.HIGH:
      return 'bg-red-500 shadow-red-500'
    case TodoPriority.MEDIUM:
      return 'bg-yellow-500 shadow-yellow-500'
    case TodoPriority.LOW:
      return 'bg-green-500 shadow-green-500'
    default:
      return 'bg-neutral-500 shadow-neutral-500'
  }
})
</script>

<template>
  <div
    class="inline-block relative w-full mb-4 p-3 min-w-[20rem] break-inside-avoid bg-neutral-100 text-neutral-600 dark:bg-neutral-800 dark:text-neutral-200 rounded-md shadow-sm cursor-pointer hover:shadow-lg transition-all ease-in-out duration-300"
    @click="$emit('click')"
  >
    <div class="mb-2">
      <span
        class="inline-flex w-2 h-2 p-1 mr-1 mb-[2px] rounded-full shadow-sm"
        :class="priorityClass"
      />
      <span class="text-md">{{ todo.title }}</span>
    </div>
    <div v-if="todo.description" class="text-sm text-neutral-400">
      {{ todo.description }}
    </div>
  </div>
</template>
