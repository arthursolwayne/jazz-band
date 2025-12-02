
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
    # Kick on 1 and 3
    (36, 0.0, 0.375), (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375), (38, 2.25, 0.375),
    # Hi-hat on every eighth
    (42, 0.0, 0.1875), (42, 0.1875, 0.1875), (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875), (42, 0.75, 0.1875), (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Cm7 (Fm7) - Bb - Ab - G (melodic motif)
sax_notes = [
    (60, 1.5, 0.375),  # C
    (62, 1.875, 0.375), # Bb
    (58, 2.25, 0.375),  # Ab
    (59, 2.625, 0.375)  # G
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Fm
bass_notes = [
    (44, 1.5, 0.375),  # F
    (45, 1.875, 0.375), # Gb
    (46, 2.25, 0.375),  # Ab
    (43, 2.625, 0.375)  # Eb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: Comp on 2 and 4 (Ab7)
piano_notes = [
    (57, 1.875, 0.375),  # Ab
    (60, 1.875, 0.375),  # C
    (62, 1.875, 0.375),  # Db
    (64, 1.875, 0.375),  # Eb
    (57, 2.625, 0.375),  # Ab
    (60, 2.625, 0.375),  # C
    (62, 2.625, 0.375),  # Db
    (64, 2.625, 0.375)   # Eb
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Ab - G - F - Eb (melodic continuation)
sax_notes = [
    (58, 3.0, 0.375),  # Ab
    (59, 3.375, 0.375), # G
    (60, 3.75, 0.375),  # F
    (57, 4.125, 0.375)  # Eb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Fm
bass_notes = [
    (50, 3.0, 0.375),  # Bb
    (51, 3.375, 0.375), # B
    (52, 3.75, 0.375),  # C
    (50, 4.125, 0.375)  # Bb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: Comp on 2 and 4 (Ab7)
piano_notes = [
    (57, 3.375, 0.375),  # Ab
    (60, 3.375, 0.375),  # C
    (62, 3.375, 0.375),  # Db
    (64, 3.375, 0.375),  # Eb
    (57, 4.125, 0.375),  # Ab
    (60, 4.125, 0.375),  # C
    (62, 4.125, 0.375),  # Db
    (64, 4.125, 0.375)   # Eb
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F - Eb - D - C (resolve the motif)
sax_notes = [
    (60, 4.5, 0.375),  # F
    (57, 4.875, 0.375), # Eb
    (55, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Fm
bass_notes = [
    (53, 4.5, 0.375),  # C
    (50, 4.875, 0.375), # Bb
    (48, 5.25, 0.375),  # Ab
    (44, 5.625, 0.375)  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: Comp on 2 and 4 (Ab7)
piano_notes = [
    (57, 4.875, 0.375),  # Ab
    (60, 4.875, 0.375),  # C
    (62, 4.875, 0.375),  # Db
    (64, 4.875, 0.375),  # Eb
    (57, 5.625, 0.375),  # Ab
    (60, 5.625, 0.375),  # C
    (62, 5.625, 0.375),  # Db
    (64, 5.625, 0.375)   # Eb
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (36, 5.625, 0.375),
    (38, 4.875, 0.375), (38, 6.0, 0.375),
    (42, 4.5, 0.1875), (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
