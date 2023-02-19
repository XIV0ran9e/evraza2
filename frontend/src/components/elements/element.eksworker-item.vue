<script setup>
import { IconOkRound, IconArrowRight, IconSheme } from "~/components/icons";
import {
  ElementEksworkerSubtitle,
  ElementLastChange,
} from "~/components/elements";
import { CommonSelect, CommonInfoBlock } from "~/components/common";
import { enums } from "~/core/enum";
import { computed } from "vue";

const props = defineProps({
  eksData: Object,
  worker: Object,
});

const { worker } = props;

//todo no algoritm :(
// const formattedEnum = computed(() => {
//   if (!worker) return;
//   return {
//     p1:
//   };
// });
</script>

<template>
  <div class="eksworker">
    <header class="eksworker__header">
      <p class="eksworker__title">
        <icon-wrapper class="eksworker__status" width="12" height="12">
          <icon-ok-round />
        </icon-wrapper>
        {{ eksData.title }}
      </p>
      <button class="eksworker__button">
        <icon-wrapper width="8" height="8">
          <icon-arrow-right />
        </icon-wrapper>
      </button>
    </header>
    <div class="eksworker__content">
      <element-eksworker-subtitle
        :title="eksData.rotor_id"
        :date="eksData.rotor_installed"
        class="eksworker__subtitle"
      />
      <element-last-change class="eksworker__lastchange" />
      <icon-wrapper class="eksworker__scheme" width="211" height="118">
        <icon-sheme />
      </icon-wrapper>
      <div class="eksworker__info">
        <common-select class="eksworker__select" title="Предупреждение">
          <common-info-block title="№1 п-к" />
        </common-select>
        <common-select class="eksworker__select" title="Все подшипники">
          <common-info-block title="№1 п-к" />
          <common-info-block title="№1 п-к" />
          <common-info-block title="№1 п-к" />
          <common-info-block title="№1 п-к" />
        </common-select>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.eksworker {
  border-radius: 7px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  height: fit-content;
  &__scheme {
    margin: 0 auto 20px auto;
  }
  &__header {
    background-color: var(--blocks-bg);
    color: var(--main-text-color);
    padding: 10px;
    display: flex;
    justify-content: space-between;
  }
  &__lastchange {
    margin: 14px 0 14px 0;
  }
  &__content {
    padding: 0 10px;
    border-radius: 0 0 7px 7px;
    background-color: var(--blocks-secondary-bg);
  }
  &__status {
    margin-right: 8px;
  }
  &__button {
    width: 35px;
    height: 35px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--main-text-color);
  }
  &__title {
    display: flex;
    align-items: center;
    font-size: 12px;
  }
}
</style>
