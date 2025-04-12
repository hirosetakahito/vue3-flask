import { createRouter, createWebHistory } from "vue-router";
import type { RouteLocationNormalized } from "vue-router";
import List from './components/ListPage.vue';
import Add from './components/AddPage.vue';
import Edit from './components/EditPage.vue';


const routes = [
  { path: '/', name: 'list', component: List },
  { path: '/add', name: 'add', component: Add },
  { 
    path: '/edit', 
    name: 'edit', 
    component: Edit, 
    props: ( route: RouteLocationNormalized ) => ({
      id: route.query.id,
      name: route.query.name,
      price: route.query.price
    })
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;
