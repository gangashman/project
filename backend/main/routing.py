from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from django.conf.urls import url
from graphql_ws.django_channels import GraphQLSubscriptionConsumer

from myapp import consumers

application = ProtocolTypeRouter({
    "websocket": SessionMiddlewareStack(
        URLRouter([
            url(r"^/subscriptions/$", GraphQLSubscriptionConsumer),
        ])
    ),
})
