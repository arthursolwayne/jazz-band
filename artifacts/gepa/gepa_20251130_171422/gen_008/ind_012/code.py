
import pretty_midi

# Create the MIDI file with the specified tempo and time signature
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Helper function to create a note
def note(note_number, start, end, velocity=100):
    return pretty_midi.Note(velocity, note_number, start, end)

# Bar 1: Drums only (0.0s - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

drums.notes.extend([
    note(KICK, bar_1_start, bar_1_start + 0.375),  # Kick on beat 1
    note(SNARE, bar_1_start + 0.75, bar_1_start + 0.75 + 0.375),  # Snare on beat 2
    note(KICK, bar_1_start + 1.125, bar_1_start + 1.125 + 0.375),  # Kick on beat 3
    note(SNARE, bar_1_start + 1.5, bar_1_start + 1.5 + 0.375),  # Snare on beat 4
])

# Hihat on every eighth
for i in range(0, 6, 1):
    hihat_start = bar_1_start + i * 0.375
    hihat_end = hihat_start + 0.125  # short duration
    drums.notes.append(note(HIHAT, hihat_start, hihat_end))

# Bar 2-4: Full band (1.5s - 6.0s)

# Time divisions
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5
bar_4_end = 6.0

# D Major scale: D (D4), E (E4), F# (F#4), G (G4), A (A4), B (B4), C# (C#5)
D4 = 62
E4 = 64
F_SHARP4 = 66
G4 = 67
A4 = 69
B4 = 71
C_SHARP5 = 73

# Melody: saxophone, starting on D (62), then B (71), then A (69), then F# (66)
# Duration of each note = 1 beat = 0.375s

# Bar 2: Start with D (62), hold for 1 beat
sax.notes.append(note(D4, bar_2_start, bar_2_start + 0.375))

# Bar 3: B (71), same duration
sax.notes.append(note(B4, bar_3_start, bar_3_start + 0.375))

# Bar 4: A (69), same duration
sax.notes.append(note(A4, bar_4_start, bar_4_start + 0.375))

# Chromatic walking bass line (D, D#, E, F, F#, G, G#, A) — 6 notes over 4 bars
# D (62) → D# (63) → E (64) → F (65) → F# (66) → G (67) → G# (68) → A (69)
bass_notes = [
    (62, bar_2_start, bar_2_start + 0.375),
    (63, bar_2_start + 0.375, bar_2_start + 0.75),
    (64, bar_2_start + 0.75, bar_2_start + 1.125),
    (65, bar_2_start + 1.125, bar_2_start + 1.5),
    (66, bar_2_start + 1.5, bar_2_start + 1.875),
    (67, bar_2_start + 1.875, bar_2_start + 2.25),
    (68, bar_2_start + 2.25, bar_2_start + 2.625),
    (69, bar_2_start + 2.625, bar_2_start + 3.0),
    (62, bar_3_start, bar_3_start + 0.375),
    (63, bar_3_start + 0.375, bar_3_start + 0.75),
    (64, bar_3_start + 0.75, bar_3_start + 1.125),
    (65, bar_3_start + 1.125, bar_3_start + 1.5),
    (66, bar_3_start + 1.5, bar_3_start + 1.875),
    (67, bar_3_start + 1.875, bar_3_start + 2.25),
    (68, bar_3_start + 2.25, bar_3_start + 2.625),
    (69, bar_3_start + 2.625, bar_3_start + 3.0),
    (62, bar_4_start, bar_4_start + 0.375),
    (63, bar_4_start + 0.375, bar_4_start + 0.75),
    (64, bar_4_start + 0.75, bar_4_start + 1.125),
    (65, bar_4_start + 1.125, bar_4_start + 1.5),
    (66, bar_4_start + 1.5, bar_4_start + 1.875),
    (67, bar_4_start + 1.875, bar_4_start + 2.25),
    (68, bar_4_start + 2.25, bar_4_start + 2.625),
    (69, bar_4_start + 2.625, bar_4_start + 3.0),
]

for note_num, start, end in bass_notes:
    bass.notes.append(note(note_num, start, end))

# Piano: 7th chords on the offbeats (2 and 4), D7, G7, B7, E7
# D7 = D, F#, A, C#
# G7 = G, B, D, F
# B7 = B, D#, F#, A
# E7 = E, G#, B, D

# Bar 2: D7 on beat 2 (offbeat)
d7_notes = [D4, F_SHARP4, A4, C_SHARP5]
d7_times = [bar_2_start + 0.75, bar_2_start + 0.75, bar_2_start + 0.75, bar_2_start + 0.75]
for n, t in zip(d7_notes, d7_times):
    piano.notes.append(note(n, t, t + 0.375))

# Bar 3: G7 on beat 2
g7_notes = [G4, B4, D4, F_SHARP4]
g7_times = [bar_3_start + 0.75, bar_3_start + 0.75, bar_3_start + 0.75, bar_3_start + 0.75]
for n, t in zip(g7_notes, g7_times):
    piano.notes.append(note(n, t, t + 0.375))

# Bar 4: B7 on beat 2
b7_notes = [B4, D_SHARP5, F_SHARP4, A4]
b7_times = [bar_4_start + 0.75, bar_4_start + 0.75, bar_4_start + 0.75, bar_4_start + 0.75]
for n, t in zip(b7_notes, b7_times):
    piano.notes.append(note(n, t, t + 0.375))

# Drum pattern for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar_start in [bar_2_start, bar_3_start, bar_4_start]:
    # Kick on 1 and 3
    drums.notes.append(note(KICK, bar_start, bar_start + 0.375))
    drums.notes.append(note(KICK, bar_start + 1.125, bar_start + 1.125 + 0.375))

    # Snare on 2 and 4
    drums.notes.append(note(SNARE, bar_start + 0.75, bar_start + 0.75 + 0.375))
    drums.notes.append(note(SNARE, bar_start + 1.5, bar_start + 1.5 + 0.375))

    # Hihat on every eighth
    for i in range(0, 6, 1):
        hihat_start = bar_start + i * 0.375
        hihat_end = hihat_start + 0.125
        drums.notes.append(note(HIHAT, hihat_start, hihat_end))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to a MIDI file
midi.write("dante_intro.mid")
