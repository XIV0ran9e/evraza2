<script setup>
defineProps({
  title: String,
  data: Object,
});
</script>

<template>
  <div class="modal">
    <p class="modal__title">{{ title }}</p>
    <div class="modal__content">
      <div class="modal__info" v-if="data.t">
        <p class="modal__key">T, °С</p>
        <p class="modal__value">{{ data.t }}</p>
      </div>
      <div class="modal__info" v-if="data.v">
        <p class="modal__key">В, мм/с</p>
        <p class="modal__value">{{ data.v }}</p>
      </div>
      <div class="modal__info" v-if="data.g">
        <p class="modal__key">Г, мм/с</p>
        <p class="modal__value">{{ data.g }}</p>
      </div>
      <div class="modal__info" v-if="data.o">
        <p class="modal__key">О, мм/с</p>
        <p class="modal__value">{{ data.o }}</p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.modal {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  padding: 10px;
  &__info {
    color: #ffffff;
    display: flex;
    justify-content: space-between;
    &:not(:last-child) {
      margin-bottom: 5px;
    }
  }
  &__value {
    @include create-font(12px, 500, 15px);
  }
  &__key {
    @include create-font(12px, 500, 15px);
  }
  &__title {
    @include create-font(12px, 500, 17px);
    border: 1px solid #ffffff;
    color: var(--main-text-color);
    padding: 2px 0;
    width: 100%;
    text-align: center;
    margin-bottom: 7px;
  }
}
</style>
