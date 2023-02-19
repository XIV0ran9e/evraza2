<script setup>
import { computed } from "vue";
import { IconInfoCritical } from "~/components/icons";

const props = defineProps({
  date: String,
});

const computedDate = computed(() => {
  if (props.date > 0) {
    return Math.floor(props.date)
  }
  return 0
})
</script>

<template>
  <div class="lastchange">
    <p class="lastchange__title">Последняя замена ротера</p>
    <div class="lastchange__block">
      <div class="lastchange__date">{{ computedDate }} суток</div>
      <div class="lastchange__info">
        <p class="lastchange__subtitle">
          Прогноз
          <icon-wrapper class="lastchange__icon" width="15" height="15">
            <icon-info-critical />
          </icon-wrapper>
        </p>
        <p class="lastchange__value">{{ computedDate }} суток</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.lastchange {
  &__title {
    @include create-font(15px, 600, 100%);
    margin-bottom: 7px;
    color: var(--main-text-color);
    margin-left: 10px;
  }
  &__block {
    padding: 6px;
    border-radius: 4px;
    background-color: var(--blocks-bg);
    display: flex;
  }
  &__subtitle {
    color: rgba(255, 255, 255, 0.6);
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    font-weight: 600;
  }
  &__value {
    @include create-font(13px, bold, 100%);
    color: var(--main-text-color);
    margin-left: 6px;
  }
  &__icon {
    margin-left: 8px;
  }
  &__date {
    background: var(--blocks-secondary-bg);
    border-radius: 4px;
    padding: 10px;
    margin-right: 15px;
    color: var(--main-text-color);
  }
}
</style>
