from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from your_app.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # 여기에 WebSocket URL 패턴 추가
            path("ws/chat/", ChatConsumer.as_asgi()),
            # 예: path("ws/chat/", YourWebSocketConsumer.as_asgi()),
        )
    ),
})