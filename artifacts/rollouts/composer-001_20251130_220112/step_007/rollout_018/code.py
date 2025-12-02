
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

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=54, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),  # D#
    pretty_midi.Note(velocity=80, pitch=61, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),  # G#
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=5.75, end=6.0),  # Bb
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=2.0),  # D7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=61, start=2.0, end=2.25),  # Bb7
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.5),  # C7
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.5),  # Bb7
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.5),
]

piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 (F, A, C, E) in first bar, then a descending line
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=110, pitch=76, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=79, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=110, pitch=76, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=110, pitch=74, start=5.75, end=6.0),  # A
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
