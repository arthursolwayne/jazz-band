
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
# Fm7 chord: F, Ab, C, D
# Walking bass line in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, D
# Bb7: Bb, D, F, Ab
# Fm7: F, Ab, C, D
# Bb7: Bb, D, F, Ab
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4: Fm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F - Gb - Ab (start), then leave it hanging, then come back with F - Gb - Ab - A

# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=63, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=1.875),  # Ab
]

# Bar 3: Leave it hanging (no notes)
# Bar 4: Come back and finish
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=63, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=61, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),   # A
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
