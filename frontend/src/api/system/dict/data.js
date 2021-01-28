import request from '@/utils/request'

export function type_all() {
  return request({
    url: '/system/dict/type/all',
    method: 'get'
  })
}

// 查询字典数据列表
export function listData(query) {
  return request({
    url: '/system/dict/data/list',
    method: 'get',
    params: query
  })
}

// 查询字典数据详细
export function getData(id) {
  return request({
    url: '/system/dict/data/' + id,
    method: 'get'
  })
}

// 根据字典类型查询字典数据信息 用于user获取字典
export function getDicts(dictType) {
  return request({
    url: '/system/dict/data/type_code/' + dictType,
    method: 'get'
  })
}

// 新增字典数据
export function addData(data) {
  return request({
    url: '/system/dict/data',
    method: 'post',
    data: data
  })
}

// 修改字典数据
export function updateData(data) {
  return request({
    url: '/system/dict/data',
    method: 'put',
    data: data
  })
}

// 删除字典数据
export function delData(dictCode) {
  return request({
    url: '/system/dict/data/' + dictCode,
    method: 'delete'
  })
}
