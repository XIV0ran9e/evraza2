<script setup>
import { AppHeader, AppFooter, AppNotifications } from "~/components/app";
</script>

<template>
  <div class="main">
    <app-header class="header" />
    <app-notifications class="notifications" />
    <div class="content">
      <slot></slot>
    </div>
    <app-footer class="footer" />
  </div>
</template>

<style lang="scss" scoped>
.main {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 4fr;
  grid-template-areas:
    "header header"
    "sidebar content"
    "footer footer";
}

.header {
  grid-area: header;
}

.notifications {
  grid-area: sidebar;
  align-self: center;
}

.content {
  grid-area: content;
}

.footer {
  grid-area: footer;
}
</style>
