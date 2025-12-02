
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=41, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),  # Eb
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Dante: Motif starts on beat 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=37, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=4.125),  # Eb
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),  # Eb
]
piano.notes.extend(piano_notes)

# Dante: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=39, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625),  # Eb
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0),  # Eb
]
piano.notes.extend(piano_notes)

# Dante: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),   # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
for bar in [3.0, 4.5]:
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=bar + 0.75, end=bar + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=bar + 1.875, end=bar + 2.0),
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=bar, end=bar + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.1875, end=bar + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.375, end=bar + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.5625, end=bar + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.75, end=bar + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.9375, end=bar + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 1.125, end=bar + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 1.3125, end=bar + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
