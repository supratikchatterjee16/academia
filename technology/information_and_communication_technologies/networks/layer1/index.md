# Physical Layer(OSI Layer 1)

The Physical layer is the lowest layer of the OSI model. It defined the mechanical, electrical and procedural specifications for activating, maintaining, and deactivating the physical connection between communicating network systems.

## Responsibilities

| Responsibility          | Description                                                               |
| ----------------------- | ------------------------------------------------------------------------- |
| **Bit Transmission**    | Transmits raw bits (0s and 1s) over a physical medium.                    |
| **Signal Encoding**     | Converts digital data into electrical/optical/radio signals (modulation). |
| **Data Rate Control**   | Defines bit rate (e.g., 100 Mbps, 1 Gbps) and timing (synchronization).   |
| **Physical Topology**   | Defines layout: bus, star, ring, mesh, etc.                               |
| **Transmission Mode**   | Simplex, Half-duplex, Full-duplex communication.                          |
| **Media Specification** | Specifies cables, connectors, and wireless frequencies.                   |
| **Physical Interface**  | Defines voltage levels, pin layout, connector type.                       |
| **Line Configuration**  | Point-to-point or multipoint communication.                               |

## Devices

| Device Type                        | Role at Physical Layer                              |
| ---------------------------------- | --------------------------------------------------- |
| **Cables**                         | Medium for transmission (twisted pair, coax, fiber) |
| **Hubs**                           | Repeat electrical signals to multiple devices       |
| **Repeaters**                      | Boost/regenerate weak signals                       |
| **Modems**                         | Modulate digital to analog and vice versa           |
| **Network Interface Cards (NICs)** | Interface between device and network                |
| **Transceivers**                   | Convert digital signals into physical media forms   |

## Important Concepts

1. Line Coding (Encoding Techniques)
    - NRZ (Non-Return to Zero)
    - Manchester Encoding
    - 4B/5B or 8B/10B encoding (used in Fast/Gigabit Ethernet)
2. Modulation
    - AM, FM, PM for analog
    - ASK, FSK, PSK for digital over analog carriers
3. Transmission Media
    - Guided: Copper (UTP, STP), Coaxial, Fiber-optic
    - Unguided: Microwave, Infrared, Satellite, Radio

Interaction with Layer 2 (Data Link Layer)
- Receives: Frames from Data Link Layer
- Transmits: Bits as physical signals
- Dependency: Data Link Layer specifies MAC addresses and frame structure; Physical Layer only cares about sending the bits

## What It Doesn’t Do

- No framing or addressing
- No error checking or correction
- No routing or switching
- No encryption or compression

