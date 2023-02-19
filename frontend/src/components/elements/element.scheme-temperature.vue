<script setup>
defineProps({
  value: Number,
});
</script>

<template>
  <div class="temperature">{{ value }} °С</div>
</template>

<style lang="scss" scoped>
.temperature {
  @include create-font(15px, 500, 17px);
  color: var(--main-text-color);
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  padding: 6px;
}
</style>
