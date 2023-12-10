import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # 라우터 설정
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # 여기에 웹 소켓 라우팅을 추가
        )
    ),
})
