
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (MIDI note numbers):
# Kick: 36, Snare: 38, Hi-hat: 42

# ----------------------------
# Bar 1: Little Ray on drums only
# ----------------------------

# Bar 1: 4 beats
bar1_start = 0.0
bar1_duration = 1.5  # 60 / 160 * 4 = 1.5 seconds

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=bar1_start + 0.75 * 2, end=bar1_start + 0.75 * 2 + 0.375))

# Hi-hat on every eighth
for i in range(8):
    note_start = bar1_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=note_start, end=note_start + 0.1875))

# ----------------------------
# Bar 2: Full ensemble
# ----------------------------

# Bar 2 starts at 1.5s
bar2_start = bar1_duration

# Bass line (Marcus) - walking line in Fm (F, Gb, Ab, Bb)
# Fm = F, Ab, Bb, Db (4th chord), chromatic approach on 2 and 3
bass_notes = [
    (bar2_start, 65),   # F (65)
    (bar2_start + 0.375, 63),  # Eb (chromatic approach)
    (bar2_start + 0.75, 64),   # E (chromatic approach)
    (bar2_start + 1.125, 62),  # D (Ab)
    (bar2_start + 1.5, 62),    # Ab (62)
    (bar2_start + 1.875, 60),  # G (chromatic)
    (bar2_start + 2.25, 61),   # G#
    (bar2_start + 2.625, 59),  # Gb (Bb)
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano (Diane) - 7th chords on 2 and 4
# Fm7 = F, Ab, Bb, Db
# 2nd beat (0.375s): Fm7
# 4th beat (1.125s): Bb7 (sub dominant)
piano_notes = [
    (bar2_start + 0.375, 65),  # F
    (bar2_start + 0.375, 62),  # Ab
    (bar2_start + 0.375, 62),  # Bb (same as 62? 62 is Bb, 60 is Bb?)
    (bar2_start + 0.375, 59),  # Db

    (bar2_start + 1.125, 60),  # Bb
    (bar2_start + 1.125, 67),  # D
    (bar2_start + 1.125, 67),  # Db (67 is D, 65 is F, 67 is D, 62 is Ab)
    (bar2_start + 1.125, 62),  # Ab
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Saxophone (Dante) - melody
# Start on F (65), then Ab (62), then Bb (62?), then F (65)
# Use a motif with a bit of tension: F, Ab, Bb, F
# Time for each note: 0.75s (quarter note)
sax_notes = [
    (bar2_start, 65),  # F
    (bar2_start + 0.75, 62),  # Ab
    (bar2_start + 1.5, 62),  # Bb
    (bar2_start + 2.25, 65),  # F
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# ----------------------------
# Bar 3: Full ensemble again (same as Bar 2)
# ----------------------------
# Just repeat the same bar for continuity

# Bass line again
bar3_start = bar2_start + bar1_duration
bass_notes = [
    (bar3_start, 65),   # F
    (bar3_start + 0.375, 63),  # Eb
    (bar3_start + 0.75, 64),   # E
    (bar3_start + 1.125, 62),  # D (Ab)
    (bar3_start + 1.5, 62),    # Ab
    (bar3_start + 1.875, 60),  # G
    (bar3_start + 2.25, 61),   # G#
    (bar3_start + 2.625, 59),  # Gb (Bb)
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano again (same as Bar 2)
piano_notes = [
    (bar3_start + 0.375, 65),  # F
    (bar3_start + 0.375, 62),  # Ab
    (bar3_start + 0.375, 62),  # Bb
    (bar3_start + 0.375, 59),  # Db

    (bar3_start + 1.125, 60),  # Bb
    (bar3_start + 1.125, 67),  # D
    (bar3_start + 1.125, 67),  # Db
    (bar3_start + 1.125, 62),  # Ab
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Saxophone: same motif but with a slight variation at the end
sax_notes = [
    (bar3_start, 65),  # F
    (bar3_start + 0.75, 62),  # Ab
    (bar3_start + 1.5, 62),  # Bb
    (bar3_start + 2.25, 65),  # F
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# ----------------------------
# Bar 4: Full ensemble again (same as Bar 2 and 3)
# ----------------------------
bar4_start = bar3_start + bar1_duration

# Bass line again
bass_notes = [
    (bar4_start, 65),   # F
    (bar4_start + 0.375, 63),  # Eb
    (bar4_start + 0.75, 64),   # E
    (bar4_start + 1.125, 62),  # D (Ab)
    (bar4_start + 1.5, 62),    # Ab
    (bar4_start + 1.875, 60),  # G
    (bar4_start + 2.25, 61),   # G#
    (bar4_start + 2.625, 59),  # Gb (Bb)
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano again
piano_notes = [
    (bar4_start + 0.375, 65),  # F
    (bar4_start + 0.375, 62),  # Ab
    (bar4_start + 0.375, 62),  # Bb
    (bar4_start + 0.375, 59),  # Db

    (bar4_start + 1.125, 60),  # Bb
    (bar4_start + 1.125, 67),  # D
    (bar4_start + 1.125, 67),  # Db
    (bar4_start + 1.125, 62),  # Ab
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Saxophone: same motif, but with a slight pause at the end to let it hang
sax_notes = [
    (bar4_start, 65),  # F
    (bar4_start + 0.75, 62),  # Ab
    (bar4_start + 1.5, 62),  # Bb
    (bar4_start + 2.25, 65),  # F
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_intro.mid")
