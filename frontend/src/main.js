import { createApp } from 'vue'
import App from './components/App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

createApp(App).use(router).mount('#app')
