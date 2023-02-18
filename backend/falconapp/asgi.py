from falcon.asgi import App
#
from .ws import WebSocketHandler

app = App()
app.add_route("/ws", WebSocketHandler())
