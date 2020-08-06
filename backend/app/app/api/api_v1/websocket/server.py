#!/usr/bin/env python
import socketio

background_task_started = False


class ServerNamespace(socketio.AsyncNamespace):

    async def on_connect(self, sid, environ):
        print(f"{sid} is connected !")
        # global background_task_started
        # if not background_task_started:
        #     self.start_background_task(self.background_task)
        #     background_task_started = True
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
            await self.sleep(10)
            await self.emit('my_response', {'data': 'Server generated event'})
