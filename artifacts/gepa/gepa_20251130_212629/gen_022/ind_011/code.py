
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # kick on 1
    (42, 0.125, 0.25), # hihat on &1
    (38, 0.5, 0.375),  # snare on 2
    (42, 0.625, 0.25), # hihat on &2
    (36, 0.875, 0.375), # kick on 3
    (42, 1.0, 0.25),   # hihat on &3
    (38, 1.375, 0.375), # snare on 4
    (42, 1.5, 0.25)    # hihat on &4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Sax enters with motif, bass starts walking, piano comps
# Dm7 chord: D F A C
# Sax motif: D, F#, Bb, rest (a chromatic descent with a twist)

sax_notes = [
    (62, 1.5, 0.375),  # D
    (66, 2.125, 0.375), # F#
    (60, 2.75, 0.375),  # Bb
    (62, 3.125, 0.375)  # D (rest is 0.375s)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Marcus - Walking bass line in Dm
# Dm -> C -> Bb -> A -> G -> F -> E -> D -> C -> Bb -> A -> G -> F -> E -> D -> C
# Timings in 16th notes, 0.1875s per 16th

bass_notes = [
    (50, 1.5, 0.1875), # D
    (48, 1.6875, 0.1875), # C
    (52, 1.875, 0.1875), # Bb
    (55, 2.0625, 0.1875), # A
    (53, 2.25, 0.1875), # G
    (51, 2.4375, 0.1875), # F
    (49, 2.625, 0.1875), # E
    (50, 2.8125, 0.1875), # D
    (48, 2.8125, 0.1875), # C
    (52, 3.0, 0.1875), # Bb
    (55, 3.1875, 0.1875), # A
    (53, 3.375, 0.1875), # G
    (51, 3.5625, 0.1875), # F
    (49, 3.75, 0.1875), # E
    (50, 3.9375, 0.1875), # D
    (48, 4.125, 0.1875)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - piano: Dm7 on beats 2 and 4 (D F A C)
piano_notes = [
    (50, 2.0, 0.375), # D
    (52, 2.0, 0.375), # F
    (55, 2.0, 0.375), # A
    (57, 2.0, 0.375), # C
    (50, 4.0, 0.375), # D
    (52, 4.0, 0.375), # F
    (55, 4.0, 0.375), # A
    (57, 4.0, 0.375)  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full band continues with rhythmic tension
# Sax plays a variation of the motif
sax_notes = [
    (62, 4.5, 0.375),  # D
    (66, 5.125, 0.375), # F#
    (60, 5.75, 0.375),  # Bb
    (62, 6.125, 0.375)  # D (rest is 0.375s)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Marcus - walking line continues
bass_notes = [
    (50, 4.5, 0.1875), # D
    (48, 4.6875, 0.1875), # C
    (52, 4.875, 0.1875), # Bb
    (55, 5.0625, 0.1875), # A
    (53, 5.25, 0.1875), # G
    (51, 5.4375, 0.1875), # F
    (49, 5.625, 0.1875), # E
    (50, 5.8125, 0.1875), # D
    (48, 5.8125, 0.1875), # C
    (52, 6.0, 0.1875), # Bb
    (55, 6.1875, 0.1875), # A
    (53, 6.375, 0.1875), # G
    (51, 6.5625, 0.1875), # F
    (49, 6.75, 0.1875), # E
    (50, 6.9375, 0.1875), # D
    (48, 7.125, 0.1875)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - piano: Dm7 on beats 2 and 4 (D F A C)
piano_notes = [
    (50, 5.0, 0.375), # D
    (52, 5.0, 0.375), # F
    (55, 5.0, 0.375), # A
    (57, 5.0, 0.375), # C
    (50, 7.0, 0.375), # D
    (52, 7.0, 0.375), # F
    (55, 7.0, 0.375), # A
    (57, 7.0, 0.375)  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: End with a question, leave the last note hanging
# Sax plays the motif again, but ends on a rest
sax_notes = [
    (62, 7.5, 0.375),  # D
    (66, 8.125, 0.375), # F#
    (60, 8.75, 0.375),  # Bb
    (62, 9.125, 0.375)  # D (rest is 0.375s)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Marcus - walking line continues
bass_notes = [
    (50, 7.5, 0.1875), # D
    (48, 7.6875, 0.1875), # C
    (52, 7.875, 0.1875), # Bb
    (55, 8.0625, 0.1875), # A
    (53, 8.25, 0.1875), # G
    (51, 8.4375, 0.1875), # F
    (49, 8.625, 0.1875), # E
    (50, 8.8125, 0.1875), # D
    (48, 8.8125, 0.1875), # C
    (52, 9.0, 0.1875), # Bb
    (55, 9.1875, 0.1875), # A
    (53, 9.375, 0.1875), # G
    (51, 9.5625, 0.1875), # F
    (49, 9.75, 0.1875), # E
    (50, 9.9375, 0.1875), # D
    (48, 10.125, 0.1875)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - piano: Dm7 on beats 2 and 4 (D F A C)
piano_notes = [
    (50, 8.0, 0.375), # D
    (52, 8.0, 0.375), # F
    (55, 8.0, 0.375), # A
    (57, 8.0, 0.375), # C
    (50, 10.0, 0.375), # D
    (52, 10.0, 0.375), # F
    (55, 10.0, 0.375), # A
    (57, 10.0, 0.375)  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray - Bar 4: Full drum pattern
drum_notes = [
    (36, 7.5, 0.375),  # kick on 1
    (42, 7.625, 0.25), # hihat on &1
    (38, 8.0, 0.375),  # snare on 2
    (42, 8.125, 0.25), # hihat on &2
    (36, 8.375, 0.375), # kick on 3
    (42, 8.5, 0.25),   # hihat on &3
    (38, 8.875, 0.375), # snare on 4
    (42, 9.0, 0.25)    # hihat on &4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro.mid")
