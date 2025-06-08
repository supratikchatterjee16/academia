# Radio Detection and Ranging

RADAR is a method of using a radio to detect and find the distance to objects.
## Types

1. Pulse based RADAR
    - requires high power
    - required for ranging
2. Continuous Wave RADAR
    - cannot range
    - can find velocity


## RADAR equations

### Ranging

$$ P_r = P_t \frac{G^2 \lambda^2 \sigma^2} {(4\pi)^3 r^4} $$

where,  
$P_r$ is Receive power  
$P_t$ is transmit power  
$G$ is Antenna Gain  
$\lambda$ is wavelength of carrier frequency  
$\sigma$ is radar cross section  
$r$ is range.

### Range resolution

$$ \Delta R = \tau c / 2 $$

$\tau$ is pylse width
$c$ is speed of light

So $1\mu s$ = 150 m of resolution.

### Bandwidth

$ BW = 1 / \tau $

$ \Delta R = c / (2 . BW) $

where,  
BW is bandwidth, and  
$\tau$ is pulse width.

### Velocity

$$ f_{reflected} - f_{transmitted} = \Delta f = \frac{2 v_{target}} {c} f$$

Doppler frequency is the frequency change based on the target __relative to the radar__. This is caused by wave expansion or contraction.

Beat frequency : Difference between original and doppler frequency($f_c$).

