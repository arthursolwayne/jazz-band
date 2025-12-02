
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),  # G#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # C
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # C
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: Motif in F - start, leave it hanging, come back and finish it
# Bar 2: Begin motif (F -> A -> G -> F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=59, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=59, start=2.625, end=3.0),   # F
    # Bar 3: Leave it hanging (rest)
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # G
    # Bar 4: Return and finish it (F -> A -> G -> F)
    pretty_midi.Note(velocity=110, pitch=59, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.625),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
