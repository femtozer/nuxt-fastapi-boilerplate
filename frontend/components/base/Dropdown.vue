<script setup lang="ts">
import { ref } from 'vue'

export interface Props {
  options: any[]
  buttonClass?: string
  labelProperty?: (value: any) => string
  valueProperty?: (value: any) => any
}

const {
  options,
  buttonClass = '',
  labelProperty = (value: any) => value.toString(),
  valueProperty = (value: any) => value,
} = defineProps<Props>()

const value = defineModel<string>()

const selectedOption = ref(optionFromValue(value.value))
const showValues = ref(false)

function selectOption(option: any): void {
  selectedOption.value = option
  value.value = valueProperty(option)
}

function optionFromValue(value: any): void {
  return options.find(o => valueProperty(o) === value)
}
</script>

<template>
  <div v-click-outside="() => showValues = false" class="w-fit">
    <!-- Dropdown button -->
    <button
      id="dropdownButton"
      v-tw-merge
      class="font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center transition duration-300 text-neutral-600 bg-neutral-100 hover:bg-neutral-200 dark:text-white dark:bg-neutral-800 dark:hover:bg-neutral-700" :class="[
        buttonClass,
      ]"
      type="button"
      @click="() => showValues = !showValues"
    >
      <span>{{ labelProperty(selectedOption) }}</span>
      <svg
        class="ml-2 w-4 h-4"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 9l-7 7-7-7"
        />
      </svg>
    </button>

    <!-- Dropdown menu -->
    <div
      v-if="showValues"
      class="absolute z-10 w-44 text-base list-none bg-white rounded divide-y divide-neutral-100 shadow dark:bg-neutral-700"
      @click="() => showValues = !showValues"
    >
      <ul class="py-1" aria-labelledby="dropdownButton">
        <li v-for="option in options" :key="labelProperty(option)">
          <div
            class="block cursor-pointer py-2 px-4 text-sm text-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-600 dark:text-neutral-200 dark:hover:text-white"
            @click="selectOption(option)"
          >
            {{ labelProperty(option) }}
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
