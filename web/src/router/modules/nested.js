/** When your routing table is too long, you can split it into small modules **/
/* eslint-disable */
import Layout from '@/layout'

const nestedRouterMap = {
  menu1: () => import('@/views/nested/menu1/index'),
  menu1_1: () => import('@/views/nested/menu1/menu1-1'),
  menu1_2: () => import('@/views/nested/menu1/menu1-2'),
  menu1_2_1: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
  menu1_2_2: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
  menu11_3: () => import('@/views/nested/menu1/menu1-3'),
  menu12: () => import('@/views/nested/menu2/index')
}

const nestedRouter = {
  path: '/nested',
  component: Layout,
  redirect: '/nested/menu1/menu1-1',
  name: 'Nested',
  meta: {
    title: 'Nested Routes',
    icon: 'nested'
  },
  children: [
    {
      path: 'menu1',
      component: nestedRouterMap['menu1'], // Parent router-view
      name: 'Menu1',
      meta: { title: 'Menu 1' },
      redirect: '/nested/menu1/menu1-1',
      children: [
        {
          path: 'menu1-1',
          component: nestedRouterMap['menu1_1'],
          name: 'Menu1-1',
          meta: { title: 'Menu 1-1' }
        },
        {
          path: 'menu1-2',
          component: nestedRouterMap['menu1_2'],
          name: 'Menu1-2',
          redirect: '/nested/menu1/menu1-2/menu1-2-1',
          meta: { title: 'Menu 1-2' },
          children: [
            {
              path: 'menu1-2-1',
              component: nestedRouterMap['menu11_2_1'],
              name: 'Menu1-2-1',
              meta: { title: 'Menu 1-2-1' }
            },
            {
              path: 'menu1-2-2',
              component: nestedRouterMap['menu11_2_2'],
              name: 'Menu1-2-2',
              meta: { title: 'Menu 1-2-2' }
            }
          ]
        },
        {
          path: 'menu1-3',
          component: nestedRouterMap['menu11_3'],
          name: 'Menu1-3',
          meta: { title: 'Menu 1-3' }
        }
      ]
    },
    {
      path: 'menu2',
      name: 'Menu2',
      component: nestedRouterMap['menu112'],
      meta: { title: 'Menu 2' }
    }
  ]
}

export default nestedRouterMap
