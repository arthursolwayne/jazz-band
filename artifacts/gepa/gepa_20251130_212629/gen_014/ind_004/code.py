
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
    (36, 0.0, 0.375),    # Kick on 1
    (38, 0.5, 0.375),    # Snare on 2
    (42, 0.0, 0.1875),   # Hihat on 1
    (42, 0.1875, 0.1875),# Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875),# Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),# Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (36, 1.5, 0.375),    # Kick on 3
    (38, 2.0, 0.375),    # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Bass starts walking line with chromatic approach
bass_notes = [
    (62, 1.5, 0.375),     # D
    (63, 1.875, 0.375),   # Eb (chromatic approach)
    (60, 2.25, 0.375),    # B
    (62, 2.625, 0.375),   # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    (64, 1.875, 0.375),   # G7 (B, D, F, G)
    (66, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (64, 2.625, 0.375),
    (66, 2.625, 0.375),
    (67, 2.625, 0.375),
    (69, 2.625, 0.375),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Melody starts in bar 2
sax_notes = [
    (65, 1.5, 0.5),       # E (start of motif)
    (67, 2.0, 0.5),       # G
    (65, 2.5, 0.5),       # E
    (64, 3.0, 0.5),       # D (leaving it hanging)
    (65, 3.5, 0.5),       # E (return)
    (67, 4.0, 0.5),       # G
    (65, 4.5, 0.5),       # E
    (64, 5.0, 0.5),       # D (ends on a question)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bar 3 and 4: Continue bass, piano, and sax with variation

# Bass continues walking
bass_notes = [
    (64, 3.0, 0.375),     # C
    (65, 3.375, 0.375),   # C#
    (62, 3.75, 0.375),    # B
    (64, 4.125, 0.375),   # C
    (65, 4.5, 0.375),     # C#
    (62, 4.875, 0.375),   # B
    (64, 5.25, 0.375),    # C
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano continues comping
piano_notes = [
    (64, 3.0, 0.375),
    (66, 3.0, 0.375),
    (67, 3.0, 0.375),
    (69, 3.0, 0.375),
    (64, 3.5, 0.375),
    (66, 3.5, 0.375),
    (67, 3.5, 0.375),
    (69, 3.5, 0.375),
    (64, 4.0, 0.375),
    (66, 4.0, 0.375),
    (67, 4.0, 0.375),
    (69, 4.0, 0.375),
    (64, 4.5, 0.375),
    (66, 4.5, 0.375),
    (67, 4.5, 0.375),
    (69, 4.5, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax continues with variation
sax_notes = [
    (64, 3.0, 0.375),     # D
    (67, 3.375, 0.375),   # G
    (64, 3.75, 0.375),    # D
    (62, 4.125, 0.375),   # B
    (64, 4.5, 0.375),     # D
    (67, 4.875, 0.375),   # G
    (64, 5.25, 0.375),    # D
    (62, 5.625, 0.375),   # B
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Drums continue with same pattern
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (38, 2.0, 0.375),    # Snare on 2
    (42, 1.5, 0.1875),   # Hihat on 1
    (42, 1.6875, 0.1875),# Hihat on &
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875),# Hihat on &
    (42, 2.25, 0.1875),  # Hihat on 3
    (42, 2.4375, 0.1875),# Hihat on &
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 3.0, 0.375),    # Kick on 1
    (38, 3.5, 0.375),    # Snare on 2
    (42, 3.0, 0.1875),   # Hihat on 1
    (42, 3.1875, 0.1875),# Hihat on &
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875),# Hihat on &
    (42, 3.75, 0.1875),  # Hihat on 3
    (42, 3.9375, 0.1875),# Hihat on &
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),    # Kick on 1
    (38, 5.0, 0.375),    # Snare on 2
    (42, 4.5, 0.1875),   # Hihat on 1
    (42, 4.6875, 0.1875),# Hihat on &
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875),# Hihat on &
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),# Hihat on &
    (42, 5.625, 0.1875), # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
