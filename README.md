# holdem-server
Simple python server for playing Texas-Hold'em

Build proper app image:
```
docker build -t koronapoker:server .
```

Run the server:
```
docker run -it -p 8081:8081 koronapoker:server python3 main.py --config server-config.json --schema schema.graphqls
```

Access graphql API explorer at localhost:8081/graphql


