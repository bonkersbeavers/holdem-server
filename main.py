import sys
import json

from starlette.applications import Starlette
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from server.engine_adapter import GrpcHoldemEngineAdapter
from server.server import GraphqlHoldemServer

print("XDDDDDDD")

config_file = sys.argv[1]
with open(config_file, 'r') as file:
    config = json.load(file)

with open(config['schema-path'], 'r') as schema_file:
    schema_str = schema_file.read()

graphql_server = GraphqlHoldemServer(schema_str)

server_app = Starlette(debug=True)
server_app.mount("/graphql",
                 CORSMiddleware(graphql_server.app, allow_methods=['*'], allow_origins=['*'], expose_headers=['']))

if __name__ == '__main__':
    engine_adapter = GrpcHoldemEngineAdapter('0.0.0.0:5004')
    print(engine_adapter.message("twoj stary"))

    uvicorn.run("main:server_app", host=config["host"], port=config["port"], log_level="debug")
