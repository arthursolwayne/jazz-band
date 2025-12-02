
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1&
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625), # Hihat on 2&
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 3&
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 4&
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, sing, leave it hanging
# Motif: D (62) -> F# (66) -> A (69) -> D (62)
# Start at bar 2, play first two notes, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.4375, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=3.0), # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
