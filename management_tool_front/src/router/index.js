import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Daily from '../views/Daily.vue'
import LoginPage from '../views/LoginPage.vue'
import Signup from '../views/Signup.vue'
import ForgotPassword from '../views/ForgotPassword.vue'

const routes = [
  {path: '/', name: 'Home', component: Home},
  {path: '/about', name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  { path: '/login', component: LoginPage },
  { path: '/signup', name : 'signup', component: Signup },
  { path: '/forgot-password', name : 'forgot-password', component: ForgotPassword }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

// router.beforeEach((to, from, next) => {
//   // redirect to login page if not logged in and trying to access a restricted page
//   const publicPages = ['/login']; //, '/register'];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem('user');

//   if (authRequired && !loggedIn) {
//     return next('/login');
//   }

//   next();
// });

export default router
