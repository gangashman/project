import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphene_django.filter import DjangoFilterConnectionField


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

    filter_fields = ['name']
    interfaces = (Node, )


class Query(graphene.ObjectType):
    user = Node.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)


schema = graphene.Schema(query=Query)
