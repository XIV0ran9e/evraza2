<script setup>
import { IconTemperature, IconVibration } from "~/components/icons";

defineProps({
  title: String,
  status: Object,
  type: String
});
</script>

<template>
  <div class="block">
    <p class="block__title">{{ title }}</p>
    <div class="block__info">
      <div class="block__info-item" :class="{warning: `temp_${type}`}">
        <icon-wrapper class="block__info-icon">
          <icon-temperature />
        </icon-wrapper>
      </div>
      <div class="block__info-item">
        <icon-wrapper class="block__info-icon">
          <icon-vibration />
        </icon-wrapper>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.block {
  padding: 4px 10px;
  background-color: var(--blocks-bg);
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  &__title {
    color: var(--main-text-color);
    font-weight: 400;
  }
  &__info {
    display: flex;
    &-item {
      padding: 2px 10px;
      border-radius: 4px;
      background: #f4f4f4;
      border: 2px solid #cccccc;
      &:not(:last-child) {
        margin-right: 2px;
      }
      &.warning {
        border: 1px solid #F69112;
        background: #FEF1DB;
      }
    }
  }
}
</style>
