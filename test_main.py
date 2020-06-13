from server.engine_adapter import CashGameTableAdapter, UpdateStream
from google.protobuf.empty_pb2 import Empty
from grpclib.client import Stream
from server.proto_utils import converters
import asyncio

async def process_update_stream(stream_coroutine):
    async with stream_coroutine as stream:
        await stream.send_message(Empty(), end=True)

        print('initialized')

        while True:
            update = await stream.recv_message()
            print('new update')
            print(converters.proto_table_to_dict(update.table))


async def main():
    with CashGameTableAdapter(host='localhost', port=8080) as adapter:

        # stream = adapter.get_update_stream().open()
        # stream_processor = process_update_stream(stream)

        settings = """{
            'seatsNumber': 5,
            'defaultStack': 1000,
            'blinds': {
                'smallBlind': 10,
                'bigBlind': 20
            },
            'playerActionTime': -1,
            'dealerActionTime': -1,
            'newHandTime': -1
        }"""

        await adapter.create(settings),

        xd = await adapter.add_player(seat=3, name='plgmatisz')
        print(xd)

        return

        cors = [
            # adapter.add_player(seat=1),
            adapter.add_player(seat=0),
            adapter.add_player(seat=4),
            adapter.start()
        ]

        res = await asyncio.gather(stream_processor, *cors)
        print("lol")

    """
    val seatsNumber: Int,
        val defaultStack: Int,
        val blinds: Blinds,
        val playerActionTime: Int,
        val dealerActionTime: Int,
        val newHandTime: Int
        """

if __name__ == '__main__':
    asyncio.run(main())
