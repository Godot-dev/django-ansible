import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App).use(router)
app.provide('API_URL', 'http://localhost:8000/api/')
app.use(createPinia())
app.mount('#app')
