
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: D major (no modulation)
key = 'D'

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, is_drum=False)
piano = Instrument(program=Program.PIANO, is_drum=False)
sax = Instrument(program=Program.SAXOPHONE, is_drum=False)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Define tempo and time per beat (seconds)
tempo = 160  # BPM
time_per_beat = 60.0 / tempo  # seconds per beat
bar_length = 4 * time_per_beat  # 4 bars = 6 seconds

# --- DRUMS (Little Ray) ---
# Bar 1: Just kick on 1 and 3
drum_notes = [
    Note(36, 0.0, time_per_beat),  # Kick on beat 1
    Note(36, 2 * time_per_beat, time_per_beat),  # Kick on beat 3
]

# Add to the drums instrument
for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full rhythm
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):  # Bars 2, 3, 4
    for beat in [0, 2]:  # Kick on 1 and 3
        kick_time = (bar - 1) * 4 * time_per_beat + beat * time_per_beat
        drums.notes.append(Note(36, kick_time, time_per_beat))
    for beat in [1, 3]:  # Snare on 2 and 4
        snare_time = (bar - 1) * 4 * time_per_beat + beat * time_per_beat
        drums.notes.append(Note(38, snare_time, time_per_beat))
    for eighth in range(0, 8):  # Hihat on every eighth note
        hihat_time = (bar - 1) * 4 * time_per_beat + eighth * time_per_beat / 2
        drums.notes.append(Note(42, hihat_time, time_per_beat / 2))

# --- BASS (Marcus) ---
# Walking line with chromatic approaches in D major (D, E, F#, G, A, B, C#, D)
bass_notes = [
    Note(62, 0.0, 0.25),  # D
    Note(63, 0.25, 0.25),  # E
    Note(63, 0.5, 0.25),  # F# (chromatic)
    Note(64, 0.75, 0.25),  # G
    Note(66, 1.0, 0.25),  # A
    Note(68, 1.25, 0.25),  # B
    Note(69, 1.5, 0.25),  # C# (chromatic)
    Note(70, 1.75, 0.25),  # D
    Note(69, 2.0, 0.25),  # C#
    Note(68, 2.25, 0.25),  # B
    Note(66, 2.5, 0.25),  # A
    Note(65, 2.75, 0.25),  # G# (chromatic)
    Note(65, 3.0, 0.25),  # G
    Note(66, 3.25, 0.25),  # A
    Note(68, 3.5, 0.25),  # B
    Note(70, 3.75, 0.25),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# --- PIANO (Diane) ---
# 7th chords on 2 and 4, comp on 2 and 4
# D7 = D, F#, A, C
# A7 = A, C#, E, G
# B7 = B, D#, F#, A
# C7 = C, E, G, B

# Bar 2: D7
piano_notes = [
    Note(62, 1.0, 0.25),  # D
    Note(67, 1.0, 0.25),  # F#
    Note(70, 1.0, 0.25),  # A
    Note(67, 1.0, 0.25),  # C (chromatic in 7th)
]

# Bar 3: A7
piano_notes.extend([
    Note(69, 2.0, 0.25),  # A
    Note(72, 2.0, 0.25),  # C#
    Note(74, 2.0, 0.25),  # E
    Note(76, 2.0, 0.25),  # G
])

# Bar 4: B7
piano_notes.extend([
    Note(71, 3.0, 0.25),  # B
    Note(76, 3.0, 0.25),  # D#
    Note(78, 3.0, 0.25),  # F#
    Note(81, 3.0, 0.25),  # A
])

for note in piano_notes:
    piano.notes.append(note)

# --- SAX (You) ---
# A short motif: D - F# - A - G (melodic minor, ascending)
# Start on beat 2 of bar 2, leave it hanging, then resolve
sax_notes = [
    Note(62, 1.0, 0.25),  # D
    Note(67, 1.25, 0.25),  # F#
    Note(70, 1.5, 0.25),  # A
    Note(69, 1.75, 0.25),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
midi.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
