# STM32 Make process

We need 4 utilities for STM32 : 

1. st-flash : debian package stlink-tools
2. arm-none-eabi-gcc : debian package binutils-arm-none-eabi
3. arm-none-eabi-size : debian package binutils-arm-none-eabi
4. arm-none-eabi-objcopy : debian package binutils-arm-none-eabi

Install with :

```bash
sudo apt install stlink-tools binutils-arm-none-eabi
```

Use the Makefile after that.

Build and flash as : 

```
make all
make flash
```
