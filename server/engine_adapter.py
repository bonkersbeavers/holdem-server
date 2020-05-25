import grpc

from .proto_gen.HoldemEngineService_pb2 import SimpleMessage
from .proto_gen.HoldemEngineService_pb2_grpc import SimpleHandManagementServiceStub


class GrpcHoldemEngineAdapter:
    def __init__(self, server_address):
        channel = grpc.insecure_channel(server_address)
        self._engine_stub = SimpleHandManagementServiceStub(channel)

    def message(self, msg_contents):
        proper_message = SimpleMessage(contents=msg_contents)
        result = self._engine_stub.Hello(proper_message)
        return result
