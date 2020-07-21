import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login/token',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/users/me',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/logout',
    method: 'post'
  })
}
