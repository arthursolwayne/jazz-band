
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Define some note values in F major
F = 70     # F4
Bb = 71    # Bb4
C = 72     # C5
D = 74     # D5
E = 76     # E5
Ab = 77    # Ab5
G = 75     # G4

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

# Kick
kick_times = [bar_1_start + 0.0, bar_1_start + 0.75]
kick_notes = [KICK] * len(kick_times)
for time, note in zip(kick_times, kick_notes):
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(note)

# Snare
snare_times = [bar_1_start + 0.375, bar_1_start + 1.125]
snare_notes = [SNARE] * len(snare_times)
for time, note in zip(snare_times, snare_notes):
    note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hi-hat
hihat_times = [bar_1_start + 0.0, bar_1_start + 0.375, bar_1_start + 0.75, bar_1_start + 1.125]
hihat_notes = [HIHAT] * len(hihat_times)
for time, note in zip(hihat_times, hihat_notes):
    note = pretty_midi.Note(velocity=70, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(note)

# Bar 2-4: Full ensemble (1.5 - 6.0s)
bar_2_start = 1.5

# Sax (Dante): short motif
sax_notes = [
    (F, bar_2_start + 0.0, 0.375),    # F
    (Bb, bar_2_start + 0.375, 0.75),   # Bb
    (C, bar_2_start + 0.75, 1.125),    # C
    (F, bar_2_start + 1.125, 1.5),     # F
    (D, bar_2_start + 1.5, 1.875),     # D
    (E, bar_2_start + 1.875, 2.25),    # E
    (Ab, bar_2_start + 2.25, 2.625),   # Ab
    (F, bar_2_start + 2.625, 3.0)      # F
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bass (Marcus): Walking line in F major
bass_notes = [
    (F, bar_2_start + 0.0, 0.375),    # F
    (G, bar_2_start + 0.375, 0.75),    # G
    (Ab, bar_2_start + 0.75, 1.125),   # Ab
    (Bb, bar_2_start + 1.125, 1.5),    # Bb
    (C, bar_2_start + 1.5, 1.875),     # C
    (D, bar_2_start + 1.875, 2.25),    # D
    (Eb, bar_2_start + 2.25, 2.625),   # Eb
    (F, bar_2_start + 2.625, 3.0)      # F
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4
# F7 = F, A, C, Eb
chord_notes = [
    (F, bar_2_start + 0.375, 0.75),
    (A, bar_2_start + 0.375, 0.75),
    (C, bar_2_start + 0.375, 0.75),
    (Eb, bar_2_start + 0.375, 0.75),
    (F, bar_2_start + 1.125, 1.5),
    (A, bar_2_start + 1.125, 1.5),
    (C, bar_2_start + 1.125, 1.5),
    (Eb, bar_2_start + 1.125, 1.5)
]

for pitch, start, end in chord_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Drums (Little Ray): continue the same groove
bar_2_end = 3.0
bar_3_end = 4.5
bar_4_end = 6.0

def add_drums(start):
    kick_times = [start + 0.0, start + 0.75]
    snare_times = [start + 0.375, start + 1.125]
    hihat_times = [start + 0.0, start + 0.375, start + 0.75, start + 1.125]

    for time in kick_times:
        note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + 0.15)
        drums.notes.append(note)

    for time in snare_times:
        note = pretty_midi.Note(velocity=95, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)

    for time in hihat_times:
        note = pretty_midi.Note(velocity=70, pitch=HIHAT, start=time, end=time + 0.05)
        drums.notes.append(note)

# Add drum grooves for bars 2-4
add_drums(bar_2_start)
add_drums(bar_2_start + 1.5)
add_drums(bar_2_start + 3.0)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_intro.mid")
