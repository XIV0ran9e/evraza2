<script setup>
import { computed } from "vue";

const props = defineProps({
  max: String,
  min: String,
  value: Number,
  title: String,
});

const mapValues = (x, x_min, x_max, out_min, out_max) => {
  return Math.floor(
    out_min + ((out_max - out_min) / (x_max - x_min)) * (x - x_min) * 1
  );
};

const currentValue = computed(() =>
  mapValues(props.value, 0, 100, props.min, props.max)
);
</script>

<template>
  <div class="progress" :style="{ maxWidth: +max + 10 + 'px' }">
    <div
      class="progress__bar"
      :style="{ maxWidth: max + 'px', width: currentValue + 'px' }"
    >
      <div class="progress__wrapper">
        <p class="progress__value">
          {{ value }}
        </p>
        <p class="progress__title">
          {{ title }}
        </p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.progress {
  border: 2px solid #ffffff;
  width: 100%;
  &__wrapper {
    position: absolute;
    margin-left: 5px;
  }
  &__bar {
    background: rgba(255, 255, 255, 0.3);
    height: 30px;
    margin: 4px;
    transition: width 0.2s ease;
  }
  &__value {
    @include create-font(11px, 500, 15px);
    color: var(--main-text-color);
  }
  &__title {
    @include create-font(11px, 500, 15px);
    color: var(--main-text-color);
    text-transform: uppercase;
  }
}
</style>
