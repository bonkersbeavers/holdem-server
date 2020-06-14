import json
from argparse import ArgumentParser

import uvicorn
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

from server.server import GraphqlServer

parser = ArgumentParser(prog="poker server app")
parser.add_argument("--config", help="path to server configuration file", required=True)
parser.add_argument("--schema", help="path to graphql schema file", required=True)
args = parser.parse_args()

with open(args.config, "r") as file:
    config = json.load(file)

with open(args.schema, "r") as file:
    schema = file.read()

graphql_server = GraphqlServer(schema, engine_config=config['engine-address'])
graphql_server.start()

server_app = Starlette(debug=True)
server_app.mount(
    "/graphql",
    CORSMiddleware(graphql_server.get_app(), allow_methods=["*"], allow_origins=["*"], expose_headers=[""])
)

if __name__ == "__main__":
    server_address = config["server-address"]
    uvicorn.run("main:server_app", host=server_address['host'], port=server_address['port'], log_level="debug")
