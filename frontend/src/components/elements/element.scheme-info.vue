<script setup>
defineProps({
  data: Object,
});
</script>

<template>
  <div class="info">
    <div class="info__item" v-for="(item, idx) of data" :key="idx">
      <p class="info__title">{{ item.title }}</p>
      <p class="info__value">
        {{ item.value }}
      </p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.info {
  display: flex;
  align-items: center;
  flex-direction: column;
  &__item {
    text-align: left;
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    justify-content: space-between;
    width: 100%;
  }
  &__title {
    @include create-font(12px, 500, 14px);
    margin-right: 16px;
    color: var(--main-text-color);
  }
  &__value {
    @include create-font(12px, 500, 14px);
    color: var(--main-text-color);
    padding: 4px 8px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 4px;
    width: 30px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
