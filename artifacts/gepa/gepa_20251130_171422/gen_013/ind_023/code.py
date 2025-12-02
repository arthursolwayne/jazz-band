
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

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.125), # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.125, end=2.5), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.875), # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=2.875, end=3.125), # G
    pretty_midi.Note(velocity=80, pitch=66, start=3.125, end=3.375), # Ab
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125), # E
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.375, end=4.625), # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.625, end=5.0), # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.375), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=81, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=80, pitch=79, start=1.5, end=1.875), # Eb
    # Bar 3: rest
    pretty_midi.Note(velocity=60, pitch=76, start=2.875, end=3.125), # F
    pretty_midi.Note(velocity=60, pitch=81, start=2.875, end=3.125), # A
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.375), # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.0, end=5.375), # A
    pretty_midi.Note(velocity=80, pitch=78, start=5.0, end=5.375), # C
    pretty_midi.Note(velocity=80, pitch=79, start=5.0, end=5.375), # Eb
]
piano.notes.extend(piano_notes)

# Sax: Melody in Fm. One short motif, make it sing.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0), # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=74, start=2.875, end=3.125), # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.125, end=3.375), # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.125), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.125, end=5.375), # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=5.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.75),
    pretty_midi.Note(velocity=110, pitch=38, start=5.75, end=6.0),
]
# Add hihat every eighth
for i in range(1.5, 6.0, 0.375):
    pretty_midi.Note(velocity=80, pitch=42, start=i, end=i + 0.1875)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("f_minor_intro.mid")
