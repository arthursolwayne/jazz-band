
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Fm7: F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bass line (walking chromatic line on Fm)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=39, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),  # B
]
bass.notes.extend(bass_notes)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # E
    # Bar 3: F7 on 2
    pretty_midi.Note(velocity=80, pitch=53, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=90, pitch=49, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.25, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 3: F7 on 2
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # E
    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=80, pitch=53, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # E
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=5.75, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # E
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=i * 1.5, end=i * 1.5 + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=i * 1.5 + 0.75, end=i * 1.5 + 0.875),
        pretty_midi.Note(velocity=100, pitch=36, start=i * 1.5 + 1.125, end=i * 1.5 + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=i * 1.5 + 1.875, end=i * 1.5 + 2.0),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5, end=i * 1.5 + 0.375),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 0.375, end=i * 1.5 + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 0.75, end=i * 1.5 + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 1.125, end=i * 1.5 + 1.5),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 1.5, end=i * 1.5 + 1.875),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 1.875, end=i * 1.5 + 2.25),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 2.25, end=i * 1.5 + 2.625),
        pretty_midi.Note(velocity=100, pitch=42, start=i * 1.5 + 2.625, end=i * 1.5 + 3.0),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
