import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import IconWrapper from '~/components/icon-wrapper.vue'

const pinia = createPinia()

const app = createApp(App)
app.component('icon-wrapper', IconWrapper)
app.use(pinia)

app.mount('#app')
