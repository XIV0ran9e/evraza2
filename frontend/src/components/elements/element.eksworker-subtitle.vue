<script setup>
defineProps({
  title: String,
  date: String,
});
</script>

<template>
  <div class="title">
    <p class="title__rotor">Ротор №35</p>
    <p class="title__date">{{ date }}</p>
    <button class="title__button">Изменить</button>
  </div>
</template>

<style lang="scss" scoped>
.title {
  color: var(--main-text-color);
  padding: 12px 0;
  border-bottom: 1px solid #ffffff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  &__rotor {
    @include create-font(13px, 600, 16px);
  }
  &__date {
    padding: 7px 7px;
    background: var(--blocks-bg);
    border-radius: 7px;
    color: var(--main-text-color);
    font-size: 12px;
  }
  &__button {
    @include create-font(13px, 600, 16px);
  }
}
</style>
