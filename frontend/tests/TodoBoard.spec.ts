import { describe, expect, it } from 'vitest'
import { mount } from '@vue/test-utils'
import { createTestingPinia } from '@pinia/testing'
import { faker } from '@faker-js/faker'
import TodoBoard from '@/components/TodoBoard.vue'
import TodoCard from '@/components/TodoCard.vue'
import TodoForm from '@/components/TodoForm.vue'
import LinearProgress from '@/components/base/LinearProgress.vue'
import Modal from '@/components/base/Modal.vue'
import type { ITodo } from '@/interfaces/todo.interface'
import { TodoPriority } from '@/interfaces/todo.interface'

describe('component TodoBoard', () => {
  it('should create', async () => {
    const todosLength = faker.number.int(20)
    const testingPinia = createTestingPinia({
      initialState: {
        todos: {
          loading: false,
          todos: Array.from({ length: todosLength }, () => (
            {
              id: faker.string.uuid(),
              title: faker.lorem.sentence(),
              description: faker.lorem.paragraph(),
              priority: faker.helpers.arrayElement(Object.values(TodoPriority)),
              createdAt: faker.date.past(),
              updatedAt: faker.date.past(),
            }
          ) as ITodo),
        },
      },
    })
    const wrapper = mount(TodoBoard, {
      global: {
        plugins: [testingPinia],
        components: {
          TodoCard,
          TodoForm,
          BaseLinearProgress: LinearProgress,
          BaseModal: Modal,
        },
      },
    })
    expect(wrapper.vm).toBeTruthy()
    const todos = wrapper.findAllComponents(TodoCard)
    expect(todos).toHaveLength(todosLength)
  })
})
