/** When your routing table is too long, you can split it into small modules **/
/* eslint-disable */
import Layout from '@/layout'

const systemRouterMap = {
  server: () => import('@/views/monitor/server/index'),
}

export default systemRouterMap
