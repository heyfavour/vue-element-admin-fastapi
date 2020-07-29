/** When your routing table is too long, you can split it into small modules **/
/* eslint-disable */
import Layout from '@/layout'

const systemRouterMap = {
  monitor: () => import('@/views/monitor/index'),
}

export default systemRouterMap
