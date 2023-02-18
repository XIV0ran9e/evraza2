from falcon.asgi import App
#
from backend.ws import WebSocketHandler

app = App()
app.add_route("/ws", WebSocketHandler())
