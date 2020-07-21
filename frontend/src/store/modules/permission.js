/* eslint-disable */
import { asyncRoutes, constantRoutes,asyncRoutesMap } from '@/router'
import store from '@/store'
import Layout from '@/layout'
/**
 * Use meta.role to determine if the current user has permission
 * @param roles
 * @param route
 */
function hasPermission(roles, route) {
  // console.log(route)
  if (route.meta && route.meta.roles) {
    return roles.some(role => route.meta.roles.includes(role))
  } else {
    return true
  }
}

/**
 * 后台查询的菜单数据拼装成路由格式的数据
 * @param routes
 */
export function generate_menu(data) {
  let routes = []
  data.forEach(item => {
    const menu = item
    menu.component = item.component == '#' ? Layout : asyncRoutesMap[item.component]
    if (item.children ){menu.children = item.children === undefined? []: generate_menu(item.children)}
    routes.push(menu)
  })
  return routes
}

/**
 * Filter asynchronous routing tables by recursion
 * @param routes asyncRoutes
 * @param roles
 */
export function filterAsyncRoutes(routes, roles) {
  const res = []
  routes.forEach(route => {
    const tmp = { ...route }
    if (hasPermission(roles, tmp)) {
      if (tmp.children) {
        tmp.children = filterAsyncRoutes(tmp.children, roles)
      }
      res.push(tmp)
    }
  })

  return res
}

const state = {
  routes: [],
  addRoutes: []
}

const mutations = {
  SET_ROUTES: (state, routes) => {
    state.addRoutes = routes
    state.routes = constantRoutes.concat(routes)
  }
}

const actions = {
  generateRoutes({ commit }, roles) {
    return new Promise(resolve => {
      store.dispatch('user/getAuthMenu', roles).then((data)=>{
        let generateRoutes = [...generate_menu(data),...asyncRoutes]
        let accessedRoutes
        if (roles.includes('admin')) {
          accessedRoutes = generateRoutes || []
        } else {
          accessedRoutes = filterAsyncRoutes(generateRoutes, roles)
        }
        commit('SET_ROUTES', accessedRoutes)
        resolve(accessedRoutes)
      })
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
