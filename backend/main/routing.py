from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from graphql_ws.django_channels import GraphQLSubscriptionConsumer


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(
                r"^/ws/subscriptions/$",
                GraphQLSubscriptionConsumer
            ),
        ])
    ),
})
