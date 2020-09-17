# vue-element-admin-fastapi
vue-element-admin-fastpai

已完成用户，权限组，菜单等基础功能。(一些细的功能点的接口都没写，增删改查遗漏那么一两个功能点样子)    
前端使用vue-element-admin的框架，部分组件模仿ruoyi-vue-ui的，但是没使用其按钮权限控制，在生产中感觉精确到按钮级别少且冗余。  
后端使用fastapi,模仿Full Stack FastAPI and PostgreSQL，但是模块化以后方便拓展。

#### socket.io
前端使用了socket.io-client  
后端使用了python-socketio，使用异步类试图的情况来区分命名空间。通过fastapi挂载scoet_app的方式。  
PS:吐槽下网上的资料要么不全要么不对，最后还是跟着文档全做了一遍.也放弃了使用vue-socket-io。反正socket-io也挺好的

#### celery
celery-redis
celery-app配置位于backend\app\app\celery_app\celery_app.py
woker代码位于backend\app\app\celery_app\worker\目录下，用于不同的woker模块区分
start celery:sh backend\app\worker-start.sh
DEMO_URL:/utils/test-celery 可以发送邮件

代码就那样，模块化做的还行。socket-io因为网上资料不多，也可以参考看看。


#### DEMO:http://49.235.242.224:9527/  
因为项目的commit是放在deps中统一提交的，demo中被我注释了，所以大家的操作不会被保存。有些功能还没写来得及写，后期会慢慢完善。


#### 后期待开发：  
1.完善已有功能  
2.excel配置导出 再report模块下，支持合并。但是还没想好怎么和前端结合。  
3.报表敏捷开发  
4.思考ing  


#### 开发规则整理：  
1.模块化 看代码就知道了  
2.router.include_router下对根路由的RESTFUL请求需要结尾加"/",这个需要前端配合，其他都不需要加"/"  
3.其他想到了再加  

#### 联系方式：
QQ：619511821
