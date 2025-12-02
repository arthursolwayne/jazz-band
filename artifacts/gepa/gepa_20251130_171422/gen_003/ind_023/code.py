
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Constants
BPM = 160
BEAT_DURATION = 60 / BPM  # seconds per beat
BAR_DURATION = BEAT_DURATION * 4  # 4/4 time
SAMPLE_RATE = 44100
DURATION = BAR_DURATION * 4  # 4 bars

# Frequencies for Dm7 (Dm7 is D F A C)
# D = 293.66 Hz, F = 349.23 Hz, A = 440 Hz, C = 261.63 Hz
# We'll use these to generate a melody with a unique voice

# Key: Dm (D, F, A, C)
# Scale: D Dorian (D, E, F, G, A, B, C)

# Time signatures
# Bar 1: Drums only (Little Ray)
# Bars 2-4: Full ensemble, with you (tenor) taking the melody

# Generate MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Create instruments
drums = Instrument(program=0, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Tenor Sax')

# Add instruments to MIDI
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Drum pattern for Bar 1 (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

def add_drums(start_time):
    # Kick on 1 and 3
    kick_notes = [Note(36, start_time, duration=0.125),
                  Note(36, start_time + 0.75, duration=0.125)]
    for note in kick_notes:
        drums.notes.append(note)

    # Snare on 2 and 4
    snare_notes = [Note(38, start_time + 0.5, duration=0.125),
                   Note(38, start_time + 1.5, duration=0.125)]
    for note in snare_notes:
        drums.notes.append(note)

    # Hihat on every eighth
    hihat_notes = [Note(42, start_time + i * 0.25, duration=0.0625) for i in range(8)]
    for note in hihat_notes:
        drums.notes.append(note)

# Bar 1: Drums only
add_drums(0)

# Bar 2: Full ensemble

# Bass line: Walking line, chromatic approaches
# Dm7: D F A C
# Walking bass line: D F Eb G A Bb B C D E F D
# In time: 4 beats per bar, 12 notes
bass_notes = [ 
    Note(62, 1.0, 0.25), # D
    Note(64, 1.25, 0.25), # F
    Note(63, 1.5, 0.25), # Eb
    Note(67, 1.75, 0.25), # G
    Note(69, 2.0, 0.25), # A
    Note(67, 2.25, 0.25), # Bb
    Note(71, 2.5, 0.25), # B
    Note(67, 2.75, 0.25), # C
    Note(69, 3.0, 0.25), # D
    Note(71, 3.25, 0.25), # E
    Note(69, 3.5, 0.25), # F
    Note(62, 3.75, 0.25) # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
# Dm7 = D F A C
# Dm7 = D F A C
# Dm7: D (root), F (minor 3rd), A (perfect 5th), C (minor 7th)

def add_piano_chord(start_time, chord_notes):
    for note in chord_notes:
        n = Note(note, start_time, duration=0.25)
        piano.notes.append(n)

# Bar 2: Dm7 on beat 2
add_piano_chord(1.5, [62, 64, 69, 67])  # D, F, A, C

# Bar 3: Dm7 on beat 2
add_piano_chord(3.5, [62, 64, 69, 67])  # D, F, A, C

# Saxophone: 4-bar melody, Dm key, unique motif
# Start on D (62), play a motive: D, E, F, Bb (D F Eb G, but in a unique voice)
# Build a phrase that resolves with a twist

# Bar 2: D, E, F, Bb (D, E, F, Bb)
# Bar 3: A, Bb, C, D (A, Bb, C, D)
# Bar 4: A, G, F, D (A, G, F, D)

# Time: Bar 2 starts at 1.0
sax_notes = [
    Note(62, 1.0, 0.25), # D
    Note(64, 1.25, 0.25), # E
    Note(65, 1.5, 0.25), # F
    Note(67, 1.75, 0.25), # Bb

    Note(69, 2.0, 0.25), # A
    Note(67, 2.25, 0.25), # Bb
    Note(71, 2.5, 0.25), # C
    Note(62, 2.75, 0.25), # D

    Note(69, 3.0, 0.25), # A
    Note(67, 3.25, 0.25), # G
    Note(65, 3.5, 0.25), # F
    Note(62, 3.75, 0.25) # D
]
for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
midi.write('dm_intro.mid')

print("MIDI file 'dm_intro.mid' created.")
