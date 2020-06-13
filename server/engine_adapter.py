from .proto_gen.TableService_grpc import CashGameTableServiceStub
from .proto_gen.TableService_pb2 import TableSettings
from .proto_gen.Players_pb2 import PlayerJoinRequest, PlayerRemoveRequest
from .proto_gen import Betting_pb2 as Betting
from google.protobuf.empty_pb2 import Empty
import uuid

from .proto_utils import converters

from grpclib.client import Channel
import grpc
import json


class UpdateStream:
    def __init__(self, stream):
        self.stream = stream

    def __enter__(self):
        self.stream.open()
        return self

    async def init(self):
        init_message = Empty()
        await self.stream.send_message(init_message, end=True)

    async def get_update(self):
        return await self.stream.recv_message()

    def __exit__(self):
        self.stream.close()
        return None


class CashGameTableAdapter:
    def __init__(self, host, port):
        self.channel = Channel(host, port)
        self.table = CashGameTableServiceStub(self.channel)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.channel.close()
        return None

    async def create(self, settings: dict):
        message = TableSettings(jsonSettings=settings['jsonSettings'])
        request_status = await self.table.create(message)
        return converters.proto_request_status_to_dict(request_status)

    def get_update_stream(self):
        return self.table.subscribe
        # print(type(xd))
        # return UpdateStream(xd)

    async def add_player(self, player_registration_data: dict):
        join_request = PlayerJoinRequest(seat=player_registration_data['seat'])
        request_status = await self.table.addPlayer(join_request)
        return converters.proto_request_status_to_dict(request_status)

    async def remove_player(self, seat: int):
        remove_request = PlayerRemoveRequest(seat=seat)
        request_status = await self.table.removePlayer(remove_request)
        return request_status

    async def start(self):
        request = Empty()
        request_status = await self.table.start(request)
        return request_status

    async def stop(self):
        request = Empty()
        request_status = await self.table.stop(request)
        return request_status

    async def take_action(self, action: str, token: str, chips: int = 0):
        request = converters.create_proto_action_request(action, token, chips)
        request_status = await self.table.takeAction(request)
        return request_status
