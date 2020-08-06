import socketio

from app.api.api_v1.websocket.server import ServerNamespace

sio = socketio.AsyncServer(async_mode='asgi',cors_allowed_origins='*')
sio.register_namespace(ServerNamespace('/server',))

socket_app = socketio.ASGIApp(sio)





