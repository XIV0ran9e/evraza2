<script setup></script>

<template>
  <div class="layout theme-dark">
    <slot />
  </div>
</template>

<style scoped lang="scss">
.layout {
  min-height: 100vh;
  background: var(--main-bg);
}
</style>
