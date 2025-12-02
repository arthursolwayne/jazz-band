
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (42, 0.125, 0.125), (42, 0.25, 0.125), (42, 0.375, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.375),
    (42, 1.25, 0.125), (42, 1.375, 0.125), (42, 1.5, 0.125)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line, chromatic approaches, never same note twice
# Fm7 chord: F, Ab, C, Eb
# Walking bass line: F -> Gb -> Ab -> A -> Bb -> B -> C -> Db -> Eb -> F
bass_notes = [
    (53, 1.5, 0.375), # F
    (52, 1.875, 0.375), # Gb
    (51, 2.25, 0.375), # Ab
    (50, 2.625, 0.375), # A
    (48, 2.875, 0.375), # Bb
    (47, 3.25, 0.375), # B
    (53, 3.625, 0.375), # C
    (52, 3.875, 0.375)  # Db
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# Fm7 chord: F (53), Ab (51), C (58), Eb (50)
# Comp on 2 and 4
piano_notes = [
    (53, 1.875, 0.375), # F
    (51, 1.875, 0.375), # Ab
    (58, 1.875, 0.375), # C
    (50, 1.875, 0.375), # Eb

    (53, 3.0, 0.375), # F
    (51, 3.0, 0.375), # Ab
    (58, 3.0, 0.375), # C
    (50, 3.0, 0.375)  # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax — short motif, start it, leave it hanging, finish it
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F (66) -> Gb (65) -> Ab (64), then rest
# Then return later to complete it
sax_notes = [
    (66, 1.5, 0.25), # F
    (65, 1.75, 0.25), # Gb
    (64, 2.0, 0.25), # Ab
    (66, 3.75, 0.25), # F
    (65, 4.0, 0.25), # Gb
    (64, 4.25, 0.25)  # Ab
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line continues
# F -> Gb -> Ab -> A -> Bb -> B -> C -> Db -> Eb -> F
bass_notes = [
    (50, 3.375, 0.375), # A
    (48, 3.75, 0.375), # Bb
    (47, 4.125, 0.375), # B
    (53, 4.5, 0.375), # C
    (52, 4.875, 0.375), # Db
    (51, 5.25, 0.375), # Ab
    (50, 5.625, 0.375), # A
    (48, 6.0, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# Fm7 chord: F (53), Ab (51), C (58), Eb (50)
# Comp on 2 and 4
piano_notes = [
    (53, 3.875, 0.375), # F
    (51, 3.875, 0.375), # Ab
    (58, 3.875, 0.375), # C
    (50, 3.875, 0.375), # Eb

    (53, 4.5, 0.375), # F
    (51, 4.5, 0.375), # Ab
    (58, 4.5, 0.375), # C
    (50, 4.5, 0.375)  # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Motif continues — the rest is still hanging
# Leave the motif as is for now, just end the bar with the last note

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line continues
# F -> Gb -> Ab -> A -> Bb -> B -> C -> Db -> Eb -> F
bass_notes = [
    (51, 4.875, 0.375), # Ab
    (50, 5.25, 0.375), # A
    (48, 5.625, 0.375), # Bb
    (47, 6.0, 0.375)  # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# Fm7 chord: F (53), Ab (51), C (58), Eb (50)
# Comp on 2 and 4
piano_notes = [
    (53, 5.25, 0.375), # F
    (51, 5.25, 0.375), # Ab
    (58, 5.25, 0.375), # C
    (50, 5.25, 0.375), # Eb

    (53, 5.875, 0.375), # F
    (51, 5.875, 0.375), # Ab
    (58, 5.875, 0.375), # C
    (50, 5.875, 0.375)  # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Complete the motif on the last bar
sax_notes = [
    (66, 5.0, 0.25), # F
    (65, 5.25, 0.25), # Gb
    (64, 5.5, 0.25), # Ab
    (66, 5.75, 0.25), # F
    (65, 6.0, 0.25), # Gb
    (64, 6.25, 0.25)  # Ab
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.125),
    (42, 3.125, 0.125), (42, 3.25, 0.125), (42, 3.375, 0.125),
    (36, 4.125, 0.375), (38, 4.5, 0.375), (42, 4.125, 0.375),
    (42, 4.25, 0.125), (42, 4.375, 0.125), (42, 4.5, 0.125),

    # Bar 4
    (36, 4.875, 0.375), (38, 5.25, 0.375), (42, 4.875, 0.125),
    (42, 4.999, 0.125), (42, 5.125, 0.125), (42, 5.25, 0.125),
    (36, 5.875, 0.375), (38, 6.25, 0.375), (42, 5.875, 0.375),
    (42, 6.0, 0.125), (42, 6.125, 0.125), (42, 6.25, 0.125)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
