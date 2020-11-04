from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from channels.auth import AuthMiddlewareStack
from django.urls import path

from main.schema import schema

from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/graphql/", GraphqlSubscriptionConsumer.as_asgi()),
    ])
})
