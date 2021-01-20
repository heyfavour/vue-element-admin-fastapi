#!/usr/bin/env python
import socketio
import psutil
from app.extensions.utils import round_float

background_task_started = False


class ServerNamespace(socketio.AsyncNamespace):

    async def on_connect(self, sid, environ):
        # print(f"{sid} is connected !")
        global background_task_started
        if not background_task_started:
            self.server.start_background_task(self.background_task)
            background_task_started = True
        # self.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

    async def on_disconnect(self, sid):
        print(f"{sid} is disconnected !")

    async def on_disconnect_request(self, sid):
        await self.on_disconnect(sid)

    async def on_client_message(self, sid, data):
        print(data)

    async def on_my_event(self, sid, data):
        await self.emit('my_response', data)

    async def on_my_room_event(self, sid, message):
        await self.emit('my_response', {'data': message['data']}, room=message['room'])

    async def on_my_broadcast_event(self, sid, message):
        await self.emit('my_response', {'data': message['data']})

    async def on_join(self, sid, message):
        await self.enter_room(sid, message['room'])
        await self.emit('my_response', {'data': 'Entered room: ' + message['room']}, room=sid)

    async def on_leave(self, sid, message):
        await self.leave_room(sid, message['room'])
        await self.emit('my_response', {'data': 'Left room: ' + message['room']}, room=sid)

    async def on_close(self, sid, message):
        await self.emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.'}, room=message['room'])
        await self.close_room(message['room'])

    async def background_task(self):
        while True:
            sys_info =await self.get_sys_info()
            await self.emit('monitor_server', sys_info)
            await self.server.sleep(1.5)

    async def get_sys_info(self):
        sys_info = {}
        cpu_info = {
            'cpuNum': psutil.cpu_count(logical=False),  # 物理核数
            'used': psutil.cpu_percent(interval=0.1),  # cpu使用率
            'pids': len(psutil.pids()),  # 进程数
            'cpu_freq': psutil.cpu_freq().current,  # CPU频率
            'boot_time': round_float(psutil.boot_time() / (60 * 60 * 60 * 24)),  # 系统启动时间
        }
        sys_info["cpu_info"] = cpu_info
        memory_info = psutil.virtual_memory()
        memory_info = {
            "total": round_float(memory_info.total / (1024 * 1024 * 1024)),
            "used": round_float(memory_info.used / (1024 * 1024 * 1024)),
            "free": round_float(memory_info.free / (1024 * 1024 * 1024)),
            "percent": memory_info.percent,
        }
        sys_info["memory_info"] = memory_info
        return sys_info

