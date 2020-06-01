import sys
import json
from argparse import ArgumentParser

import uvicorn
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

from server.engine_adapter import GrpcHoldemEngineAdapter
from server.server import GraphqlHoldemServer

parser = ArgumentParser(prog="poker server app")
parser.add_argument("--config", help="path to server configuration file", required=True)
parser.add_argument("--schema", help="path to graphql schema file", required=True)
args = parser.parse_args()

with open(args.config, "r") as file:
    config = json.load(file)

with open(args.schema, "r") as file:
    schema = file.read()

graphql_server = GraphqlHoldemServer(schema)

server_app = Starlette(debug=True)
server_app.mount(
    "/graphql",
    CORSMiddleware(graphql_server.app, allow_methods=["*"], allow_origins=["*"], expose_headers=[""])
)

if __name__ == "__main__":
    engine_address = config['engine-address']
    engine_adapter = GrpcHoldemEngineAdapter(engine_address['host'], engine_address['port'])
    print(engine_adapter.message("twoj stary"))

    server_address = config["server-address"]
    uvicorn.run("main:server_app", host=server_address['host'], port=server_address['port'], log_level="debug")
