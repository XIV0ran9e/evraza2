<script setup>
import { PageMain, PageScheme, PageGraph } from "./pages";
import { SectionScheme, SectionGraph } from "./sections";
import { ref } from "vue";

const currentEks = ref(null)

const setCurrent = (item) => {
  currentEks.value = item
}
</script>

<template>
  <div class="home">
    <page-main v-if="!currentEks" @set="setCurrent" />
    <page-scheme v-else @close="setCurrent(null)">
      <section-scheme />
    </page-scheme>
    <!-- <page-graph>
      <section-graph />
    </page-graph> -->
  </div>
</template>

<style scoped lang="scss"></style>
