# Antennas

## What is an antenna

An antenna is a specialized transducer that converts electric current into electromagnetic (EM) waves or vice versa. Antennas are used to transmit and receive non-ionizing EM fields, which include radio waves, microwaves, infrared radiation (IR) and visible light.

## Common Terms

- Frequency : The basics of sinusoids (sine and cosine waves), wavelength, frequency and the speed of light.
- Frequency Bands : No discussion on antenna fundamentals is complete without a real-world list of frequency bands.
- Radiation Pattern : The radiation pattern for an antenna is defined on this page. We have 3D graphs of real antenna radiation patterns, with a discussion on isotropic, omnidirectional and directional radiation patterns. Radiation patterns are of the utmost importance in the discussion of antenna basics.
- Field Regions : The introduction to antennas continues with a discussion of Field Regions. The Far Field, Near Field and Fresnel Regions for an antenna is presented.
- Directivity : Directivity is fundamental to antennas. It is a measure of how "directional" an antenna's radiation pattern is.
- Antenna Efficiency : An antenna's efficiency is a measure of how much power is radiated by the antenna relative to the antenna input power.
- Antenna Gain : Antenna Gain is a measure of power radiated in a particular direction (typically the peak direction of radiation).
- Beamwidths and Sidelobes : An antenna's radiation pattern in the far field is often characterized by it's beamwidth and sidelobe levels. This introduction to antenas illustrates this with an example.
- Impedance : Antenna Impedance is presented as the ratio of voltage to current at the antenna's terminals. Low- and High-Frequency models are presented for transmission lines. The fundamentals of antenna theory requires that the antenna be "impedance matched" to the transmission line or the antenna will not radiate. The concept of VSWR is introduced as a measure of how well matched an antenna is.
- Bandwidth : The bandwidth of an antenna is the frequency range over which the antenna radiates. The bandwidth can be defined in different ways; this page presents an introduction to antenna bandwidth.
- Polarization of Waves : All electromagnetic plane waves have an associated polarization. The antenna concepts of Linear, Circular and elliptical polarization are presented.
- Polarization of Antennas : Antennas are also classified by their polarization; this defines the type of plane wave polarization the antenna is most sensitive to. This is a fundamental antenna concept.
- Effective Aperture : Effective aperture is a basic antenna concept that is a measure of the power captured by an antenna from a plane wave. Effective aperture can be expressed as a function of the antenna gain and the wavelength of interest.
- Friis Transmission Equation : Friis Transmission Formula is the most fundamental equation of antenna theory. This equation relates transmit power, antenna gains, distance and wavelength to received power. This page is a must-read for those interested in antenna theory.
- Antenna Temperature : Antenna Temperature is a property of an antenna and the environment it operates in. It is a measure of the noise received by the antenna due to thermal (or temperature) effects.
- Why do Antennas Radiate? : The antenna basics section concludes with a discussion of Why Antennas Radiate. The idea here is to explain the physical concepts that produce radiation in terms of electrons flowing on a wire.
- Smith Charts : a fantastic tool for visualizing the impedance of a transmission line and antenna system as a function of frequency. Smith Charts can be used to increase understanding of transmission lines and how they behave from an impedance viewpoint. Smith Charts are also extremely helpful for impedance matching, as we will see. The Smith Chart is used to display an actual (physical) antenna's impedance when measured on a Vector Network Analyzer (VNA).
- Impedance Dancing : is the process of removing mismatch loss. That is, we want to minimize the reflection coefficient, to reduce the power reflected from the load (the antenna), and maximize the power delivered to the antenna.

## Impedance Dancing

Impedance Matching is the process of removing mismatch loss. That is, we want to minimize the reflection coefficient, to reduce the power reflected from the load (the antenna), and maximize the power delivered to the antenna. This is one of the fundamental tasks in getting an antenna to radiate, and hence is one of the more important topics in antenna theory.

To achieve perfect matching, we want the antenna or load impedance to match the transmission line. That is, we want $Z_L=Z_0 (or Z_{in}=Z_0)$. In Smith Chart terms, we want to move the impedance $Z_L$ towards the center of the Smith Chart, where the reflection coefficient $\Gamma$ is zero.

## Types of Antennas

Broadly antennas based on their types can be :

- Wire Antennas
- Travelling Wave Antennas
- Reflector Antennas
- Microstrip Antennas
- Log-Periodic Antennas
- Aperture Antennas
- Others

### Wire Antennas

A type of radio antenna that includes a long wire suspended over the ground.

- Short Dipole Antenna
- Dipole Antenna
- Half-Wave Dipole
- Broadband Dipoles
- Monopole Antenna
- Folded Dipole Antenna- Loop Antenna
- Cloverleaf Antenna

The advantages of wire antennae include the following.

