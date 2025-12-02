
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # D
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - motif: F - Ab - C - Eb, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # Eb
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.625),  # F
]
sax.notes.extend(sax_notes)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.dump()
