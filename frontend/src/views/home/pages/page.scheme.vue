<script setup>
import { AppHeader, AppFooter, AppNotifications } from "~/components/app";
const emit = defineEmits(['close'])
const close = () => {
  emit('close')
}
</script>

<template>
  <div class="main">
    <app-header class="header" />
    <app-notifications class="notifications" />
    <div class="content">
      <button @click="close" class="back">Вернуться на главную</button>
      <slot></slot>
    </div>
    <app-footer class="footer" />
  </div>
</template>

<style lang="scss" scoped>
.back {
  color: #000000;
  background: #ffffff;
  border-radius: 7px;
  padding: 10px;
}
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
