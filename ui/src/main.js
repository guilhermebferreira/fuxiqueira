import Vue from 'vue';
import App from './App.vue';
import './registerServiceWorker';
import store from './store';
import vuetify from './plugins/vuetify';
import '@babel/polyfill';
import 'roboto-fontface/css/roboto/roboto-fontface.css';
import './assets/style.css';
import '@fortawesome/fontawesome-free/css/all.css';
import '@mdi/font/css/materialdesignicons.css';

Vue.config.productionTip = false;


new Vue({
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
