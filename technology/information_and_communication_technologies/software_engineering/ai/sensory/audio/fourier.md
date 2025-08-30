# Fourier Tranform

The Fourier transform is a mathematical operation that breaks down a function or signal into its constituent frequencies, effectively converting it from the time domain to the frequency domain. This process reveals the amplitude and phase of each frequency present in the original signal, which is a powerful tool for analyzing and understanding complex waveforms. It is widely used in fields like signal processing, physics, and engineering to analyze signals from sources such as audio, RADAR, and even chemical interactions.

## Key Concepts

- Time Domain vs. Frequency Domain: A signal in the time domain shows how its amplitude changes over time. In contrast, a signal in the frequency domain shows which frequencies are present and how strong they are.
- Decomposition: The Fourier transform decomposes a complex waveform into a sum of simple sinusoidal (sine and cosine) waves, each with its own unique frequency and amplitude. 

## Applications

- Signal Processing: Used to filter out unwanted noise or extract specific frequencies from audio signals. 
- Spectroscopy: Fourier-transform infrared (FTIR) spectroscopy is a technique used in chemistry to analyze the chemical composition of a sample by measuring its absorption of light across a range of frequencies. 
- Mass Spectrometry: Fourier-transform ion cyclotron mass analyzers (FTMS) use the Fourier transform to accurately determine the mass-to-charge ratio of ions, providing detailed information about molecular composition. 

## How it Works (Conceptual)

Imagine a complex musical chord played on a piano. In the time domain, you hear the chord as a single, complex sound over time. When you apply a Fourier transform, the process reveals the individual notes (frequencies) that make up that chord. 

## **Why Fourier?**

Most signals (audio, images, vibrations, etc.) are recorded in the **time domain**:

* For audio, that’s amplitude changing with time.
* But many useful properties are hidden in the **frequency domain**:

  * Which notes are being played in music.
  * Which vibration modes exist in a machine.
  * Which frequencies dominate noise.

The **Fourier Transform** is the mathematical tool that lets us **move from the time domain to the frequency domain**.

## **Core Idea**

Any complex signal can be expressed as a sum of **simple sine and cosine waves** of different frequencies, amplitudes, and phases.

Formally:

$$
x(t) = \sum_{k} A_k \cos(2 \pi f_k t + \phi_k)
$$

The Fourier Transform tells us **what those frequencies $f_k$ and amplitudes $A_k$ are**.

## **Fourier Transform definition**

For a continuous-time signal $x(t)$, the Fourier Transform is:

$$
X(f) = \int_{-\infty}^{\infty} x(t) e^{-j 2 \pi f t} dt
$$

* $x(t)$ → time domain signal
* $X(f)$ → frequency spectrum

The inverse transform lets you reconstruct the original signal:

$$
x(t) = \int_{-\infty}^{\infty} X(f) e^{j 2 \pi f t} df
$$

So the transform is **reversible**.

## **Discrete Fourier Transform (DFT)**

In practice, we don’t have continuous signals — we have **digital samples**.
So we use the **DFT**, computed efficiently by the **Fast Fourier Transform (FFT)**.

For $N$ samples $x[n]$:

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N}kn}, \quad k = 0,1,...,N-1
$$

* $X[k]$ → tells us the amplitude & phase of frequency bin $k$.
* Each bin corresponds to a frequency $f_k = \frac{k}{N} f_s$, where $f_s$ is the sampling rate.

## **Why is this useful in signal processing?**

* **Filtering**

  * Low-pass (remove high frequencies → smooth signals)
  * High-pass (remove slow drifts → emphasize detail)
  * Band-pass (keep only specific frequency ranges, e.g. human speech 300–3000 Hz).

* **Compression**

  * MP3, JPEG, MPEG all use frequency representations to discard “less important” frequencies.

* **Feature extraction**

  * Speech recognition looks at spectral features.
  * Machine fault detection looks for certain vibration frequencies.

* **Visualization**

  * Spectrograms (like you plotted) are just a series of FFTs over time windows.

## **Concrete Example (audio signal)**

Imagine a signal that is a mixture of two pure tones:

* A sine wave at 440 Hz (A4, musical note).
* A sine wave at 880 Hz (A5).

The **waveform** just looks like a complicated wiggle.
But after FFT, you see **two clear spikes**: one at 440 Hz and one at 880 Hz.
That tells you exactly which frequencies are present.

## **Problem with standard FFT**

* A standard FFT gives you **frequency content of the whole signal**.
* For music or speech, frequencies change over time — e.g., notes, chords, drums.
* So a single FFT is not enough to see the time evolution.

---

### **Solution: Short-Time Fourier Transform (STFT)**

* The idea is simple: **break the signal into short overlapping windows** and apply the FFT to each window.
* Each window is short enough that the signal is “almost stationary” inside it.
* For each window, you get a frequency spectrum.

Mathematically:

$$
X(t, f) = \sum_{n=0}^{N-1} x[n+t] \cdot w[n] \cdot e^{-j 2 \pi f n / N}
$$

Where:

* $w[n]$ is a **window function** (like Hanning or Hamming) to reduce edge effects.
* $t$ slides along the signal in steps (hop length).
* $f$ is frequency bins from the FFT.

---

### **Building the spectrogram**

* For each time slice (window), compute FFT → gives amplitude per frequency.
* Stack these slices over time → a **2D array**:

  * **x-axis:** time
  * **y-axis:** frequency
  * **color/intensity:** amplitude (often in decibels).

This is exactly what `librosa.stft()` + `librosa.amplitude_to_db()` does in your Python code.

---

#### **Python example**

```python
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load audio
y, sr = librosa.load("example.mp3")

# Compute STFT
S = librosa.stft(y, n_fft=2048, hop_length=512)

# Convert amplitude to decibels
S_db = librosa.amplitude_to_db(np.abs(S))

# Plot spectrogram
plt.figure(figsize=(12, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz', cmap='magma')
plt.colorbar(format="%+2.f dB")
plt.title("Spectrogram")
plt.show()
```

* `n_fft` → size of each window (more points = better frequency resolution, worse time resolution).
* `hop_length` → how much the window slides forward each step (smaller = more time resolution).
* `S_db` → decibel-scaled amplitude for visualization.

---

#### **Intuition**

* Imagine slicing a song into tiny chunks of 20–50 ms.
* Each chunk is almost “pure” in time → FFT tells which frequencies are active.
* Stack the FFT results → now you see **how the frequencies evolve over time**.
