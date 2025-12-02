
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    # Bar 2: F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # Ab
    # Bar 3: Bb -> B -> C -> C#
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # C#
    # Bar 4: D -> Eb -> E -> F
    pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25), # Bb
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75), # Bb
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=5.875), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=5.875), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=5.875), # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif in F, short and haunting
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),  # A
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),  # A
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125), # Snare 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625), # Snare 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125), # Snare 2
    pretty_midi.Note(velocity=110, pitch=38, start=5.5, end=5.625), # Snare 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
