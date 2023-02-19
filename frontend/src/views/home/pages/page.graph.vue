<script setup>
import { AppHeader, AppFilter } from "~/components/app";
</script>

<template>
  <div class="main">
    <app-header class="header" />
    <app-filter class="filter" />
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
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "sidebar contentt";
}

.header {
  grid-area: header;
}

.filter {
  grid-area: sidebar;
}

.content {
  grid-area: contentt;
}
</style>
