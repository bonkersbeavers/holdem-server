# holdem-server
Simple python server for playing Texas-Hold'em

Generate proto definitions (those will require manual imports fixing):
```
python3 -m grpc_tools.protoc -I./proto --python_out=./server/proto_gen --grpclib_python_out=./server/proto_gen ./proto/*.proto
```

Build proper app image:
```
docker build -t koronapoker:server .
```

Run the server:
```
docker run -it -p 8081:8081 koronapoker:server python3 main.py --config server-config.json --schema schema.graphqls
```

Access graphql API explorer at localhost:8081/graphql


