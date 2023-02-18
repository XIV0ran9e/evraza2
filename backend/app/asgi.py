import traceback
from falcon.asgi import App
#
from app.ws import WebSocketHandler, EnumsResource

app = App()
app.add_route("/ws", WebSocketHandler())
app.add_route("/enums", EnumsResource())


async def handle_all_exceptions(req, resp, exc, params, ws=None):
    print(exc)
    print(traceback.format_exc())


app.add_error_handler(Exception, handle_all_exceptions)
