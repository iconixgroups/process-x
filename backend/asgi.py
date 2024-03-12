import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from company.urls import websocket_urlpatterns as company_websocket_urlpatterns
from settings.urls import websocket_urlpatterns as settings_websocket_urlpatterns
from design.urls import websocket_urlpatterns as design_websocket_urlpatterns
from dashboard.urls import websocket_urlpatterns as dashboard_websocket_urlpatterns
from publish.urls import websocket_urlpatterns as publish_websocket_urlpatterns
from user.urls import websocket_urlpatterns as user_websocket_urlpatterns
from workflow.urls import websocket_urlpatterns as workflow_websocket_urlpatterns
from reports.urls import websocket_urlpatterns as reports_websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            company_websocket_urlpatterns +
            settings_websocket_urlpatterns +
            design_websocket_urlpatterns +
            dashboard_websocket_urlpatterns +
            publish_websocket_urlpatterns +
            user_websocket_urlpatterns +
            workflow_websocket_urlpatterns +
            reports_websocket_urlpatterns
        )
    ),
})