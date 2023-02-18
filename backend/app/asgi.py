from falcon.asgi import App
#
from app.ws import WebSocketHandler, EnumsResource

app = App()
app.add_route("/ws", WebSocketHandler())
app.add_route("/enums", EnumsResource())
