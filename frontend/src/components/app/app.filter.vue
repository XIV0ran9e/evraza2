<script setup>
import { CommonSelect } from "../common";
import { ref } from "vue";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

const dateFrom = ref(null);
const dateTo = ref(null);
</script>

<template>
  <div class="filter">
    <header class="filter__head">
      <div class="block">
        <VueDatePicker
          v-model="dateFrom"
          class="filter__button dp__theme_dark"
        />
        <button class="filter__value">
          От {{ dateFrom ?? "выберите дату" }}
        </button>
      </div>
      <div class="block">
        <VueDatePicker v-model="dateTo" class="filter__button dp__theme_dark" />
        <button class="filter__value">
          До {{ dateTo ?? "выберите дату" }}
        </button>
      </div>
    </header>
  </div>
</template>

<style lang="scss" scoped>
.block {
  display: flex;
}
.filter {
  margin-left: 50px;
  &__head {
    width: 100%;
  }
  &__button {
    width: 100px;
    background: var(--footer-bg);
    color: var(--main-text-color);
    padding: 10px 15px;
    white-space: nowrap;
    margin-right: 15px;
  }
  &__value {
    width: 100%;
    white-space: nowrap;
    background: var(--footer-bg);
    color: var(--main-text-color);
    padding: 10px 15px;
  }
}
</style>
