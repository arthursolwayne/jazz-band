
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),    # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),    # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),   # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # snare on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),    # snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),    # hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),    # hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),     # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),    # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),    # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),     # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),     # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),    # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),    # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),     # E
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),     # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),    # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),    # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),     # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),    # F7: F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),    # F7: Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),    # F7: E
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),    # F7: F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),    # F7: F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),    # F7: Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),    # F7: E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),    # F7: F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),    # F7: F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),    # F7: Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),    # F7: E
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),    # F7: F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: sax melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),    # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),   # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),    # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),    # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),   # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),    # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),    # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),   # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),    # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),    # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),   # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),   # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),    # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),    # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),    # hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),   # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),   # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),    # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),    # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),    # hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),   # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),   # hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),    # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
