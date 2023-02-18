<script setup>
import { AppHeader } from "~/components/app";
import { ElementLegend } from "~/components/elements";
</script>

<template>
  <div class="main">
    <app-header />
    <element-legend class="legend" />
  </div>
</template>

<style lang="scss" scoped>
.legend {
  margin-top: 60px;
}
</style>
