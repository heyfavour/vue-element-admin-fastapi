/** When your routing table is too long, you can split it into small modules**/
/* eslint-disable */
import Layout from '@/layout'

const chartsRouterMap = {
  keyboard: () => import('@/views/charts/keyboard'),
  line: () => import('@/views/charts/line'),
  mix_chart: () => import('@/views/charts/mix-chart')
}

const chartsRouter = {
  path: '/charts',
  component: Layout,
  redirect: 'noRedirect',
  name: 'Charts',
  meta: {
    title: 'Charts',
    icon: 'chart'
  },
  children: [
    {
      path: 'keyboard',
      component: chartsRouterMap['keyboard'],
      name: 'KeyboardChart',
      meta: { title: 'Keyboard Chart', noCache: true }
    },
    {
      path: 'line',
      component: chartsRouterMap['line'],
      name: 'LineChart',
      meta: { title: 'Line Chart', noCache: true }
    },
    {
      path: 'mix-chart',
      component: chartsRouterMap['mix_chart'],
      name: 'MixChart',
      meta: { title: 'Mix Chart', noCache: true }
    }
  ]
}

export default chartsRouterMap
