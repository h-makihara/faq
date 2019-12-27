import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import FAQ from '../views/FAQ.vue'
import FAQCreate from '../views/faq_create.vue'
Vue.use(VueRouter)

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(VueMaterial)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
  },
  {
    path: '/faq',
    name: 'FAQ Tool',
    component: FAQ
  },
  {
    path: '/faq/create',
    name: 'FAQ Create',
    component: FAQCreate
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
