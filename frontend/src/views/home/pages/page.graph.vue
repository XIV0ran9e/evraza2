<script setup>
import { AppHeader, AppFilter } from "~/components/app";
</script>

<template>
  <div class="main">
    <app-header class="header" />
    <app-AppFilter class="filter" />
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 4fr;
  grid-template-areas:
    "header header"
    "sidebar content";
}

.header {
  grid-area: header;
}

.filter {
  grid-area: sidebar;
  align-self: center;
}

.content {
  grid-area: content;
}
</style>
