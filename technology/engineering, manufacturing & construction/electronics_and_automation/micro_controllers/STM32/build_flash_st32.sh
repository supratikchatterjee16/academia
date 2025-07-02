# Texane st-link

# Install required lib and bin
sudo apt install git zlib1g-dev libtool flex bison libgmp3-dev libmpfr-dev libncurses5-dev libmpc-dev autoconf texinfo build-essential libftdi-dev
sudo apt install stlink-tools binutils-arm-none-eabi

# GCC compile
arm-none-eabi-gcc -std=gnu99 -g -O2 -Wall -mlittle-endian -mthumb -mthumb-interwork -mcpu=cortex-m0 -fsingle-precision-constant -Wdouble-promotion main.c -o main.elf

# Check size of program
arm-none-eabi-size -tA main.elf 

# Make binary object
arm-none-eabi-objcopy -O binary main.elf main.bin

# Flash
st-flash write firmware.bin 0x8000000
