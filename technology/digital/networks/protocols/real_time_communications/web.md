# WebRTC

## Protocols

1. RTMP
2. RTSP
3. HTTP Live Streaming
4. DASH
5. VOD

### HTTP Live Streaming

HLS works by breaking media files into small chunks so that a client device can stream them. The client can then continuously play these chunks and append new ones to the end to deliver an uninterrupted stream.

A crucial benefit of HLS is that it can respond to changes in transfer speeds and adjust the quality of the streamed media accordingly. This enables the stream to continue — albeit at a lower quality — if transfer speeds drop. Then, it can increase the quality once transfer speeds have recovered.

### Dynamic Adaptive Streaming over HTTP(DASH)



### Real Time Messaging Protocol(RTMP)

Real-Time Messaging Protocol (RTMP) is a communication protocol for streaming audio, video, and data over the Internet. Originally developed as a proprietary protocol by Macromedia for streaming between Flash Player and the Flash Communication Server, Adobe (which acquired Macromedia) has released an incomplete version of the specification of the protocol for public use. 

The RTMP protocol has multiple variations:

1. RTMP proper, the "plain" protocol which works on top of Transmission Control Protocol (TCP) and uses port number 1935 by default.
2. RTMPS, which is RTMP over a Transport Layer Security (TLS/SSL) connection.
3. RTMPE, which is RTMP encrypted using Adobe's own security mechanism. While the details of the implementation are proprietary, the mechanism uses industry standard cryptographic primitives.
4. RTMPT, which is encapsulated within HTTP requests to traverse firewalls. RTMPT is frequently found utilizing cleartext requests on TCP ports 80 and 443 to bypass most corporate traffic filtering. The encapsulated session may carry plain RTMP, RTMPS, or RTMPE packets within.
5. RTMFP, which is RTMP over User Datagram Protocol (UDP) instead of TCP, replacing RTMP Chunk Stream. The Secure Real-Time Media Flow Protocol suite has been developed by Adobe Systems and enables end‐users to connect and communicate directly with each other (P2P).


### Video On Demand(VOD)

Video on demand (VOD) is a media distribution system that allows users to access videos without a traditional video playback device and the constraints of a typical static broadcasting schedule. In the 20th century, broadcasting in the form of over-the-air programming was the most common form of media distribution.



## Architectures

There are 3 architectures : 

1. Peer-Peer
2. Multipoint Control Unit
3. Selective Forwarding Unit

### Peer-Peer(P2P)

Peer-to-peer communication for WebRTC assumes direct exchange of media content between two browsers. Unfortunately, the purely direct exchange may not always be possible, as a browser may be located behind a symmetric Network Address Translator (NAT). NATs force WebRTC applications to use TURN servers located in the public Internet for forwarding of media data between browsers.

### Mulipoint Control Unit(MCU)

In a multipoint control topology, each participant connects to a server known as a multipoint control unit (MCU). The job of the MCU is to receive media from each participant, decode it, and mix the audio and video from the participants together into a single stream and send it to each participant. When using an MCU, each participant uploads their stream just once to the server and the server then sends one stream back to each participant, containing the mixed audio and video from all of the participants.

Pros : 

1. Good in low bandwidth areas
2. Scales well with number of users

Cons : 

1. Server requires high CPU power
2. Transcoding is handled by CPU

### Selective Forwarding Unit(SFU)

In a selective forwarding topology, each participant in a session connects to a server known as a selective forwarding unit (SFU). At its core, SFU is just a “forwarder” — meaning little to no processing happens here.

## Techs

HTTP Live Streaming, Dash, RTMP, RTSP, VOD.

## Media Servers 

Mediasoup, kurento, jitsi, janus

## Media formats and Protocols

MPEG-2, H.264AVC, AAC, AC3, MP4, TS
