
import numpy as np
import sounddevice as sd
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 4 bars at 160 BPM
BUFFER_SIZE = int(SAMPLE_RATE * DURATION)
FREQ = 440.0  # A4 for reference

# Time signatures and beat timing
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = BEAT * 4  # 4/4 time

# Sine wave function
def sine_wave(freq, duration, amplitude=0.5):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave

# Generate silence
def silence(duration):
    return np.zeros(int(SAMPLE_RATE * duration))

# Bar 1: Little Ray on drums — rhythm only, no melody
def bar_1():
    # Kick on 1 and 3
    kick_1 = sine_wave(60, BEAT/4, 0.2)  # Low C
    kick_3 = sine_wave(60, BEAT/4, 0.2)
    kick_1 = np.concatenate([kick_1, silence(BEAT/2)])
    kick_3 = np.concatenate([silence(BEAT/2), kick_3])
    
    # Snare on 2 and 4
    snare_2 = sine_wave(220, BEAT/4, 0.5)  # A4
    snare_4 = sine_wave(220, BEAT/4, 0.5)
    snare_2 = np.concatenate([silence(BEAT/2), snare_2])
    snare_4 = np.concatenate([snence(BEAT/2), snare_4])
    
    # Hi-hat on every eighth
    hihat = []
    for i in range(8):
        hihat_wave = sine_wave(1000, BEAT/8, 0.1)
        hihat.append(hihat_wave)
    hihat = np.concatenate(hihat)
    
    # Combine all
    bar_1 = kick_1 + kick_3 + snare_2 + snare_4 + hihat
    return bar_1

# Bar 2: Everyone in, sax melody begins
def bar_2():
    # Tenor sax — short motif: Fm (F, Ab, Bb) with rhythmic space
    motif = [
        sine_wave(174.61, BEAT/8, 0.4),  # F
        silence(BEAT/8),
        sine_wave(116.54, BEAT/8, 0.4),  # Ab
        silence(BEAT/8),
        sine_wave(146.83, BEAT/8, 0.4),  # Bb
        silence(BEAT/8),
        sine_wave(174.61, BEAT/8, 0.4),  # F again, rest on beat 4
    ]
    motif = np.concatenate(motif)
    
    # Bass: walking line in Fm, chromatic movement
    bass_notes = [174.61, 195.00, 207.65, 220.00, 174.61, 195.00, 207.65, 220.00]
    bass = []
    for note in bass_notes:
        bass.append(sine_wave(note, BEAT/8, 0.2))
    bass = np.concatenate(bass)
    
    # Piano: 7th chords on 2 and 4, comp around the sax
    piano = []
    for i in range(8):
        if i % 2 == 1:  # On 2 and 4
            chord = sine_wave(146.83, BEAT/4, 0.2)  # Bb
            chord += sine_wave(116.54, BEAT/4, 0.15)  # Ab
            chord += sine_wave(174.61, BEAT/4, 0.15)  # F
            chord += sine_wave(220.00, BEAT/4, 0.1)   # Db (7th in Fm)
            piano.append(chord)
        else:
            piano.append(silence(BEAT/4))
    piano = np.concatenate(piano)
    
    # Drums continue
    bar_2_drums = bar_1()  # Same rhythm pattern as bar 1
    
    # Combine all tracks
    bar_2 = motif + bass + piano + bar_2_drums
    return bar_2

# Bar 3: Develop the motif, answer the question
def bar_3():
    # Tenor sax — variation of the motif, with a twist (F to Eb to Bb)
    motif = [
        sine_wave(174.61, BEAT/8, 0.4),  # F
        silence(BEAT/8),
        sine_wave(130.81, BEAT/8, 0.4),  # Eb
        silence(BEAT/8),
        sine_wave(146.83, BEAT/8, 0.4),  # Bb
        silence(BEAT/8),
        sine_wave(174.61, BEAT/8, 0.4),  # F again, resolves
    ]
    motif = np.concatenate(motif)
    
    # Bass: walking line, chromatic movement, same as before
    bass = bar_2()[len(bar_2()) - len(bass_notes):]
    
    # Piano: same comp pattern, but with a slight shift in tension
    piano = bar_2()[len(bar_2()) - len(piano):]
    
    # Drums continue
    bar_3_drums = bar_1()
    
    # Combine all tracks
    bar_3 = motif + bass + piano + bar_3_drums
    return bar_3

# Bar 4: Resolve the motif, leave a lingering note
def bar_4():
    # Tenor sax — resolution of the motif, Fm7 chord
    motif = [
        sine_wave(174.61, BEAT/8, 0.4),  # F
        silence(BEAT/8),
        sine_wave(174.61, BEAT/8, 0.4),  # F again, rest on beat 4
    ]
    motif += silence(BEAT/2)  # Long rest, silence speaks
    motif = np.concatenate(motif)
    
    # Bass: walking line, resolves to F
    bass_notes = [174.61, 195.00, 207.65, 220.00, 174.61, 195.00, 207.65, 174.61]
    bass = []
    for note in bass_notes:
        bass.append(sine_wave(note, BEAT/8, 0.2))
    bass = np.concatenate(bass)
    
    # Piano: 7th chord, Fm7 (F, Ab, Bb, Db) — resolution
    piano = []
    for i in range(8):
        if i % 2 == 1:  # On 2 and 4
            chord = sine_wave(174.61, BEAT/4, 0.2)  # F
            chord += sine_wave(116.54, BEAT/4, 0.15)  # Ab
            chord += sine_wave(146.83, BEAT/4, 0.15)  # Bb
            chord += sine_wave(130.81, BEAT/4, 0.1)   # Db
            piano.append(chord)
        else:
            piano.append(silence(BEAT/4))
    piano = np.concatenate(piano)
    
    # Drums continue
    bar_4_drums = bar_1()
    
    # Combine all tracks
    bar_4 = motif + bass + piano + bar_4_drums
    return bar_4

# Main function
def main():
    bar_1_data = bar_1()
    bar_2_data = bar_2()
    bar_3_data = bar_3()
    bar_4_data = bar_4()
    
    # Normalize volume and combine
    full_data = np.concatenate([bar_1_data, bar_2_data, bar_3_data, bar_4_data])
    full_data = full_data / np.max(np.abs(full_data))  # Normalize
    
    # Play with sounddevice
    sd.play(full_data, SAMPLE_RATE)
    sd.wait()

if __name__ == "__main__":
    main()
