
import pretty_midi

# Initialize a PrettyMIDI object with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle, textured, with space and shading
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use dynamic variation (velocity) to add texture
drum_notes = [
    (bar1_start + 0.0, KICK, 70),     # Kick on beat 1
    (bar1_start + 0.5, HIHAT, 90),    # Hi-hat on &1
    (bar1_start + 1.0, SNARE, 80),    # Snare on beat 2
    (bar1_start + 1.5, HIHAT, 85),    # Hi-hat on &2
    (bar1_start + 2.0, KICK, 65),     # Kick on beat 3
    (bar1_start + 2.5, HIHAT, 85),    # Hi-hat on &3
    (bar1_start + 3.0, SNARE, 90),    # Snare on beat 4
    (bar1_start + 3.5, HIHAT, 90),    # Hi-hat on &4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Saxophone: Your one short, emotional motif
# Fm key: F, Ab, Bb, D, Eb, G, A (but we'll pull from this for the motif)
# Fm7 (F, Ab, Bb, D) => we'll use F, Ab, Bb, D
# Motif: F -> Ab -> Bb -> D -> rest -> F -> Ab
# Make it sing — no runs, just emotion and space
sax_notes = [
    (bar2_start + 0.0, 65, 100),   # F (65)
    (bar2_start + 0.375, 76, 100),  # Ab (76)
    (bar2_start + 0.75, 71, 100),   # Bb (71)
    (bar2_start + 1.125, 69, 100),  # D (69)
    (bar2_start + 1.5, 65, 100),    # F (again)
    (bar2_start + 1.875, 76, 100),  # Ab (again)
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass: Marcus — walking line, chromatic approaches, no repeated notes
# Fm key: F, Gb, Ab, Bb, B, C, Db, D
# Bass line: F -> Gb -> Ab -> Bb -> B -> C -> Db -> D (and repeat with variation)
# Use melodic phrasing, not just rhythm

bass_notes = [
    (bar2_start + 0.0, 65, 80),     # F
    (bar2_start + 0.375, 66, 80),   # Gb
    (bar2_start + 0.75, 71, 80),    # Ab
    (bar2_start + 1.125, 70, 80),   # Bb
    (bar2_start + 1.5, 71, 80),     # B
    (bar2_start + 1.875, 67, 80),   # C
    (bar2_start + 2.25, 69, 80),    # Db
    (bar2_start + 2.625, 69, 80),   # D

    (bar3_start + 0.0, 70, 85),     # Bb
    (bar3_start + 0.375, 71, 85),   # B
    (bar3_start + 0.75, 69, 85),    # Db
    (bar3_start + 1.125, 67, 85),   # C
    (bar3_start + 1.5, 65, 85),     # F
    (bar3_start + 1.875, 66, 85),   # Gb
    (bar3_start + 2.25, 71, 85),    # Ab
    (bar3_start + 2.625, 70, 85),   # Bb

    (bar4_start + 0.0, 70, 80),     # Bb
    (bar4_start + 0.375, 71, 80),   # B
    (bar4_start + 0.75, 69, 80),    # Db
    (bar4_start + 1.125, 67, 80),   # C
    (bar4_start + 1.5, 65, 80),     # F
    (bar4_start + 1.875, 66, 80),   # Gb
    (bar4_start + 2.25, 71, 80),    # Ab
    (bar4_start + 2.625, 70, 80),   # Bb
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: Diane — emotional, with tension, 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Play chord on beat 2 and 4, with emotional tension in each

piano_notes = [
    (bar2_start + 1.0, 65, 100),   # F
    (bar2_start + 1.0, 76, 100),   # Ab
    (bar2_start + 1.0, 71, 100),   # Bb
    (bar2_start + 1.0, 69, 100),   # D
    (bar2_start + 3.0, 65, 100),   # F
    (bar2_start + 3.0, 76, 100),   # Ab
    (bar2_start + 3.0, 71, 100),   # Bb
    (bar2_start + 3.0, 69, 100),   # D

    (bar3_start + 1.0, 65, 105),   # F (slightly louder)
    (bar3_start + 1.0, 76, 105),   # Ab
    (bar3_start + 1.0, 71, 105),   # Bb
    (bar3_start + 1.0, 69, 105),   # D
    (bar3_start + 3.0, 65, 105),   # F
    (bar3_start + 3.0, 76, 105),   # Ab
    (bar3_start + 3.0, 71, 105),   # Bb
    (bar3_start + 3.0, 69, 105),   # D
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_quartet_intro.mid")
