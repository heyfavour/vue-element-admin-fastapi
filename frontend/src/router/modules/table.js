/** When your routing table is too long, you can split it into small modules **/
/* eslint-disable */
import Layout from '@/layout'

const tableRouterMap = {
  dynamic_tabrle: () => import('@/views/table/dynamic-table/index'),
  drag_tabrle: () => import('@/views/table/drag-table'),
  inline_edit_table: () => import('@/views/table/inline-edit-table'),
  complex_table: () => import('@/views/table/complex-table')
}

const tableRouter = {
  path: '/table',
  component: Layout,
  redirect: '/table/complex-table',
  name: 'Table',
  meta: {
    title: 'Table',
    icon: 'table'
  },
  children: [
    {
      path: 'dynamic-tabrle',
      component: tableRouterMap['dynamic_tabrle'],
      name: 'DynamicTable',
      meta: { title: 'Dynamic Table' }
    },
    {
      path: 'drag-table',
      component: tableRouterMap['drag_tabrle'],
      name: 'DragTable',
      meta: { title: 'Drag Table' }
    },
    {
      path: 'inline-edit-table',
      component: tableRouterMap['inline_edit_table'],
      name: 'InlineEditTable',
      meta: { title: 'Inline Edit' }
    },
    {
      path: 'complex-table',
      component: tableRouterMap['complex_table'],
      name: 'ComplexTable',
      meta: { title: 'Complex Table' }
    }
  ]
}
export default tableRouterMap
