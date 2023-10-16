import { defineStore } from 'pinia'
import type { ITodo } from '../interfaces/todo.interface'
import type { IPage } from '@/interfaces/page.interface'

export const useMainStore = defineStore('todos', {
  state: () => ({
    todos: [] as ITodo[],
    loading: false,
  }),
  actions: {
    async getTodos() {
      this.loading = true
      const { data, error } = await useBaseURLFetch<IPage<ITodo>>('/todos?sort=updatedAt&is_desc=true')

      if (error.value)
        console.error(error.value)
      else
        this.todos = data.value?.items ?? []

      this.loading = false
    },
    async postTodo(todo: ITodo) {
      this.loading = true
      const { error } = await useBaseURLFetch<ITodo>('/todos', { method: 'POST', body: todo })

      if (error.value)
        console.error(error.value)
      else
        this.getTodos()

      this.loading = false
    },
    async putTodo(todo: ITodo) {
      this.loading = true
      const { error } = await useBaseURLFetch<ITodo>(`/todos/${todo.id}`, { method: 'PUT', body: todo })

      if (error.value)
        console.error(error.value)
      else
        this.getTodos()

      this.loading = false
    },
    async deleteTodo(todo: ITodo) {
      this.loading = true
      const { error } = await useBaseURLFetch(`/todos/${todo.id}`, { method: 'DELETE', body: todo })

      if (error.value)
        console.error(error.value)
      else
        this.getTodos()

      this.loading = false
    },
  },
})
