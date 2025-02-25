import { createRouter, createWebHistory } from 'vue-router'

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'games',
      component: () => import('@/views/GameListView.vue')
    },
    // {
    //   path: '/games/:id',
    //   name: 'game-details',
    //   component: () => import('@/views/GameDetailsView.vue')
    // },
    // {
    //   path: '/games/:id/similar',
    //   name: 'game-graph',
    //   component: () => import('@/views/GameGraphView.vue')
    // },
    // {
    //   path: '/recommendations',
    //   name: 'recommendations',
    //   component: () => import('@/views/RecommendationsView.vue')
    // }
  ]
})

export default router
