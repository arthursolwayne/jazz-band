
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
    pretty_midi Note(36, 0.0, 0.375),
    pretty_midi Note(36, 1.125, 0.375),
    # Snare on 2 and 4
    pretty_midi Note(38, 0.75, 0.375),
    pretty_midi Note(38, 1.875, 0.375),
    # Hihat on every eighth
    pretty_midi Note(42, 0.0, 0.1875),
    pretty_midi Note(42, 0.1875, 0.1875),
    pretty_midi Note(42, 0.375, 0.1875),
    pretty_midi Note(42, 0.5625, 0.1875),
    pretty_midi Note(42, 0.75, 0.1875),
    pretty_midi Note(42, 0.9375, 0.1875),
    pretty_midi Note(42, 1.125, 0.1875),
    pretty_midi Note(42, 1.3125, 0.1875),
    pretty_midi Note(42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(62, 1.5, 0.375), # D
    pretty_midi.Note(63, 1.875, 0.375), # Eb
    pretty_midi.Note(60, 2.25, 0.375), # C
    pretty_midi.Note(62, 2.625, 0.375), # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(67, 1.875, 0.375), # F
    pretty_midi.Note(71, 1.875, 0.375), # Bb
    pretty_midi.Note(72, 1.875, 0.375), # B
    pretty_midi.Note(64, 1.875, 0.375), # G
    pretty_midi.Note(67, 2.625, 0.375), # F
    pretty_midi.Note(71, 2.625, 0.375), # Bb
    pretty_midi.Note(72, 2.625, 0.375), # B
    pretty_midi.Note(64, 2.625, 0.375), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, make it sing
sax_notes = [
    pretty_midi.Note(65, 1.5, 0.375), # E
    pretty_midi.Note(67, 1.875, 0.375), # F
    pretty_midi.Note(65, 2.25, 0.375), # E
    pretty_midi.Note(62, 2.625, 0.375), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(65, 3.0, 0.375), # E
    pretty_midi.Note(67, 3.375, 0.375), # F
    pretty_midi.Note(64, 3.75, 0.375), # G
    pretty_midi.Note(65, 4.125, 0.375), # E
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(67, 3.375, 0.375), # F
    pretty_midi.Note(71, 3.375, 0.375), # Bb
    pretty_midi.Note(72, 3.375, 0.375), # B
    pretty_midi.Note(64, 3.375, 0.375), # G
    pretty_midi.Note(67, 4.125, 0.375), # F
    pretty_midi.Note(71, 4.125, 0.375), # Bb
    pretty_midi.Note(72, 4.125, 0.375), # B
    pretty_midi.Note(64, 4.125, 0.375), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: continuation of motif
sax_notes = [
    pretty_midi.Note(67, 3.0, 0.375), # F
    pretty_midi.Note(65, 3.375, 0.375), # E
    pretty_midi.Note(62, 3.75, 0.375), # D
    pretty_midi.Note(65, 4.125, 0.375), # E
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(36, 3.0, 0.375),
    pretty_midi.Note(36, 4.125, 0.375),
    pretty_midi.Note(38, 3.375, 0.375),
    pretty_midi.Note(38, 4.5, 0.375),
    pretty_midi.Note(42, 3.0, 0.1875),
    pretty_midi.Note(42, 3.1875, 0.1875),
    pretty_midi.Note(42, 3.375, 0.1875),
    pretty_midi.Note(42, 3.5625, 0.1875),
    pretty_midi.Note(42, 3.75, 0.1875),
    pretty_midi.Note(42, 3.9375, 0.1875),
    pretty_midi.Note(42, 4.125, 0.1875),
    pretty_midi.Note(42, 4.3125, 0.1875),
    pretty_midi.Note(42, 4.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(62, 4.5, 0.375), # D
    pretty_midi.Note(64, 4.875, 0.375), # G
    pretty_midi.Note(62, 5.25, 0.375), # D
    pretty_midi.Note(60, 5.625, 0.375), # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(67, 4.875, 0.375), # F
    pretty_midi.Note(71, 4.875, 0.375), # Bb
    pretty_midi.Note(72, 4.875, 0.375), # B
    pretty_midi.Note(64, 4.875, 0.375), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: finish the motif
sax_notes = [
    pretty_midi.Note(62, 4.5, 0.375), # D
    pretty_midi.Note(65, 4.875, 0.375), # E
    pretty_midi.Note(67, 5.25, 0.375), # F
    pretty_midi.Note(65, 5.625, 0.375), # E
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(36, 4.5, 0.375),
    pretty_midi.Note(36, 5.625, 0.375),
    pretty_midi.Note(38, 4.875, 0.375),
    pretty_midi.Note(38, 6.0, 0.375),
    pretty_midi.Note(42, 4.5, 0.1875),
    pretty_midi.Note(42, 4.6875, 0.1875),
    pretty_midi.Note(42, 4.875, 0.1875),
    pretty_midi.Note(42, 5.0625, 0.1875),
    pretty_midi.Note(42, 5.25, 0.1875),
    pretty_midi.Note(42, 5.4375, 0.1875),
    pretty_midi.Note(42, 5.625, 0.1875),
    pretty_midi.Note(42, 5.8125, 0.1875),
    pretty_midi.Note(42, 6.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
