# vue-element-admin-fastapi
vue-element-admin-fastpai

已经完成用户，权限组，菜单等基础功能。但是一些细的功能点的接口都没写，（增删改查遗漏那么一两个功能点样子)

前端使用vue-element-admin的框架，部分组件模仿的ruoyi-vue-ui的，但是没使用其按钮权限控制，在生产中感觉精确到按钮级别少且冗余。

后端使用fastapi框架模仿的Full Stack FastAPI and PostgreSQL，但是模块化以后方便拓展。

socket.io
前端使用了socket.io-client

后端使用了python-socketio，使用异步类试图的情况来区分命名空间。通过fastapi挂载scoet_app的方式。

PS:吐槽下网上的资料要么不全要么不对，最后还是跟着文档全做了一遍.也放弃了使用vue-socket-io。反正socket-io也挺好的


代码就那样，模块化做的还行。socket-io因为网上资料不多，也可以参考看看。


DEMO:http://49.235.242.224:9527/

因为是自己私人服务器，目前暂时没时间做demo的权限，大家查查就好了，不要修改数据，暂时还没备份数据。

开发规则：
1.模块化 看代码就知道了
2.router.include_router下对根路由的RESTFUL请求需要结尾加"/",这个需要前端配合，其他都不需要加"/"
3.其他想到了再加
