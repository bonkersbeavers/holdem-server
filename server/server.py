from ariadne import gql, QueryType, make_executable_schema, SubscriptionType, convert_kwargs_to_snake_case, ObjectType
from ariadne.asgi import GraphQL
import asyncio
import random

from .engine_adapter import GrpcHoldemEngineAdapter

class GraphqlServer:
    def __init__(self, schema_str, engine_config):
        self._schema_str = gql(schema_str)
        self._engine_adapter = GrpcHoldemEngineAdapter(engine_config['host'], engine_config['port'])
        self._app = None

    def _get_echo_resolver(self):
        def resolver(obj, info, message):
            return message

        return resolver

    def _get_engine_echo_resolver(self):
        def resolver(obj, info, message):
            engine_reply = self._engine_adapter.echo(message)
            return engine_reply.contents

        return resolver

    def start(self):
        query = QueryType()
        query.set_field('echo', self._get_echo_resolver())
        query.set_field('engineEcho', self._get_engine_echo_resolver())

        resolvers = [query]

        executable_schema = make_executable_schema(
            self._schema_str,
            resolvers
        )
        self._app = GraphQL(executable_schema, debug=True)

    def get_app(self):
        return self._app


class MockServer(GraphqlServer):
    def _get_random_table(self):
        players = [
            {
                'name': 'plgmatisz',
                'seat': 0,
                'stack': random.randint(500, 1000),
                'cards': [
                    {'rank': 'ACE', 'suit': 'DIAMONDS'},
                    {'rank': 'KING', 'suit': 'CLUBS'}
                ],
                'currentBet': 300,
                'currentAction': 'BET'
            },
            {
                'name': 'domiomi3',
                'seat': 1,
                'stack': random.randint(500, 1000),
                'cards': [
                    {'rank': 'QUEEN', 'suit': 'DIAMONDS'},
                    {'rank': 'QUEEN', 'suit': 'HEARTS'}
                ],
                'currentBet': 0
            }
        ]
        table = {
            'players': players,
            'positions': {'button': 0, 'smallBlind': 0, 'bigBlind': 1},
            'blinds': {'smallBlind': 20, 'bigBlind': 40},
            'communityCards': [
                {'rank': 'TWO', 'suit': 'DIAMONDS'},
                {'rank': 'QUEEN', 'suit': 'CLUBS'},
                {'rank': 'SEVEN', 'suit': 'DIAMONDS'}
            ],
            'pots': [300]
        }

        return table

    def _get_table_subscription_resolver(self):
        def resolver(table, info):
            return table

        return resolver

    def _get_table_subscription_generator(self):
        async def generator(obj, info):
            while True:
                await asyncio.sleep(10)
                yield self._get_random_table()

        return generator

    def start(self):
        query = QueryType()
        query.set_field('echo', self._get_echo_resolver())
        query.set_field('engineEcho', self._get_engine_echo_resolver())

        subscription = SubscriptionType()
        subscription.set_field('subscribe', self._get_table_subscription_resolver())
        subscription.set_source('subscribe', self._get_table_subscription_generator())

        resolvers = [query, subscription]

        executable_schema = make_executable_schema(
            self._schema_str,
            resolvers
        )
        self._app = GraphQL(executable_schema, debug=True)