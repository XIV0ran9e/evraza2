import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '~/views/home'

export default createRouter({
  history: createWebHistory(),
  routes: [...HomeView],
})
