# holdem-server
Simple python server for playing Texas-Hold'em

To run Docker container, first set up your environment by installing docker engine:
https://docs.docker.com/engine/install/.

To build server's image named poker-server use command:
```
docker build -t poker-server .
```

and start the container named poker-server-cnt with outer port 5000:

```
docker run -p 5000:5000 --name poker-server-cnt poker server
```

and access graphql GUI with 0.0.0.0:5000/graphql.


