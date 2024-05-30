import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
const app = createApp(App);

import config from './config.js'
app.provide('config', config);

import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import * as ElementPlusIconsVue from '@element-plus/icons-vue';
app.use(ElementPlus);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}

app.mount('#app');
