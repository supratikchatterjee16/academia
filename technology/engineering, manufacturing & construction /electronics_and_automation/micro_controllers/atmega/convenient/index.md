# Convenient Arduino Makefile

The convenient method of making and pushing arduino code.

A sample code for arduino looks like : 

```C
#include<Arduino.h>

const int LED =  13;    // Onboard LED 

void setup() {
    pinMode(LED, OUTPUT);
}

void loop() {
   digitalWrite(LED, HIGH);
   delay(1000);
   digitalWrite(LED, LOW);
   delay(1000);
}

int main(void) {
    init();
    setup();
    while(true){
       loop();
    }
}
```

To load program : 

```
make upload
```

Refer to Makefile for expected library structure.

Tree of `/usr/share/arduino` should look like the following :

```
.
├── Arduino.mk
├── arduino-mk-vars.md
├── chipKIT.mk
├── Common.mk
├── examples -> ../doc/arduino-core/examples
├── hardware
│   ├── arduino
│   └── tools
├── lib
│   ├── keywords.txt
│   ├── preferences.txt
│   └── version.txt
├── libraries
│   ├── EEPROM
│   ├── Esplora
│   ├── Ethernet
│   ├── Firmata
│   ├── GSM
│   ├── LiquidCrystal
│   ├── Robot_Control
│   ├── Robot_Motor
│   ├── SD
│   ├── Servo
│   ├── SoftwareSerial
│   ├── SPI
│   ├── Stepper
│   ├── TFT
│   ├── WiFi
│   └── Wire
├── reference -> ../doc/arduino-core/reference
├── revisions.txt
├── Teensy.mk
└── tools
    ├── howto.txt
    └── Mangler
```
