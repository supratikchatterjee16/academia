# Audio Processing

Sound is the physical phenomenon of vibrations traveling through a medium, creating pressure waves that we perceive with our ears. Audio is the electronic or digital representation of sound that is captured, recorded, transmitted, or reproduced using technology. Therefore, all audio is a form of sound, but not all sound is audio.

## Sound 

• Definition: The physical vibrations that propagate as pressure waves through a medium like air or water.  
• Nature: A physical event, a mechanical wave of pressure.  
• Perception: We perceive sound through the reception of these waves by our ears and the subsequent interpretation by our brain.  

## Audio 

• Definition: An electronic signal representing sound, or a sound that has been recorded, transmitted, or processed digitally.  
• Nature: A technological representation of sound.  
• Examples: Music, speech, or environmental noise that is captured by a microphone, stored on a digital file (like an MP3), or played through speakers.  

## Key Differences 

• Physical vs. Electronic: Sound is the natural physical event, while audio is its technological counterpart, often used for recording and transmission.  
• Universal vs. Technological: Sound is a universal phenomenon that exists independently of technology, whereas audio implies the involvement of electronic or digital processes to manipulate or capture it.  

### Analogy 

Think of it this way: a singer performing in a room creates sound (the physical vibration of their voice). If a microphone captures and records that voice, it creates audio (an electronic signal representing that sound). When you then play that recording on a speaker, the audio signal is converted back into sound waves, which your ears then perceive as sound.  

## Pulse-Code Modulation

PCM is the **raw digital representation of an analog audio signal**:

1. **Sampling**: The continuous-time signal (sound wave) is sampled at regular intervals.
   * Example: 44,100 samples per second (44.1 kHz, standard for CD audio).
   * Each sample represents the instantaneous amplitude of the signal at that point in time.
2. **Quantization**: Each sample is mapped to a discrete value.
   * 16-bit PCM → 65,536 possible amplitude levels.
   * 24-bit PCM → 16,777,216 levels.
3. **Storage**: The samples are stored as **integers or floats** in sequence, one after another.

So PCM is essentially a **sequence of numbers** describing the audio waveform over time.

---

### WAV file structure

A **WAV file** is a **container format** for PCM (or sometimes compressed audio), standardized in the **RIFF (Resource Interchange File Format)** structure.

A WAV file consists of **chunks**:

#### RIFF header

* Identifies the file as a WAV: `"RIFF"`
* Size of the file (minus 8 bytes of the RIFF header)
* Format: `"WAVE"`

---

#### fmt chunk

* Contains **format information**, crucial for playback:

  * `AudioFormat` → PCM = 1
  * `NumChannels` → 1 = mono, 2 = stereo
  * `SampleRate` → how many samples per second (e.g., 44100 Hz)
  * `ByteRate` → `SampleRate * NumChannels * BitsPerSample/8`
  * `BlockAlign` → `NumChannels * BitsPerSample/8` (number of bytes per sample frame)
  * `BitsPerSample` → 8, 16, 24, or 32 bits per sample

**Example:**
A standard CD WAV:

* 16-bit, 2 channels, 44,100 Hz
* BlockAlign = 2 channels \* 16 bits/8 = 4 bytes per sample frame
* ByteRate = 44,100 \* 4 = 176,400 bytes/sec

This **tells the audio player how fast to play the samples** (the “playback speed”) and how to interpret each sample.

---

#### data chunk

* The actual **PCM samples**.
* For stereo 16-bit audio:

  * Sample frame = 4 bytes (2 bytes per channel)
  * Data is stored **interleaved**: `[Left1][Right1][Left2][Right2]…`
* The player reads the samples according to the format chunk and outputs the waveform at the correct **rate** (SampleRate).

---

#### Optional chunks

* Metadata: `LIST`, `cue`, `smpl` etc.
* Usually ignored by audio players.

---

### How playback works

1. Player reads **fmt chunk** → knows: sample rate, channels, bits per sample.
2. Player reads **data chunk** → raw PCM samples.
3. Player sends samples to DAC (Digital-to-Analog Converter) **at the sample rate specified**.
4. The DAC converts the numbers into a voltage waveform → speaker vibrates → you hear sound.

---

### Summary

| Component       | WAV Chunk | Role                                        |
| --------------- | --------- | ------------------------------------------- |
| File type       | RIFF      | Identifies WAV format                       |
| Format info     | fmt       | Playback speed (SampleRate), Channels, Bits |
| Audio data      | data      | PCM samples                                 |
| Metadata (opt.) | LIST etc. | Extra info (artist, title)                  |

---

### WAV format in a gist

```text
+-------------------------- WAV File ---------------------------+
|                                                               |
| RIFF Header                                                   |
|  ├─ ChunkID: "RIFF"                                           |
|  ├─ ChunkSize: <file size - 8 bytes>                          |
|  └─ Format: "WAVE"                                            |
|                                                               |
| fmt Chunk (Format Info)                                       |
|  ├─ Subchunk1ID: "fmt "                                       |
|  ├─ Subchunk1Size: 16 (for PCM)                               |
|  ├─ AudioFormat: 1 (PCM)                                      |
|  ├─ NumChannels: 1 (mono) or 2 (stereo)                       |
|  ├─ SampleRate: 44100 Hz (samples/sec)                        |
|  ├─ ByteRate: SampleRate * NumChannels * BitsPerSample/8      |
|  ├─ BlockAlign: NumChannels * BitsPerSample/8                 |
|  └─ BitsPerSample: 16 (CD quality)                            |
|                                                               |
| data Chunk (PCM Samples)                                      |
|  ├─ Subchunk2ID: "data"                                       |
|  ├─ Subchunk2Size: NumSamples * NumChannels * BitsPerSample/8 |
|  └─ PCM Data:                                                 |
|       Sample1_Channel1, Sample1_Channel2,                     |
|       Sample2_Channel1, Sample2_Channel2,                     |
|       ...                                                     |
|                                                               |
| Optional Chunks (metadata, cues, etc.)                        |
+---------------------------------------------------------------+
```

#### Key Points

1. **Playback speed:** Determined by `SampleRate` in the fmt chunk.
2. **Channels:** `NumChannels` tells the player how to interpret interleaved samples.
3. **PCM Data:** Just raw numbers representing amplitude over time.

   * Stereo example: `[Left1][Right1][Left2][Right2]...`
4. **BitsPerSample:** Determines resolution of each sample (16-bit = 65,536 levels).
5. **ByteRate and BlockAlign:** Help the player step through the data correctly.
