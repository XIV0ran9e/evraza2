import asyncio
import uuid
#
from datetime import datetime
# from queue import Queue

import falcon
from falcon.asgi import WebSocket
from falcon.errors import WebSocketDisconnected
from falcon.request import Request


class Hub:
    _connections: dict

    def __init__(self):
        self._connections = {}

    def add_connection(self, _uuid, queue):
        self._connections[_uuid] = queue
        print(f'successfully connected {_uuid}')

    def delete_connection(self, _uuid):
        try:
            self._connections.pop(_uuid)
            print(f'successfully disconnected {_uuid}')
        except KeyError:
            pass

    async def send_to_all(self, message):
        connection: asyncio.Queue
        for connection in self._connections.values():
            await connection.put(message)


class Connection:
    def __init__(self):
        self.uuid = uuid.uuid4().hex
        self.queue = asyncio.Queue()


#         async def sink(queue: Queue):
#             while True:
#                 try:
#                     message = await ws.receive_text()
#                 except falcon.WebSocketDisconnected:
#                     break
#                 if message == 'ping':
#                     await ws.send_text('pong')
#                 else:
#                     await ws.send_text('echo: ' + message)
#
#         sink_task = falcon.create_task(sink())
#
#         while not sink_task.done():
#             while ws.ready and not sink_task.done():
#                 await ws.send_text(datetime.now().isoformat())
#                 await asyncio.sleep(10)


async def spam(hub: Hub):
    while True:
        await hub.send_to_all("aboba test")
        await asyncio.sleep(1)


class WebSocketHandler:
    _hub: Hub

    def __init__(self):
        self._hub = Hub()
        falcon.create_task(spam(self._hub))

    async def on_websocket(self, req: Request, ws: WebSocket):
        try:
            await ws.accept()
        except WebSocketDisconnected:
            return
        connection = Connection()
        self._hub.add_connection(connection.uuid, connection.queue)

        try:
            while ws.ready:
                message = await connection.queue.get()
                await ws.send_text(message)
        except falcon.WebSocketDisconnected:
            pass
        except Exception as exc:
            print(exc)
        finally:
            self._hub.delete_connection(connection.uuid)
