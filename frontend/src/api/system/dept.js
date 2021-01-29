import request from '@/utils/request'

// 查询部门列表
export function listDept(query) {
  return request({
    url: '/system/department/list',
    method: 'get',
    params: query
  })
}

// 查询部门列表（排除节点）
export function listDeptExcludeChild(departmentId) {
  return request({
    url: '/system/department/list/exclude/' + departmentId,
    method: 'get'
  })
}

// 查询部门详细
export function getDept(departmentId) {
  return request({
    url: '/system/department/' + departmentId,
    method: 'get'
  })
}

// 新增部门
export function addDept(data) {
  return request({
    url: '/system/department/',
    method: 'post',
    data: data
  })
}

// 修改部门
export function updateDept(data) {
  return request({
    url: '/system/department/',
    method: 'put',
    data: data
  })
}

// 删除部门
export function delDept(departmentId) {
  return request({
    url: '/system/department/' + departmentId,
    method: 'delete'
  })
}
