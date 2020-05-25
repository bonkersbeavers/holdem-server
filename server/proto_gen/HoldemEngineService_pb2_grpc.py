# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import HoldemEngineService_pb2 as HoldemEngineService__pb2

class SimpleHandManagementServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Hello = channel.unary_unary(
                '/service.grpc.SimpleHandManagementService/Hello',
                request_serializer=HoldemEngineService__pb2.SimpleMessage.SerializeToString,
                response_deserializer=HoldemEngineService__pb2.SimpleMessage.FromString,
                )


class SimpleHandManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Hello(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleHandManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=HoldemEngineService__pb2.SimpleMessage.FromString,
                    response_serializer=HoldemEngineService__pb2.SimpleMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.grpc.SimpleHandManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleHandManagementService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.grpc.SimpleHandManagementService/Hello',
            HoldemEngineService__pb2.SimpleMessage.SerializeToString,
            HoldemEngineService__pb2.SimpleMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
