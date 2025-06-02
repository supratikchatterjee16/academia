# Protocols - Networks

Protocol - The official procedure or system of rules governing affairs of state or diplomatic occasions.

Network Protocols are the set of protocols that govern information sharing over the internet.

The protocols can be divided by the OSI model, that partitions flow of data into 7 abstraction layers.

## OSI Model

OSI stands for Open Systems Interconnection model. This is a reference model from the International 
Standards Organization(ISO, aka Organisation internationale de normalisation), which is an NGO headquartered in Switzerland.

This is a successor of the TCP/IP model, which is also called the Internet Protocol suite.

The OSI Model was defined in ISO/IEC 7498, and is divided into 4 parts:

1. ISO/IEC 7498-1 The Basic Model
2. ISO/IEC 7498-2 Security Architecture
3. ISO/IEC 7498-3 Naming and addressing
4. ISO/IEC 7498-4 Management framework

These are documents that are sold directly.

The following describes the layers:

| Layer | Protocol Data Unit("Data" unless mentioned otherwise) | Function |
| :---: | :----------------: | :------: |
| Application | | High-level protocols such as for resource sharing or remote file access, e.g. HTTP. |
| Presentation | | Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption |
| Session |  | Managing communication sessions, i.e., continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes |
| Transport | Segment, Datagram | Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing |
| Network | Packet | Structuring and managing a multi-node network, including addressing, routing and traffic control |
| Data link | Frame | Transmission of data frames between two nodes connected by a physical layer |
| Physical | Bit, Symbol | Transmission and reception of raw bit streams over a physical medium |

The bottom 3 are known as "Media" layers, and the others are known as the "Host" layers.

A pnemonic to remember this is :
> All People Seem To Need Data Processing

### Physical Layer

This layer is responsible for the transmission of unstructured raw data between 2 devices, such as an Ethernet port and a network switch, or a network switch and a physical transmission medium. Layer specifications define characteristics such as voltage levels, the timing of voltage changes, physical data rates, maximum transmission distances, modulation scheme, channel access method and physical connectors. This includes the layout of pins, voltages, line impedance, cable specifications, signal timing and frequency for wireless devices. Bit rate control is done at the physical layer and may define transmission mode as simplex, half duplex, and full duplex.

This is usually described in terms of network topology.

### Data Link

