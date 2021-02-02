# vue-element-admin-fastapi
vue-element-admin-fastpai
  
frontend:vue-element-admin  
backend:fastapi and Full Stack FastAPI and PostgreSQL

```
root:[vue-element-admin-fastapi]
|--frontend		#vue-element-admin
|--backend
|      |--app
|      |      |--alembic	#alembic
|      |      |--app
|      |      |      |--api
|      |      |      |      |--api_v1
|      |      |      |      |      |--api.py
|      |      |      |      |      |--endpoints
|      |      |      |      |      |--report	#excel export api 敏捷开发 
|      |      |      |      |      |      |--gen_excel.py
|      |      |      |      |      |      |--gen_report.py
|      |      |      |      |      |      |--report
|      |      |      |      |      |      |--__init__.py
|      |      |      |      |      |--system
|      |      |      |      |      |--websocket	#python-socketio,异步类视图区分命名空间
|      |      |      |      |      |      |--server.py
|      |      |      |      |--deps.py
|      |      |      |--celery_app	#celery
|      |      |      |      |--celery_app.py
|      |      |      |      |--worker
|      |      |      |      |      |--example.py
|      |      |      |--core
|      |      |      |      |--config.py
|      |      |      |      |--security.py
|      |      |      |--crud
|      |      |      |--db
|      |      |      |      |--base.py
|      |      |      |      |--session.py
|      |      |      |--extensions
|      |      |      |      |--exception.py	#全局异常捕获 暂时没有使用的需要,所以没用
|      |      |      |      |--logger.py	#替代原来的日志
|      |      |      |      |--routing.py	#重写路由器  支持exclude_dependencies参数=>支持全局登陆验证剔除login端口
|      |      |      |      |--utils.py		#utils 主要使用了其中的list_to_tree
|      |      |      |--initial_data.py		#初始化数据
|      |      |      |--main.py
|      |      |      |--middleware			#中间件
|      |      |      |      |--access_middle.py		#中间件 登陆日志
|      |      |      |--models		#models 	Table
|      |      |      |--schemas		#schemas	Pydantic
|      |      |      |--tests
|      |      |      |--__init__.py
|      |      |--pyproject.toml		#项目所需要的包
|      |      |--scripts
|--logs				#日志路径
|      |--backend
|      |--celery
```
#### socket.io
frontend:socket.io-client  
backend:python-socketio  
前后端版本兼容请去官网检查，我使用的已经是最新的版本  
前端：socket.io-client version 3.X  
后端：python-socketio  version 5.X  

#### celery
celery-redis  
start celery:sh backend\app\worker-start.sh   
you can use swagger : http://49.235.242.224:8080/docs  api:/utils/test-celery  try send email by celery,just post your email address

#### middleware


#### DEMO:http://49.235.242.224:9527/ 



#### 开发规则整理：  
1.模块化  
2.router.include_router下对根路由的RESTFUL请求需要结尾加"/",这个需要前端配合，其他都不需要加"/"

#### 联系方式:
QQ：619511821
