
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument, TempoChange

# Settings
BPM = 160
TIME_SIGNATURE = (4, 4)
TEMPO = 60.0 * 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * TEMPO  # seconds per bar (4 beats)
TOTAL_DURATION = 4 * BAR_DURATION  # 4 bars
SAMPLE_RATE = 44100
NOTE_DURATION = 0.375  # seconds per beat
NOTE_RESOLUTION = 0.01  # seconds per note division

# Key: Dm
# Scale: D Dorian (D, E, F, G, A, Bb, C)
# Chords: Dm (D, F, A), Gm7 (G, Bb, D, F), Am7 (A, C, E, G), Cm7 (C, Eb, G, Bb)
# We'll use these as a base for the chord progressions and melodic ideas

# ---------------------
# 1. Drum Pattern (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Slight variations in hihat timing

# 2. Bass Line (Marcus)
# Walking line with chromatic approaches, roots and fifths, D2-G2

# 3. Piano (Diane)
# Open voicings, each bar has a unique chord, resolves on the last beat

# 4. Tenor Sax (Dante)
# One short motif, melodic, haunting, not too clear, not too abstract

# ---------------------
# Create MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# ---------------------
# 1. Drums (Little Ray)
drums = Instrument(program=10, is_drum=True)
drum_notes = []

for bar in range(4):
    for beat in [0, 2]:  # Kick on 1 and 3
        time = (bar * 4 + beat) * NOTE_DURATION
        note = Note(35, time, NOTE_DURATION, 100)  # Kick
        drum_notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        time = (bar * 4 + beat) * NOTE_DURATION
        note = Note(38, time, NOTE_DURATION, 100)  # Snare
        drum_notes.append(note)
    for beat in range(4):  # Hi-hat on every eighth
        time = (bar * 4 + beat) * NOTE_DURATION
        # Add a little variation in hihat timing
        note = Note(42, time - np.random.uniform(-0.01, 0.01), NOTE_DURATION * 0.5, 100)
        drum_notes.append(note)

drums.notes = drum_notes
midi.instruments.append(drums)

# ---------------------
# 2. Bass (Marcus)
bass = Instrument(program=33)
bass_notes = []

# Walking line with D2-G2 (MIDI 38-43)
# D2 (MIDI 38), F2 (MIDI 41), A2 (MIDI 45)
# Chromatic approaches to each root and fifth

for bar in range(4):
    if bar == 0:
        # Bar 1: D2, F, D2
        notes = [38, 41, 38]
    elif bar == 1:
        # Bar 2: G2, Bb2, G2
        notes = [43, 46, 43]
    elif bar == 2:
        # Bar 3: A2, C3, A2
        notes = [45, 48, 45]
    else:
        # Bar 4: C3, Eb3, C3
        notes = [48, 50, 48]

    for i, note in enumerate(notes):
        time = (bar * 4 + i) * NOTE_DURATION
        bass_note = Note(note, time, NOTE_DURATION, 100)
        bass_notes.append(bass_note)

bass.notes = bass_notes
midi.instruments.append(bass)

# ---------------------
# 3. Piano (Diane)
piano = Instrument(program=0)
piano_notes = []

# Bar 1: Dm (D, F, A)
# Open voicing: D, F, A, C (Dm7)
# Play on beat 2 and 4
bar_1_chords = [[50, 53, 55, 57]]  # D, F, A, C
for beat in [1, 3]:
    time = (0 * 4 + beat) * NOTE_DURATION
    for note in bar_1_chords[0]:
        piano_note = Note(note, time, NOTE_DURATION * 0.75, 100)
        piano_notes.append(piano_note)

# Bar 2: Gm7 (G, Bb, D, F)
bar_2_chords = [[55, 58, 60, 62]]
for beat in [1, 3]:
    time = (1 * 4 + beat) * NOTE_DURATION
    for note in bar_2_chords[0]:
        piano_note = Note(note, time, NOTE_DURATION * 0.75, 100)
        piano_notes.append(piano_note)

# Bar 3: Am7 (A, C, E, G)
bar_3_chords = [[57, 60, 64, 67]]
for beat in [1, 3]:
    time = (2 * 4 + beat) * NOTE_DURATION
    for note in bar_3_chords[0]:
        piano_note = Note(note, time, NOTE_DURATION * 0.75, 100)
        piano_notes.append(piano_note)

# Bar 4: Cm7 (C, Eb, G, Bb)
bar_4_chords = [[60, 63, 67, 70]]
for beat in [1, 3]:
    time = (3 * 4 + beat) * NOTE_DURATION
    for note in bar_4_chords[0]:
        piano_note = Note(note, time, NOTE_DURATION * 0.75, 100)
        piano_notes.append(piano_note)

piano.notes = piano_notes
midi.instruments.append(piano)

# ---------------------
# 4. Tenor Sax (Dante)
sax = Instrument(program=64)
sax_notes = []

# Motif: D (MIDI 62) -> F (MIDI 65) -> A (MIDI 69) -> D (MIDI 62)
# First phrase (bar 1): start on D, leave it hanging
# Second phrase (bar 3): return and finish

# Bar 1: Start phrase, incomplete
time = 0 * 4 * NOTE_DURATION
sax_note = Note(62, time, NOTE_DURATION * 0.75, 100)
sax_notes.append(sax_note)

# Bar 3: Return and finish the motif
time = 2 * 4 * NOTE_DURATION
sax_note = Note(62, time, NOTE_DURATION * 0.75, 100)
sax_notes.append(sax_note)
time = time + NOTE_DURATION * 0.5
sax_note = Note(65, time, NOTE_DURATION * 0.75, 100)
sax_notes.append(sax_note)
time = time + NOTE_DURATION * 0.5
sax_note = Note(69, time, NOTE_DURATION * 0.75, 100)
sax_notes.append(sax_note)

# Let the last note ring a little longer
time = time + NOTE_DURATION * 0.5
sax_note = Note(62, time, NOTE_DURATION * 1.5, 100)
sax_notes.append(sax_note)

sax.notes = sax_notes
midi.instruments.append(sax)

# ---------------------
# Save MIDI file
# midi.write disabled
print("MIDI file created: 'dante_intro.mid'")
print("This is the intro that made Wayne lean forward.")
