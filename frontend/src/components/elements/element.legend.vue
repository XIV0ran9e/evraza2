<script setup>
import { ref } from "vue";
import {
  IconOil,
  IconTemperature,
  IconVibration,
  IconWarningSquare,
  IconCriticalSquare,
  IconCriticalRound,
  IconOkRound,
} from "~/components/icons";

const legends = ref([
  {
    name: "Температура",
    icon: IconTemperature,
  },
  {
    name: "Вибрация",
    icon: IconVibration,
  },
  {
    name: "Уровень масла",
    icon: IconOil,
  },
  {
    name: "Предупреждение",
    icon: IconWarningSquare,
    type: "simple",
  },
  {
    name: "Опасность",
    icon: IconCriticalSquare,
    type: "simple",
  },
  {
    name: "В работе",
    icon: IconOkRound,
    type: "simple",
  },
  {
    name: "Не в работе",
    icon: IconCriticalRound,
    type: "simple",
  },
]);
</script>

<template>
  <div class="legends">
    <div class="container">
      <div class="legends__list">
        <div class="legends__item" v-for="(legend, idx) of legends" :key="idx">
          <icon-wrapper v-if="legend.type !== 'simple'">
            <component :is="legend.icon"></component>
          </icon-wrapper>
          <icon-wrapper v-else width="12" height="12">
            <component :is="legend.icon"></component>
          </icon-wrapper>
          <p class="legends__text">{{ legend.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.legends {
  &__item {
    color: var(--main-text-color);
    margin-right: 30px;
  }
  &__text {
    margin-left: 15px;
    @include create-font(15px, 600, 16px);
  }
  &__item {
    display: flex;
    align-items: center;
  }
  &__list {
    display: flex;
  }
}
</style>
