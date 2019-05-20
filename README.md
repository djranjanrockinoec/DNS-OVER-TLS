# DNS over TLS for TCP requests
This Project deals with creating a daemon service to listen to a designated port for DNS requests, encrypt them and send to Cloudflare, get response packet and send unencrypted data back to client.


## REQUIREMENTS
Handle at least one DNS query and give result to client> Completed
DNS over TLS over TCP > Completed

## BONUS POINTS
Allow multiple requests at same time > Completed
Handle UDP requests > Incomplete

## DELIVERABLES
Soure Code > Attached
Dockerfile > Attached
README.md > you are reading it :)

## IMPLEMENTATION
The daemon works as below
1> Establish open unencrypted listener socket for incoming tcp requests from clients.
2> Establish a secured one way SSl/TLS with atached cert.
3> The moment incoming request are received from client, it is encrypted and request is send over to Cloudflare DNS for resolution.
4> Once reply is received from DNS , it is decrypted and sent over to the client who had requested
5> Clean up sockets as per need

The Daemon does not modifies the request. The received request is plainly encrypted and decrypted as per need.

## DISCUSSIONS
>Security concerns
a) Firewall exceptions needs to be provided for the container to work properly.
b) The request stream is not end to end encrypted.

>How to integrate in distributed, microservices-oriented and containerized architecture
a) I would prefer having a discovery service running under my orchestrator to discover the services automatically to maintain registeries and assign requests to required containers/microservice.
b) WE will just need to update the discovery service config to integrate the new container.

>Other improvements
a) I would prefer having this daemon run on the proxy server.
b) For stringent security 2-way ssl between applications is highly suggestible.

## INSTALLATION
```bash
cd N26/
sudo docker build -t dnsotls .
sudo docker run -d -p 127.0.0.1:54:53 -t dnsotls:latest
```

##WHERE TO FIND ME?
[here](https://www.linkedin.com/in/ranjan-behera-692b0817/)

