import Vue from "vue";
import Router from "vue-router";

Vue.use(localStorage);
Vue.use(Router);

import Login from "@/components/login.vue";
import Register from "@/components/register.vue";

let router = new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      name: 'register',
      component: Register
    }
  ]
});

export default router;
