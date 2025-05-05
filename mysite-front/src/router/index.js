import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TestView from "@/views/TestView.vue";
import LoginView from "@/views/LoginView.vue";
import LogoutView from "@/views/LogoutView.vue";
import DashboardView from "@/views/DashboardView.vue";
import ManageView from "@/views/ManageView.vue";
import RegisterView from "@/views/RegisterView.vue";
import { useLinksStore } from '@/stores/links'

const routes = [
  {path: '/', name: 'home', component: HomeView},
  {path: '/about', name: 'about', component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')},
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  {path: '/test', name: 'test', component: TestView},
  {path: '/login', name: 'login', component: LoginView},
  {path: '/logout', name: 'logout', component: LogoutView},
  {path: '/manage', name: 'manage', component: ManageView, meta: { requiresAuth: true }},
  {path: '/dashboard', name: 'dashboard', component: DashboardView, meta: { requiresAuth: true }},
  {path: '/register', name: 'register', component: RegisterView},
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  let store = useLinksStore();
  if (to.meta["requiresAuth"] && !store.isUserAuthenticated) {
    next('/login');  // redirige vers login si pas connecté
  } else {
    next();  // continue normalement
  }
});

export default router
