from ariadne import gql, QueryType, make_executable_schema, SubscriptionType
from ariadne.asgi import GraphQL

from .resolvers.fake_handstate_resolver import helloQuery

from .proto_gen.HoldemEngineService_pb2_grpc import SimpleHandManagementServiceStub

class GraphqlHoldemServer:
    def __init__(self, schema, config=None):
        self._config = config
        schema = gql(schema)
        schema = make_executable_schema(schema, [helloQuery])

        self.app = GraphQL(schema, debug=True)
