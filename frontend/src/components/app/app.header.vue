<script setup>
import { onMounted } from "vue";
import { IconLogo } from "~/components/icons";
</script>

<template>
  <header class="header">
    <div class="container">
      <div class="header__wrapper">
        <div class="header__title-main">Прогнозная аналитика эксгаустеров</div>
        <div class="header__title-page">Главный экран</div>
        <div class="header__logo">
          <icon-wrapper width="118" height="22">
            <icon-logo />
          </icon-wrapper>
        </div>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
.header {
  color: var(--main-text-color);
  padding: 30px 0;
  &__logo {
    justify-self: self-end;
  }
  &__title {
    &-main {
      @include create-font(26px, 600, 100%);
      line-height: 30px;
    }
    &-page {
      @include create-font(26px, 600, 100%);
    }
  }
  &__wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    align-items: center;
    justify-items: center;
  }
}
</style>
