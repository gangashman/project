import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Home Page - Project',
    }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: {
      title: 'About - Project',
    }
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})
