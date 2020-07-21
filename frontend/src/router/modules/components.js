/** When your routing table is too long, you can split it into small modules **/
/* eslint-disable */
import Layout from '@/layout'

const componentsRouterMap = {
  tinymce: () => import('@/views/components-demo/tinymce'),
  markdown: () => import('@/views/components-demo/markdown'),
  json_editor: () => import('@/views/components-demo/json-editor'),
  split_pane: () => import('@/views/components-demo/split-pane'),
  avatar_upload: () => import('@/views/components-demo/avatar-upload'),
  dropzone: () => import('@/views/components-demo/avatar-upload'),
  sticky: () => import('@/views/components-demo/sticky'),
  count_to: () => import('@/views/components-demo/count-to'),
  mixin: () => import('@/views/components-demo/mixin'),
  back_to_top: () => import('@/views/components-demo/back-to-top'),
  drag_dialog: () => import('@/views/components-demo/drag-dialog'),
  drag_select: () => import('@/views/components-demo/drag-select'),
  dnd_list: import('@/views/components-demo/dnd-list'),
  drag_kanban: import('@/views/components-demo/drag-kanban')
}

const componentsRouter = {
  path: '/components',
  component: Layout,
  redirect: 'noRedirect',
  name: 'ComponentDemo',
  meta: {
    title: 'Components',
    icon: 'component'
  },
  children: [
    {
      path: 'tinymce',
      component: componentsRouterMap['tinymce'],
      name: 'TinymceDemo',
      meta: { title: 'Tinymce' }
    },
    {
      path: 'markdown',
      component: componentsRouterMap['markdown'],
      name: 'MarkdownDemo',
      meta: { title: 'Markdown' }
    },
    {
      path: 'json-editor',
      component: componentsRouterMap['json_editor'],
      name: 'JsonEditorDemo',
      meta: { title: 'JSON Editor' }
    },
    {
      path: 'split-pane',
      component: componentsRouterMap['split_pane'],
      name: 'SplitpaneDemo',
      meta: { title: 'SplitPane' }
    },
    {
      path: 'avatar-upload',
      component: componentsRouterMap['avatar_upload'],
      name: 'AvatarUploadDemo',
      meta: { title: 'Upload' }
    },
    {
      path: 'dropzone',
      component: componentsRouterMap['dropzone'],
      name: 'DropzoneDemo',
      meta: { title: 'Dropzone' }
    },
    {
      path: 'sticky',
      component: componentsRouterMap['sticky'],
      name: 'StickyDemo',
      meta: { title: 'Sticky' }
    },
    {
      path: 'count-to',
      component: componentsRouterMap['count_to'],
      name: 'CountToDemo',
      meta: { title: 'Count To' }
    },
    {
      path: 'mixin',
      component: componentsRouterMap['mixin'],
      name: 'ComponentMixinDemo',
      meta: { title: 'Component Mixin' }
    },
    {
      path: 'back-to-top',
      component: componentsRouterMap['back_to_top'],
      name: 'BackToTopDemo',
      meta: { title: 'Back To Top' }
    },
    {
      path: 'drag-dialog',
      component: componentsRouterMap['drag_dialog'],
      name: 'DragDialogDemo',
      meta: { title: 'Drag Dialog' }
    },
    {
      path: 'drag-select',
      component: componentsRouterMap['drag_select'],
      name: 'DragSelectDemo',
      meta: { title: 'Drag Select' }
    },
    {
      path: 'dnd-list',
      component: componentsRouterMap['dnd_list'],
      name: 'DndListDemo',
      meta: { title: 'Dnd List' }
    },
    {
      path: 'drag-kanban',
      component: componentsRouterMap['drag_kanban'],
      name: 'DragKanbanDemo',
      meta: { title: 'Drag Kanban' }
    }
  ]
}

export default componentsRouterMap