- The construction of this antenna is simple
- These antennas provide satisfactory gain & directivity.
- These antennas have sharp directional patterns.
- These are not expensive.
- At low vertical angles, it simply focuses on radiation
- They radiate on any range of frequency for which their overall length is not below λ/2.


The disadvantages of wire antennae include the following.

- At low frequencies, the dipole antenna exhibits a large size.
- Loop antennas have poor gain, they hard to tune & are extremely narrowband.
- Helical antennas size is bulky & they are very easily de-tuned by near objects.
- Wire antennas need an appropriate matching system to have better results.
- These antennas need a matching system or tuner unit.

### Travelling Wave Antennas

A class of antenna that uses a traveling wave on a guiding structure as the main radiating mechanism.

- Helical Antennas
- Yagi-Uda Antennas
- Spiral Antennas

### Reflector Antennas

A device that reflects electromagnetic waves.

- Corner Reflector
- Parabolic Reflector (Dish Antenna)

The advantages of reflector antenna include the following.

- These are versatile.
- They have outstanding radiation performances.
- The parabolic type antenna has high gain and high directivity.
- The parabolic reflector decreases minor lobes.
- The amount of wastage of power is fairly low as compared to other antennas.
- It provides flexibility while arranging the feed element.
- The parabolic reflector provides easy beam adjustment.

The disadvantages of reflector antennae include the following.

- The reflector antenna needs to be balanced to keep away from obstruction of the feed point.
- The parabolic type antenna design is a complex procedure.
- The surface distortions in parabolic reflector antenna can take place in an extremely large dish. So this can be decreased with a broad mesh in place of a continuous surface.
- This antenna size is quite large and the overall cost is also high.
- To achieve the best performance results, the feed should be placed exactly at the focus of the parabolic antenna. This is difficult to achieve practically.

### Microstrip Antennas

Mostly used at microwave frequencies. An individual microstrip antenna consists of a patch of metal foil of various shapes (a patch antenna) on the surface of a PCB, with a metal foil ground plane on the other side of the board.

- Rectangular Microstrip (Patch) Antennas
- Planar Inverted-F Antennas (PIFA)

The microstrip antenna characteristics include the following.

- The microstrip antenna patch should be an extremely thin conductive region.
- As compared to a patch, the ground plane should have fairly extremely large dimensions.
- Photo-etching on the substrate is done to construct the radiating element & feed lines.
- A thick dielectric substrate by the dielectric constant in the 2.2 to 12 range offers excellent performance of an antenna.
- Microstrip element arrays in the microstrip antenna design offer superior directivity.
- Microstrip antennas offer high beam width.
- This antenna provides extremely high-quality factors because a high Q factor results in a low efficiency & slight bandwidth. But, this can be compensated by simply increasing the width of the substrate. However, the increase in width beyond a particular limit will cause an unnecessary power loss.

The advantages of microstrip antenna include the following.

- Microstrip antennas are very small.
- These antenna’s weight is less.
- The fabrication procedure provided by this antenna is simple.
- Its installation is very easy because of its small size & volume.
- It offers simple integration by other devices.
- This antenna can perform double & triple-frequency operations.
- These antenna arrays can be constructed easily.
- This antenna provides a high amount of robustness above strong surfaces.
- It is simple to fabricate, customize & modify..
- This antenna has simple and low-cost construction.
- In this antenna, linear & circular polarization is achievable.
- It is appropriate for array antennas.
- It is compatible with monolithic microwave ICs.
- Bandwidth can be expanded by simply improving the width of dielectric material.


The disadvantages of microstrip antennae include the following.

- This antenna provides less gain.
- The efficiency of this type of antenna is low due to conductor & dielectric losses.
- This antenna has a high range of cross-polarization radiation.
- The power handling capacity of this antenna is low.
- It has less impedance bandwidth.
- The structure of this antenna radiates from feeds & other junction points.
- This antenna shows extremely sensitive performance towards ecological factors.
- These antennas are more prone to forged feed radiation.
- This antenna has more conductor & dielectric losses.


### Log-Periodic Antennas

A log-periodic antenna (LP), also known as a log-periodic array or log-periodic aerial, is a multi-element, directional antenna designed to operate over a wide band of frequencies.

- Bow Tie Antennas
- Log-Periodic Antennas
- Log-Periodic Dipole Array

### Aperture Antennas

An aperture antenna may be described in two ways. First, as an area of a surface with a radiating field distribution across it, the field being negligible on the surface outside the area. Second, as an area bounded by edges and excited by a source.

- Slot Antenna
- Cavity-Backed Slot Antenna
- Inverted-F Antenna
- Slotted Waveguide Antenna
- Horn Antenna
- Vivaldi Antenna
- Telescopes

### Others

- NFC Antennas
- Fractal Antennas
- Wearable Antennas
- Lens Antenna
