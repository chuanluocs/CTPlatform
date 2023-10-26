import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView,
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/main',
        name: 'main',
        component: () => import('../views/Main.vue')
    },
]

// const router = createRouter({
//     history: createWebHistory(process.env.BASE_URL),
//     routes
// })
const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    routes
})

export default router
