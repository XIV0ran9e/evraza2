<script setup>
import { ref } from "vue";
import {
  IconBearing,
  IconCold,
  IconNitro,
  IconFilter,
  IconSettings,
  IconWater,
} from "~/components/icons";

const icons = ref([
  {
    name: "П-к 1",
    icon: IconBearing,
  },
  {
    name: "П-к 2",
    icon: IconBearing,
  },
  {
    name: "П-к 3",
    icon: IconBearing,
  },

  {
    name: "П-к 4",
    icon: IconBearing,
  },
  {
    name: "П-к 5",
    icon: IconBearing,
  },
  {
    name: "П-к 6",
    icon: IconBearing,
  },
  {
    name: "П-к 7",
    icon: IconBearing,
  },
  {
    name: "П-к 8",
    icon: IconBearing,
  },
  {
    name: "П-к 9",
    icon: IconBearing,
  },
  {
    name: "Ох-ль",
    icon: IconCold,
  },
  {
    name: "За-жка",
    icon: IconSettings,
  },
  {
    name: "К-тор",
    icon: IconNitro,
  },
  {
    name: "П-вод",
    icon: IconFilter,
  },
  {
    name: "Масло",
    icon: IconWater,
  },
]);
</script>

<template>
  <footer class="footer">
    <button class="footer__tab" v-for="(item, idx) of icons" :key="idx">
      <icon-wrapper class="footer__icon" width="32" height="32">
        <component :is="item.icon"></component>
      </icon-wrapper>
      <p class="footer__name">{{ item.name }}</p>
    </button>
    <div class="footer__line"></div>
  </footer>
</template>

<style lang="scss" scoped>
.footer {
  position: relative;
  margin-bottom: 20px;
  height: 100px;
  align-self: end;
  background-color: var(--footer-bg);
  display: flex;
  padding: 10px 0;
  border-radius: 10px;
  width: 1100px;
  display: flex;
  justify-content: center;
  margin: 0 auto;
  &::before {
    content: "";
    width: 38px;
    height: 124px;
    background: var(--footer-bg);
    position: absolute;
    left: -31px;
    transform: rotate(33deg);
    z-index: 0;
    top: 0;
  }
  &::after {
    content: "";
    width: 38px;
    height: 124px;
    background: var(--footer-bg);
    position: absolute;
    right: -31px;
    transform: rotate(-33deg);
    z-index: 0;
    top: 0;
  }
  &__line {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 20px;
    right: 0;
    left: 0;
    background: var(--footer-bg);
  }
  &__tab {
    opacity: 0.4;
    color: var(--main-text-color);
    justify-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;
    min-width: 60px;
    cursor: pointer;
    transition: opacity 0.1s ease;
    &:hover {
      opacity: 1;
    }
    &:not(:last-child) {
      margin-right: 15px;
    }
  }
}
</style>
