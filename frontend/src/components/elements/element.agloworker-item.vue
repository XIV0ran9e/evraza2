<script setup>
import { computed, watch } from "vue";
import { ElementEksworkerItem } from "~/components/elements";
import { useStore } from "~/stores/stores.main";

const props = defineProps({
  worker: Object,
  idx: Number,
});

const store = useStore();

const enumComputed = computed(() => store.enum);

const eksComputed = computed(() => enumComputed.value[+props.idx - 1]);

const { exchausters, rotor_ids, rotor_installed, id } = eksComputed.value;

const eksFormatted = computed(() => {
  if (!eksComputed.value) return {};
  return [
    {
      agloId: id,
      title: exchausters[0],
      rotor_id: rotor_ids,
      rotor_installed: rotor_installed[0],
    },
    {
      agloId: id,
      title: exchausters[1],
      rotor_id: rotor_ids,
      rotor_installed: rotor_installed[1],
    },
  ];
});

watch(props.worker, () => {
  // console.log(
  //   "change",
  //   props.worker,
  //   eksComputed.value,
  //   props.idx,
  //   enumComputed
  // );
  console.log("change", props.worker);
});
</script>

<template>
  <div class="worker">
    <header class="worker__header">Агломашина № 1</header>
    <div class="worker__content" v-if="eksFormatted">
      <element-eksworker-item
        v-for="(item, idx) of worker"
        :key="idx"
        :eks-data="eksFormatted[idx]"
        :worker="item"
        class="worker__item"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.worker {
  width: 600px;
  &__header {
    padding: 20px 0;
    width: 100%;
    background-color: var(--blocks-bg);
    border-radius: 7px;
    margin-bottom: 20px;
    text-align: center;
    color: var(--main-text-color);
  }
  &__content {
    display: flex;
  }
  &__item {
    width: 100%;
    &:not(:last-child) {
      margin-right: 15px;
    }
  }
}
</style>
