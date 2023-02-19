<script setup>
import { IconOk } from "~/components/icons";
</script>

<template>
  <div class="notification">
    <div class="notification__left">
      <icon-wrapper class="notification__icon" width="24" height="24">
        <icon-ok />
      </icon-wrapper>
    </div>
    <div class="notification__right">
      <p class="notification__title">All Systems Check</p>
      <p class="notification__description">Normal</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.notification {
  display: flex;
  justify-content: center;
  &__icon {
    color: #9499c3;
  }
  &__left {
    margin-right: 12px;
  }
  &__title {
    @include create-font(16px, 700, 100%);
    color: #9499c3;
    margin-bottom: 10px;
  }
  &__description {
    @include create-font(16px, 400, 100%);
    color: rgba(148, 153, 195, 0.5);
  }
}
</style>
