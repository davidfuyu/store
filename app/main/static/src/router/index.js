import Vue from "vue";
import Router from "vue-router";

import { userProfile } from "@/store/store-user.js";

Vue.use(Router);

import Login from "@/components/login.vue";
import Register from "@/components/register.vue";
import Dashboard from "@/components/dashboard.vue";
import Home from "@/components/home.vue";

let router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: {
        requiresAuth: true
      }
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (userProfile.state.isAuthenticated) {
      next()
    } else {
      next({
        path: '/login',
        query: { redirect: to.path }
      })
    }
  } else {
    next()
  }
})

export default router;
