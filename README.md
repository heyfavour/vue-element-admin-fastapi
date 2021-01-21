# vue-element-admin-fastapi
vue-element-admin-fastpai
  
frontend:vue-element-admin
backend:fastapi and Full Stack FastAPI and PostgreSQL

```
root:[vue-element-admin-fastapi]
|--frontend
|--backend
|      |--app
|      |      |--alembic							#alembic
|      |      |      |--versions
|      |      |--app
|      |      |      |--api							#apis
|      |      |      |      |--api_v1
|      |      |      |      |      |--endpoints
|      |      |      |      |      |--report
|      |      |      |      |      |--system
|      |      |      |      |      |--websocket		#python-socketio,异步类视图区分命名空间	app.mount('/', socket_app) in main
|      |      |      |--celery_app					#celery
|      |      |      |      |--worker				#different celery workers
|      |      |      |--core
|      |      |      |--crud
|      |      |      |--db
|      |      |      |--db_pre_start
|      |      |      |--email-templates
|      |      |      |--extensions					#logging and utils
|      |      |      |      |--logger				#LOG_CONFFIG	uvicorn.run(log_config=LOGGING_CONFIG)
|      |      |      |--middleware					#middleware
|      |      |      |--models
|      |      |      |--schemas
|      |      |--scripts
|--logs
|      |--backend
|      |--celery
```
#### socket.io
frontend:socket.io-client  
backend:python-socketio

#### celery
celery-redis  
start celery:sh backend\app\worker-start.sh   
DEMO_URL:/utils/test-celery can end email

#### logging

#### middleware


#### DEMO:http://49.235.242.224:9527/ 



#### 开发规则整理：  
1.模块化  
2.router.include_router下对根路由的RESTFUL请求需要结尾加"/",这个需要前端配合，其他都不需要加"/"

#### 联系方式:
QQ：619511821
