
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches in Fm
bass_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=35, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=34, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),   # F

    # Bar 3: Fm7
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=35, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=34, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),   # F

    # Bar 4: Fm7
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=35, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=34, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2: Comp on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=35, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.625),  # F
    # Bar 3: Comp on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),   # Bb7
    pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=35, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),   # F
    # Bar 4: Comp on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),   # Bb7
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=35, start=5.625, end=6.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),   # F
]
piano.notes.extend(piano_notes)

# Sax (Dante) - One short motif, leave it hanging, then come back
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),   # Ab
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),    # C
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),   # C
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Finalize
midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
