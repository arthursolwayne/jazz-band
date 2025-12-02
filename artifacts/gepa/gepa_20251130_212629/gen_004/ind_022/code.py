
import pretty_midi

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Upright Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42
# MIDI note numbers for Dm scale (D, Eb, F, G, A, Bb, C)
Dm_notes = [50, 51, 53, 55, 57, 58, 60]

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar duration = 1.5s, beat = 0.375s
# Bar 1: 0.0 - 1.5s
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3 (0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.1))

# Snare on 2 and 4 (0.375 and 1.125s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.1))

# Hi-hat on every 8th (0.0, 0.375, 0.75, 1.125)
for i in range(4):
    hi_hat_start = bar1_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hi_hat_start, end=hi_hat_start + 0.05))

# Bar 2: Full ensemble (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Marcus (bass): Walking line in Dm, chromatic approaches
# Dm: D (50), Eb (51), F (53), G (55), A (57), Bb (58), C (60)
# Start on D, walk up chromatically, then resolve

bass_notes = [
    (50, bar2_start, bar2_start + 0.25),        # D
    (51, bar2_start + 0.25, bar2_start + 0.5),   # Eb
    (53, bar2_start + 0.5, bar2_start + 0.75),   # F
    (55, bar2_start + 0.75, bar2_start + 1.0),   # G
    (57, bar2_start + 1.0, bar2_start + 1.25),   # A
    (58, bar2_start + 1.25, bar2_start + 1.5),   # Bb
    (60, bar2_start + 1.5, bar2_start + 1.75),   # C
    (55, bar2_start + 1.75, bar2_start + 2.0),   # G
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Diane (piano): 7th chords on 2 and 4, comp in Dm
# Dm7: D, F, A, C (50, 53, 57, 60)
# Play 7th chords on beats 2 and 4 (0.375 and 1.125 into the bar)

piano_notes = [
    (50, bar2_start + 0.375, bar2_start + 0.5),   # D
    (53, bar2_start + 0.375, bar2_start + 0.5),   # F
    (57, bar2_start + 0.375, bar2_start + 0.5),   # A
    (60, bar2_start + 0.375, bar2_start + 0.5),   # C
    (50, bar2_start + 1.125, bar2_start + 1.375), # D
    (53, bar2_start + 1.125, bar2_start + 1.375), # F
    (57, bar2_start + 1.125, bar2_start + 1.375), # A
    (60, bar2_start + 1.125, bar2_start + 1.375), # C
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end))

# Dante (sax): 4-bar motif, 1st bar is the intro. This is your moment.
# Start with a short motif: D, F, A, Bb (50, 53, 57, 58), then leave it hanging.

sax_notes = [
    (50, bar2_start, bar2_start + 0.375),  # D
    (53, bar2_start + 0.375, bar2_start + 0.75),  # F
    (57, bar2_start + 0.75, bar2_start + 1.125),  # A
    (58, bar2_start + 1.125, bar2_start + 1.5),   # Bb
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# Bar 3: Full ensemble (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Marcus (bass): Walk again, but continue the line
bass_notes = [
    (55, bar3_start, bar3_start + 0.25),        # G
    (57, bar3_start + 0.25, bar3_start + 0.5),   # A
    (58, bar3_start + 0.5, bar3_start + 0.75),   # Bb
    (60, bar3_start + 0.75, bar3_start + 1.0),   # C
    (55, bar3_start + 1.0, bar3_start + 1.25),   # G
    (57, bar3_start + 1.25, bar3_start + 1.5),   # A
    (58, bar3_start + 1.5, bar3_start + 1.75),   # Bb
    (60, bar3_start + 1.75, bar3_start + 2.0),   # C
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Diane (piano): 7th chords again
piano_notes = [
    (50, bar3_start + 0.375, bar3_start + 0.5),   # D
    (53, bar3_start + 0.375, bar3_start + 0.5),   # F
    (57, bar3_start + 0.375, bar3_start + 0.5),   # A
    (60, bar3_start + 0.375, bar3_start + 0.5),   # C
    (50, bar3_start + 1.125, bar3_start + 1.375), # D
    (53, bar3_start + 1.125, bar3_start + 1.375), # F
    (57, bar3_start + 1.125, bar3_start + 1.375), # A
    (60, bar3_start + 1.125, bar3_start + 1.375), # C
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end))

# Dante (sax): Repeat the motif, but finish it
sax_notes = [
    (50, bar3_start, bar3_start + 0.375),  # D
    (53, bar3_start + 0.375, bar3_start + 0.75),  # F
    (57, bar3_start + 0.75, bar3_start + 1.125),  # A
    (58, bar3_start + 1.125, bar3_start + 1.5),   # Bb
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# Bar 4: Full ensemble (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Marcus (bass): Walk again, but continue the line
bass_notes = [
    (55, bar4_start, bar4_start + 0.25),        # G
    (57, bar4_start + 0.25, bar4_start + 0.5),   # A
    (58, bar4_start + 0.5, bar4_start + 0.75),   # Bb
    (60, bar4_start + 0.75, bar4_start + 1.0),   # C
    (55, bar4_start + 1.0, bar4_start + 1.25),   # G
    (57, bar4_start + 1.25, bar4_start + 1.5),   # A
    (58, bar4_start + 1.5, bar4_start + 1.75),   # Bb
    (60, bar4_start + 1.75, bar4_start + 2.0),   # C
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Diane (piano): 7th chords again
piano_notes = [
    (50, bar4_start + 0.375, bar4_start + 0.5),   # D
    (53, bar4_start + 0.375, bar4_start + 0.5),   # F
    (57, bar4_start + 0.375, bar4_start + 0.5),   # A
    (60, bar4_start + 0.375, bar4_start + 0.5),   # C
    (50, bar4_start + 1.125, bar4_start + 1.375), # D
    (53, bar4_start + 1.125, bar4_start + 1.375), # F
    (57, bar4_start + 1.125, bar4_start + 1.375), # A
    (60, bar4_start + 1.125, bar4_start + 1.375), # C
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end))

# Dante (sax): Repeat the motif, but finish it
sax_notes = [
    (50, bar4_start, bar4_start + 0.375),  # D
    (53, bar4_start + 0.375, bar4_start + 0.75),  # F
    (57, bar4_start + 0.75, bar4_start + 1.125),  # A
    (58, bar4_start + 1.125, bar4_start + 1.5),   # Bb
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end))

# Add all the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
