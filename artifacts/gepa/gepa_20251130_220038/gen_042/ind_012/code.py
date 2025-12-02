
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum sounds
kick = 36  # Kick drum
snare = 38  # Snare
hihat = 42  # Hi-hat

# ---------------------
# BAR 1: Little Ray alone (0.0 - 1.5s)
# Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time signature: 4/4, 160 BPM => 1 bar = 1.5s, beat = 0.375s, 1/8 = 0.1875s

drum_notes = [
    (kick, 0.0),     # Kick on 1
    (snare, 0.375),  # Snare on 2
    (kick, 0.75),    # Kick on 3
    (snare, 1.125)   # Snare on 4
]

# Add hihat on every eighth note
for i in range(8):
    hihat_time = i * 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.0625))

# Add the kick and snare
for pitch, start in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.0625))

# ---------------------
# BAR 2-4: Full quartet (1.5 - 6.0s)
# Time: 1.5 - 6.0s (4.5 seconds for 3 bars)

# ---------------------
# Marcus: Walking bass line (Dm7 - G7 - Cm7 - F7)
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb

# Walking line in Dm (Dm7 -> G7 -> Cm7 -> F7), using chromatic approaches

# Define the walking bass line (in quarter notes)
bass_notes = [
    (58, 1.5),  # D (Dm7 root)
    (60, 1.875),  # Eb (chromatic approach to G)
    (62, 2.25),  # F (G7 3rd)
    (64, 2.625),  # G (G7 root)

    (64, 2.625),  # G (G7 root)
    (66, 2.875),  # A (chromatic approach to Bb)
    (65, 3.125),  # Ab (Bb in Cm7)
    (62, 3.5),    # C (Cm7 root)

    (62, 3.5),    # C (Cm7 root)
    (64, 3.875),  # D (chromatic approach to Eb)
    (63, 4.25),   # D# (Eb in F7)
    (60, 4.625),  # F (F7 root)
]

for pitch, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# ---------------------
# Diane: Piano comping on 2 and 4 (Dm7 - G7 - Cm7 - F7)
# Root 7th chords, comp on the backbeats

piano_notes = [
    # Bar 2 (Dm7)
    (58, 1.875),  # D (root)
    (60, 1.875),  # F (7th)
    (62, 1.875),  # A (3rd)
    (64, 1.875),  # C (5th)

    # Bar 3 (G7)
    (67, 2.875),  # G (root)
    (69, 2.875),  # B (7th)
    (71, 2.875),  # D (3rd)
    (72, 2.875),  # F (5th)

    # Bar 4 (Cm7)
    (60, 3.875),  # C (root)
    (63, 3.875),  # Eb (7th)
    (67, 3.875),  # G (3rd)
    (70, 3.875),  # Bb (5th)

    # Bar 4 (F7)
    (58, 4.875),  # F (root)
    (61, 4.875),  # A (7th)
    (64, 4.875),  # C (3rd)
    (67, 4.875),  # Eb (5th)
]

for pitch, start in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# ---------------------
# Dante: Tenor sax (Motif in Dm7)
# Motif idea: D - F - Bb - D (Dm7 triad with tension)
# Start at 1.5s, leave it hanging, return to finish it on the last beat

# Bar 2: Start the motif
sax_notes = [
    (58, 1.5),   # D
    (60, 1.875), # F
    (62, 2.25),  # A
    (64, 2.625), # C (Dm7 root, 3rd, 5th, 7th)

    # Bar 3: Leave it hanging
    (64, 3.0),   # Wait (repeat C)
    (64, 3.375), # Wait (repeat C)
    (64, 3.75),  # Wait (repeat C)

    # Bar 4: Return and finish it
    (62, 4.5),   # A
    (60, 4.875), # F
    (58, 5.25),  # D
]

for pitch, start in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# ---------------------
# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_sax_intro.mid')
