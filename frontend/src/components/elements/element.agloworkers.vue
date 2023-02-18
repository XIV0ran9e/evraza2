<script setup>
import { ElementAgloworkerItem } from "~/components/elements";
defineProps({
  workers: Object,
});
</script>

<template>
  <div class="worker">
    <div class="container">
      <div class="worker__list">
        <element-agloworker-item />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
</style>
