import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/* Router Modules */
import componentsRouterMap from './modules/components'
import chartsRouterMap from './modules/charts'
import nestedRouterMap from './modules/nested'
import tableRouterMap from './modules/table'
import systemRouterMap from './modules/system'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */
/**
 * 前端动态路由 component加载
 */
export const asyncRoutesMap = {
  Layout,
  redirect: () => import('@/views/redirect/index'),
  login: () => import('@/views/login/index'),
  auth_redirect: () => import('@/views/login/auth-redirect'),
  error_404: () => import('@/views/error-page/404'),
  error_401: () => import('@/views/error-page/401'),
  dashboard: () => import('@/views/dashboard/index'),
  documentation: () => import('@/views/documentation/index'),
  guide: () => import('@/views/guide/index'),
  profile: () => import('@/views/profile/index'),
  permission_page: () => import('@/views/permission/page'),
  permission_directive: () => import('@/views/permission/directive'),
  permission_role: () => import('@/views/permission/role'),
  icon: () => import('@/views/icons/index'),
  ...componentsRouterMap,
  ...chartsRouterMap,
  ...nestedRouterMap,
  ...tableRouterMap,
  ...systemRouterMap,
  example_create: () => import('@/views/example/create'),
  example_edit: () => import('@/views/example/edit'),
  example_list: () => import('@/views/example/list'),
  tab: () => import('@/views/tab/index'),
  error_log: () => import('@/views/error-log/index'),
  export_excel: () => import('@/views/excel/export-excel'),
  select_excel: () => import('@/views/excel/select-excel'),
  merge_header: () => import('@/views/excel/merge-header'),
  upload_excel: () => import('@/views/excel/upload-excel'),
  zip: () => import('@/views/zip/index'),
  pdf: () => import('@/views/pdf/index'),
  pdf_download: () => import('@/views/pdf/download'),
  theme: () => import('@/views/theme/index'),
  clipboard: () => import('@/views/clipboard/index')
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
