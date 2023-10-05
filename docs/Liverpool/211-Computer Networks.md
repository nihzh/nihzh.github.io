# 09/28/2023
- ISP: Internet Services Provider
- **packet switching**: break application-layer messages into packets
- L bits per packet, R bps. Tranmission delay: L/R seconds
- queueing delay
- Store and forward: entire packet must arrive at router before it ca be transmitted on next link
- routing algorithm: RAP
- FDM (Frequency Division Multiplexing) and TDM (Tim Division Multiplexing)
- Network of Networks

# 10/02/2023
#### Application layer
- P2P: distributes the host to peers (customers computer)
	- client & server processes
- Inter-process communicating
	- client: process that initiates communication
	- server: process that waits to be contacted
- Sockets: process sends/recieves messages to/from
- Addressing: IP & port number
	- IP: 32-bit, each host has a unique one, could mirror the host name
	- Port: a number between 0-65535, corresponding a listener process on the host.
- A application layer protocal defines:
	- type of messages exchanged
	- message syntax, semantics
	- rules for how processes send and respond to messages.
- A app need: data integrity, timing, throughput, security
- TCP service:
	- reliable transport
	- flow control
	- congestion control
	- does not provide: timing, troughput, security guarantee
	- connection oriented
- UDP service:
	- unreliable transport
	- does not provide everything
- TLS&SSL:socket protocal for TCP, encripted connections, end-point authentication, data integrity
- Non-persistant response time: 2RTT + file transmission time
	- RTT:  a small packet to travel from client to server and back.

# 10/05/2023
### HTTP
- HTTP message: request, response

#### Request
- request line, request header, empty line, request entity
- GET: user input transferred in URL field, by following `?`
- POST: sent in entity body of HTTP package
- HEAD: request headers only
- PUT: uploads new file to server

#### Response
- response status code
	- *200 OK*
	- *301 Moved Permanently*
	- *400 Bad Request*: request not understood
	- *404 Not Found*: resources request not found on the server
	- *505 HTTP Version Not Supported*

#### Cookie
- HTTP is a stage-less protocol
- Cookie: maintaining user/server state
- Generate a unique id, entry in backend database for ID
- Every time client send request to the server with the ID, the server could - recognise and given special services.
- Session state

#### Web caches
- satisfy client request without involving origin server
- Proxy server the request messages to the origin server, if the resource exists in proxy server, then response it directly with not requesting the origin server.
- Weaken the transferring delay if the proxy server in nearer to the client.
- CDN

### SMTP: E-mail
- User agents
- Mail servers
- Sample mail transfer protocol: SMTP \[RFC 5321\] \[RFC 822\]
- Uses TCP
- HTTP: pull, each object encapsulated in tis own response message
- SMTP: push, multiple objects sent in multipart messages persistent connections, uses CRLF to determine end of message