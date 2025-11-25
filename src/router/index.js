import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: () => import('../views/Welcome.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/auth/Login.vue'),
      beforeEnter: (to, from, next) => {
        // If already logged in, redirect to label generator
        const isAuthenticated = localStorage.getItem('isAuthenticated')
        if (isAuthenticated === 'true') {
          next('/label-generator')
        } else {
          next()
        }
      }
    },
    {
      path: '/label-generator',
      name: 'label-generator',
      component: () => import('../views/application/LabelGenerator.vue'),
      meta: { requiresAuth: true }
    },
  ],
})

// Global navigation guard for authentication
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated')

  // Check if route requires authentication
  if (to.meta.requiresAuth && isAuthenticated !== 'true') {
    // Redirect to login if not authenticated
    next('/login')
  } else {
    next()
  }
})

export default router
