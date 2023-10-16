<script setup lang="ts">
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useMainStore } from '@/stores/todos'
import { TodoPriority } from '@/interfaces/todo.interface'
import type { ITodo } from '@/interfaces/todo.interface'

const store = useMainStore()
const { loading, todos } = storeToRefs(store)
const modalTodo = ref()
const showModal = ref(false)
store.getTodos()

function newTodo(): void {
  modalTodo.value = {
    title: '',
    description: '',
    priority: TodoPriority.LOW,
  }
  showModal.value = true
}

function editTodo(todo: ITodo): void {
  modalTodo.value = todo
  showModal.value = true
}

function submitTodo(todo: ITodo): void {
  if (todo) {
    if (todo.id)
      store.putTodo(todo)
    else
      store.postTodo(todo)
  }

  showModal.value = false
}

function deleteTodo(todo: ITodo): void {
  if (todo && todo.id)
    store.deleteTodo(todo)

  showModal.value = false
}
</script>

<template>
  <div class="flex flex-col justify-center">
    <div v-show="loading" class="w-full">
      <BaseLinearProgress />
    </div>
    <div v-show="!loading" class="w-full h-1" />
    <div class="w-full p-4">
      <button
        class="w-full py-2 mb-4 rounded-md flex justify-center text-neutral-600 dark:text-neutral-200 hover:bg-neutral-100 dark:hover:bg-neutral-800 transition-all duration-300 hover:shadow-md"
        @click="newTodo"
      >
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
            d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
      </button>
      <div class="columns-xs">
        <TodoCard
          v-for="todo in todos"
          :key="todo.id"
          :todo="todo"
          @click="editTodo(todo)"
        />
      </div>
      <BaseModal v-if="showModal" @close="submitTodo">
        <TodoForm :todo="modalTodo" @submit="submitTodo" @delete="deleteTodo" />
      </BaseModal>
    </div>
  </div>
</template>
