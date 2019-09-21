import graphene
import random
import string
from datetime import datetime
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from shorturl.models import UrlEntry


class UrlEntryNode(DjangoObjectType):
    class Meta:
        model = UrlEntry


class Query(graphene.ObjectType):
    url = graphene.Field(UrlEntryNode, short_id=graphene.String())

    def resolve_url(self, info, short_id):
        result = UrlEntry.objects.filter(short_id=short_id)
        if not result:
            raise GraphQLError(f'Entry with id {short_id} was not found')
        if len(result) > 1:
            raise Exception(
                f'Data inconsistency detected: multiple entries with the same short_id={short_id}')
        return result[0]


class AddUrlEntry(graphene.Mutation):

    class Arguments:
        value = graphene.String()

    url_entry = graphene.Field(UrlEntryNode)

    def mutate(self, info, value):
        short_id = AddUrlEntry.generateRandomStringWithDigits()
        entry = UrlEntryNode(
            short_id=short_id,
            value=value,
            created_on=datetime.now()
        )
        return AddUrlEntry(entry)

    def generateRandomStringWithDigits(stringLength=6):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


class Mutations(graphene.ObjectType):
    add_url_entry = AddUrlEntry.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
