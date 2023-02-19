<script setup>
import { computed, onMounted } from "vue";
import { ElementAgloworkerItem } from "~/components/elements";
import { useStore } from "~/stores/stores.main";

defineProps({
  workers: Object,
});

const store = useStore();

const computedWorkers = computed(() => store.data);
</script>
<template>
  <div class="worker">
    <div class="container">
      <div class="worker__list" v-if="computedWorkers">
        <element-agloworker-item
          class="worker__item"
          v-for="(worker, idx) in computedWorkers.aglomachines"
          :idx="idx"
          :key="idx"
          :worker="worker"
        />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.worker {
  &__list {
    display: flex;
    justify-content: center;
  }
  &__item {
    &:not(:last-child) {
      margin-right: 20px;
    }
  }
  &__list {
    // overflow-x: scroll;
  }
}
</style>
