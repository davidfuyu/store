import Vue from "vue";
import Router from "vue-router";

import { user} from "@/store/store-user.js";

Vue.use(Router);

import Login from "@/components/login.vue";
import Register from "@/components/register.vue";
import Dashboard from "@/components/dashboard.vue";
import OP from "@/components/main-organism-property.vue";
import NO from "@/components/main-organism-new.vue";
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
    },
    {
      path: "/organism/new",
      component: NO,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/organism/:id",
      component: OP,
      props(route) {
        const props = { ...route.params };
        props.id = parseInt(props.id);
        return props
      },
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "*",
      redirect: "/dashboard"
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (user.state.isAuthenticated) {
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
