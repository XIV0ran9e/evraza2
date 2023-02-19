<script setup>
import { IconArrowRight } from "~/components/icons";
import { ref } from "vue";

const isOpened = ref(false);
const content = ref(null);

const toggle = () => {
  isOpened.value = !isOpened.value;
  if (content.value.style.maxHeight) {
    content.value.style.maxHeight = null;
  } else {
    content.value.style.maxHeight = content.value.scrollHeight + "px";
  }
};

defineProps({
  title: String,
});
</script>

<template>
  <div class="select" @click="toggle">
    <div class="select__header">
      <button class="select__button">
        <icon-wrapper
          :class="{ opened: isOpened }"
          class="select__icon"
          width="8"
          height="8"
        >
          <icon-arrow-right />
        </icon-wrapper>
      </button>
      <p class="select__text">Предупреждение</p>
    </div>
    <div ref="content" class="select__content">
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.select {
  cursor: pointer;
  &__content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.2s ease-out;
  }
  &__icon {
    transform: rotate(0deg);
    transition: transform 0.2s ease-out;
    &.opened {
      transform: rotate(90deg);
    }
  }
  &__header {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
  }
  &__button {
    width: 25px;
    height: 25px;
    background-color: var(--button-bg);
    margin-right: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 4px;
  }
  &__text {
    @include create-font(14px, 600, 13px);
    color: var(--main-text-color);
    user-select: none;
  }
}
</style>
