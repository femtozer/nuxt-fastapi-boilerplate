<script setup lang="ts">
import { ref } from 'vue'
import type { ITodo } from '@/interfaces/todo.interface'
import { TodoPriority } from '@/interfaces/todo.interface'

const { todo } = defineProps<{ todo: ITodo }>()

const emit = defineEmits(['submit', 'delete'])

const { t } = useI18n()

// deep copy todo to edit
const todoForm = ref<ITodo>(JSON.parse(JSON.stringify(todo)))
const showInvalid = ref(false)

const priorityNames = Object.values(TodoPriority)

function checkAndSubmit(): void {
  if (!todoForm.value.title)
    showInvalid.value = true
  else
    emit('submit', todoForm.value)
}

function deleteTodo(): void {
  emit('delete', todoForm.value)
}

function priorityLabel(priority?: string | object): string {
  return t(`todos.model.priority.values.${priority?.toString().toLowerCase()}`).toUpperCase()
}
</script>

<template>
  <div class="flex flex-col">
    <h2 class="mb-6">
      {{ todo.id ? $t('todos.edit') : $t('todos.new') }}
    </h2>
    <h3>{{ $t('todos.model.title') }}</h3>
    <BaseInput
      v-model="todoForm.title"
      :placeholder="$t('todos.model.title')"
      :show-invalid="showInvalid"
      required
      class="mb-3"
    />
    <h3>{{ $t('todos.model.description') }}</h3>
    <BaseTextArea
      v-model="todoForm.description"
      :placeholder="$t('todos.model.description')"
      class="mb-3"
    />
    <h3>{{ $t('todos.model.priority.label') }}</h3>
    <BaseDropdown
      v-model="todoForm.priority"
      :options="priorityNames"
      button-class="text-neutral-600 bg-neutral-200 hover:bg-neutral-300 dark:text-white dark:bg-neutral-800 dark:hover:bg-neutral-700"
      :label-property="priorityLabel"
    />
    <div class="flex justify-between mt-8">
      <div>
        <BaseButton class="mr-2" @click="checkAndSubmit">
          {{
            $t('actions.save')
          }}
        </BaseButton>
        <BaseButton outline @click="$emit('submit')">
          {{
            $t('actions.cancel')
          }}
        </BaseButton>
      </div>
      <BaseButton
        v-if="todoForm.id"
        class="!bg-red-500 !text-neutral-200 !border-red-500"
        @click="deleteTodo"
      >
        {{ $t('actions.delete') }}
      </BaseButton>
    </div>
  </div>
</template>
