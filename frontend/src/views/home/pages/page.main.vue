<script setup>
import { AppHeader } from "~/components/app";
import { ElementLegend, ElementAgloworkers } from "~/components/elements";

const emit = defineEmits('set')

const set = (item) => {
  emit('set', item)
}

</script>

<template>
  <div class="main">
    <app-header />
    <element-legend class="legend" />
    <element-agloworkers @set="set" class="agloworkers" />
  </div>
</template>

<style lang="scss" scoped>
.main {
  max-height: 100vh;
  overflow-y: scroll;;
}
.legend {
  margin-top: 60px;
}

.agloworkers {
  margin-top: 60px;
}
</style>
