
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

# Bass line: Walking line in D, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.625),   # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=2.875, end=3.0),   # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=90, pitch=80, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=82, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=84, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=86, start=3.5, end=3.625),   # Bb
    pretty_midi.Note(velocity=90, pitch=88, start=3.625, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=89, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=91, start=3.875, end=4.0),   # C#
    pretty_midi.Note(velocity=90, pitch=93, start=4.0, end=4.125),   # D
    pretty_midi.Note(velocity=90, pitch=95, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=96, start=4.25, end=4.375),  # E
    pretty_midi.Note(velocity=90, pitch=98, start=4.375, end=4.5),   # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=98, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=90, pitch=99, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=90, pitch=101, start=4.75, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=103, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=105, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=107, start=5.125, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=108, start=5.25, end=5.375), # C
    pretty_midi.Note(velocity=90, pitch=110, start=5.375, end=5.5),  # C#
    pretty_midi.Note(velocity=90, pitch=112, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=114, start=5.625, end=5.75), # Eb
    pretty_midi.Note(velocity=90, pitch=115, start=5.75, end=5.875), # E
    pretty_midi.Note(velocity=90, pitch=117, start=5.875, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7: D, F#, A, C
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G7: G, B, D, F
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D7: D, F#, A, C
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif in D, make it sing, leave it hanging
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
