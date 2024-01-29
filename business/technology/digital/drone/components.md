# Drone Components 

'Drone' is not limited to anything.

Listed are components required primarily for control.
This will later be used for merging all components into a single board.

## Sensors

### Positioning

Altimeter and Accelerometers for **Micro Positioning**: 

1. Altimeter & Barometer(BME280)
2. Accelerometer & gyro(MPU9250)

GPS for macro positioning : 

1. GPS requires antenna and control(Neo 6M, requires antenna separately)
2. GSM and GPRS(A9 and A9G)

### Proximity

1. IR proximity(TCRT5000)
2. Ultrasonic proximity(HC-SR04)

### Vision

1. Camera(OV7670)
 
### RADAR

NXP TEF810X
 
## Communication

### Home Range

Within homes.

1. Wifi : ESP32
2. Bluetooth : ESP32

Long in Home : 
1. HC-12(433 MHz 1km)
2. NRF24L01(2.4GHz 1.1km LOS)
3. LoRa(125kHz, 15 km, uses 3.3V)

### Close Range

This is a range of 50 km, with at least 6 hr flight time.

1. GSM module in urban setting


### Mid Range

### Long Range

## Control

Microcontrollers for dedicated tasks and Microprocessors for general processing.

### Micro Controllers
Controllers can be be dynamically fed data for motor actuator control.
Good for wheel drive control, flight control and any other aspect requiring fine grained control.

1. STM32F4(Clock : 168MHz)
2. Atmega( 328, 32U4 )(Clock : 16MHz)
3. PIC32MZ(Clock : 200MHz)

Arduino Yún exists with Atmega32U4 and Atheros AR9331(micro processor 400 MHz running Linino)
STM32F4 has something called a **DFU** bootloader.

### Microprocessor

1. RP3A0-AU(Clock : 1GHz)
2. RP2040(Clock : 133MHz)
3. BCM2711(Clock : 1.5 GHz)

### Hybrid(Microcontroller with Microprocessor)

1. Arduino Portenta X8(1x ARM® Cortex® -M7 core up to 480MHz & 1x ARM® Cortex® -M4 core up to 240MHz)
    1. MPU : 4x ARM® Cortex® -A53 core up to 1.8GHz 1x ARM® Cortex® -M4 core up to 400 MHz
    2. MCU : 1x ARM® Cortex® -M7 core up to 480MHz (for internal use) 1x ARM® Cortex® -M4 core up to 240MHz

## Interfacing

1. USB to Serial(CH340G)
2. USB to UART(CP210x)

## Voltage Regulators

1. 4B2X(V_in_max : 10 V, V_out : 3.3V, I_out : 150mA)
2. 78M05(V_in : 5-18, V_out : 4.9-5.1 V)

## PCB materials

1. Single Sided Boards – XPC, FR1, FR2, CEM1, CEM3, FR4
2. Double Sided Boards – CEM3, FR4, High Tg from ITEQ, PTFE from ROGERS, GETEK, TACONIC, NELCO
3. Multi Layer Boards – FR4, High Tg, PTFE from ROGERS, GETEK, TACONIC, NELCO

## Manufacturers

### Kolkata

1. Mekatron(9339003645/msplkolkata@gmail.com)(Provides Design Services as well as Assembly)
2. Dhan Laminates(+91-33-40060760/info@dhanlaminates.in)
