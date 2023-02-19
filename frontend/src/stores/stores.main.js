import { defineStore } from 'pinia'

export const useStore = defineStore('main', {
  state: () => {
    return {
      theme: 'dark',
      data: null,
      enum: null
    }
  }
})
