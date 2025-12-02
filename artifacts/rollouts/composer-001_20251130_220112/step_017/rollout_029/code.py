
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=36, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=37, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, make it sing
sax_notes = [
    # Bar 2 - start the motif
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # G (Fm7)
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # E (chromatic)
    # Bar 3 - leave it hanging, then come back
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # G (Fm7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # E (chromatic)
    # Bar 4 - finish it
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # F (resolve)
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # G (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
