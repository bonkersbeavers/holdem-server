import grpc

from .proto_gen.HoldemEngineService_pb2 import SimpleMessage
from .proto_gen.HoldemEngineService_pb2_grpc import SimpleHandManagementServiceStub


class GrpcHoldemEngineAdapter:
    def __init__(self, host, port):
        address = f'{host}:{port}'
        channel = grpc.insecure_channel(address)
        self._engine_stub = SimpleHandManagementServiceStub(channel)

    def echo(self, msg_contents):
        try:
            proper_message = SimpleMessage(contents=msg_contents)
            result = self._engine_stub.Echo(proper_message)
            return result
        except grpc.RpcError as error:
            print(error.details)
            return None
