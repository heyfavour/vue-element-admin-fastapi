import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/* Router Modules */
import systemRouterMap from './modules/system'

/**
 * 前端动态路由 component加载
 */
export const asyncRoutesMap = {
  Layout,
  redirect: () => import('@/views/redirect/index'),
  login: () => import('@/views/login/index'),
  auth_redirect: () => import('@/views/login/auth-redirect'),
  dashboard: () => import('@/views/dashboard/index'),
  profile: () => import('@/views/profile/index'),
  ...systemRouterMap
}

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path(.*)',
        component: asyncRoutesMap['redirect']
      }
    ]
  },
  {
    path: '/login',
    component: asyncRoutesMap['login'],
    hidden: true
  },
  {
    path: '/auth-redirect',
    component: asyncRoutesMap['auth_redirect'],
    hidden: true
  },
  {
    path: '/404',
    component: asyncRoutesMap['error_404'],
    hidden: true
  },
  {
    path: '/401',
    component: asyncRoutesMap['error_401'],
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        component: asyncRoutesMap['dashboard'],
        name: 'Dashboard',
        meta: { title: '首页', icon: 'dashboard', affix: true }
      }
    ]
  },
  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [
      {
        path: 'index',
        component: asyncRoutesMap['profile'],
        name: 'Profile',
        meta: { title: 'Profile', icon: 'user', noCache: true }
      }
    ]
  }
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  // 404 page must be placed at the end !!!
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
