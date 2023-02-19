import traceback
from falcon import CORSMiddleware
from falcon.asgi import App
#
from app.ws import WebSocketHandler, EnumsResource, GetLast

app = App(middleware=CORSMiddleware(allow_origins='*', allow_credentials='*'))
app.add_route("/ws", WebSocketHandler())
app.add_route("/enums", EnumsResource())
app.add_route("/getlast", GetLast())


async def handle_all_exceptions(req, resp, exc, params, ws=None):
    print(exc)
    print(traceback.format_exc())


app.add_error_handler(Exception, handle_all_exceptions)
