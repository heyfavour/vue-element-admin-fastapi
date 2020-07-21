/** When your routing table is too long, you can split it into small modules **/
/* eslint-disable */
import Layout from '@/layout'

const systemRouterMap = {
  user: () => import('@/views/system/user/index'),
  menu: () => import('@/views/system/menu/index'),
  department: () => import('@/views/system/department/index'),
  dict: () => import('@/views/system/dict/index'),
  dict_data: () => import('@/views/system/dict/data'),
  permission_role: () => import('@/views/system/permission/role'),
}

export default systemRouterMap
