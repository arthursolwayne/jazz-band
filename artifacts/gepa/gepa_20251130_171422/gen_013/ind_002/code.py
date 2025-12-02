
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
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
# Fm = F, Ab, Bb, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Db
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
piano_notes = [
    # Bar 2 - Fm7
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=68, start=1.5, end=1.875),  # Db
    # Bar 3 - Bb7
    pretty_midi.Note(velocity=95, pitch=61, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=66, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625), # Ab
    # Bar 4 - Eb7
    pretty_midi.Note(velocity=95, pitch=59, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.375),  # Db
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

# Dante: saxophone motif
# F, Ab, Bb, F (melody)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=105, pitch=66, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=105, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=105, pitch=66, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=105, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=105, pitch=66, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=105, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=105, pitch=66, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=105, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=5.75, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
