from falcon.asgi import App
#
from app.ws import WebSocketHandler

app = App()
app.add_route("/ws", WebSocketHandler())
