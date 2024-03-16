import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store/modules/store'; // Adjust the path to match the location of your store module

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
