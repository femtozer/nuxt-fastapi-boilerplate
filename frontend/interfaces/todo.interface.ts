export enum TodoPriority {
  LOW = 'LOW',
  MEDIUM = 'MEDIUM',
  HIGH = 'HIGH',
}

export interface ITodo {
  id?: number
  title: string
  description: string
  priority: TodoPriority
  createdAt?: Date
  updatedAt?: Date
}
