from ariadne import gql, QueryType, make_executable_schema, SubscriptionType, convert_kwargs_to_snake_case, ObjectType, \
    MutationType
from ariadne.asgi import GraphQL
import asyncio
import random
import uuid

from .engine_adapter import CashGameTableAdapter
from google.protobuf.empty_pb2 import Empty
from .proto_utils import converters

class GraphqlServer:
    def __init__(self, schema_str, engine_config):
        self._schema_str = gql(schema_str)
        self._table = CashGameTableAdapter(host=engine_config['host'], port=engine_config['port'])
        self._app = None
        self._players = {}

    def _echo_resolver(self):
        async def resolver(obj, info, message):
            return message

        return resolver

    def _create_table_resolver(self):
        async def resolver(obj, info, settings):
            return await self._table.create(settings['jsonSettings'])

        return resolver

    def _add_player_resolver(self):
        async def resolver(obj, info, request):
            request_status = await self._table.add_player(request['playerName'], request['seat'])
            return request_status

        return resolver

    def _subscribe_resolver(self):
        def resolver(table, info, request):
            return table

        return resolver

    def _subscribe_generator(self):
        async def generator(obj, info, request):
            stream_coroutine = self._table.get_update_stream().open()
            async with stream_coroutine as stream:
                request = converters.player_token_to_proto_subscription_request(request['playerToken'])
                await stream.send_message(request, end=True)

                print('initialized')

                while True:
                    update = await stream.recv_message()
                    yield converters.proto_game_update_to_dict(update)

        return generator

    def _take_action_resolver(self):
        async def resolver(obj, info, request):
            action = request['action']
            token = request['actionToken']
            chips = request.get('chips', None)
            request_status = await self._table.take_action(token, action, chips)
            return request_status

        return resolver

    def _start_game_resolver(self):
        async def resolver(obj, info):
            request_status = await self._table.start()
            return request_status

        return resolver

    def _stop_game_resolver(self):
        async def resolver(obj, info):
            request_status = await self._table.stop()
            return request_status

        return resolver

    def start(self):
        query = QueryType()
        query.set_field('echo', self._echo_resolver())

        mutation = MutationType()
        mutation.set_field('createTable', self._create_table_resolver())
        mutation.set_field('addPlayer', self._add_player_resolver())
        mutation.set_field('takeAction', self._take_action_resolver())
        mutation.set_field('startGame', self._start_game_resolver())
        mutation.set_field('stopGame', self._stop_game_resolver())

        subscription = SubscriptionType()
        subscription.set_field('subscribe', self._subscribe_resolver())
        subscription.set_source('subscribe', self._subscribe_generator())

        resolvers = [query, mutation, subscription]

        executable_schema = make_executable_schema(
            self._schema_str,
            resolvers
        )
        self._app = GraphQL(executable_schema, debug=True)

    def get_app(self):
        return self._app
