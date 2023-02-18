<script setup>
import LayoutDefault from '~/layout/default.vue'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const layouts = {
  default: LayoutDefault,
}

const route = useRoute()
const computedLayout = computed(() => {
  return layouts[route.meta.layout || 'default']
})
</script>

<template>
  <component :is="computedLayout">
    <router-view />
  </component>
</template>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
