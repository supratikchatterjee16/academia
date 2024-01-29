# Actual Arduino Make

Not depending on `Arduino.h` and related libraries, we have to program all aspects line by line : 

```C
#include <avr/io.h>
int main(void){
    DDRB = 0xFF;
    while(1){
        PORTB++;
        int i; 
        for (i=0; i < 0x7FFF; i++){}
    }
    return 0;
}
```

Change the avrdude target in flash subprocess in Makefile.
