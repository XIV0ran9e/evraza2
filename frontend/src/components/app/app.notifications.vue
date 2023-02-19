<script setup>
import { ElementNotificationsItem } from "~/components/elements";
</script>

<template>
  <aside class="notifications">
    <element-notifications-item class="notifications__item" />
    <element-notifications-item class="notifications__item" />
    <element-notifications-item class="notifications__item" />
  </aside>
</template>

<style lang="scss" scoped>
.notifications {
  &__item {
    margin-bottom: 40px;
  }
}
</style>
