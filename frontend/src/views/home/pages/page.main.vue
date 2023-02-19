<script setup>
import { AppHeader } from "~/components/app";
import { ElementLegend, ElementAgloworkers } from "~/components/elements";
</script>

<template>
  <div class="main">
    <app-header />
    <element-legend class="legend" />
    <element-agloworkers class="agloworkers" />
  </div>
</template>

<style lang="scss" scoped>
.legend {
  margin-top: 60px;
}

.agloworkers {
  margin-top: 60px;
}
</style>
