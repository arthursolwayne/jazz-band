
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=50, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0),
]
bass.notes.extend(bass_notes)

# Piano comp
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=59, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano comp
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.375),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=50, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=51, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano comp
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on every eighth
    hihat = [
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0),
    ]
    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
