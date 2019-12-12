import Vue from 'vue'
import App from './App.vue'
import router from "@/router";
import store from "@/store/store";
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

import axios from "axios";
import api from "@/plugins/api.js";
Vue.use(api, { axios });
Vue.prototype.$http = axios;


import DialogLoading from "@/components/dialog-loading.vue";
Vue.component("dialog-loading", DialogLoading);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')