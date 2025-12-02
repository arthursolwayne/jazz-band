
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Marcus: Walking bass line in D (F#-A-D-F)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=79, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (D7, B7, F#7, C#7)
piano_notes = [
    # D7 (2nd beat of bar 2)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),  # C#
    # B7 (4th beat of bar 2)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),  # A
    # F#7 (2nd beat of bar 3)
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=4.125),  # D
    # C#7 (4th beat of bar 3)
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875),  # B
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kicks (Bar 2-4)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare (Bar 2-4)
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    # Hi-hats (Bar 2-4)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Dante's sax melody: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (72), F# (76), A (79), B (81), C# (84), D (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.65),
    pretty_midi.Note(velocity=100, pitch=76, start=1.65, end=1.8),
    pretty_midi.Note(velocity=100, pitch=79, start=1.8, end=1.95),
    pretty_midi.Note(velocity=100, pitch=81, start=1.95, end=2.1),
    pretty_midi.Note(velocity=100, pitch=84, start=2.1, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4),
    pretty_midi.Note(velocity=100, pitch=76, start=2.4, end=2.55),
    pretty_midi.Note(velocity=100, pitch=79, start=2.55, end=2.7),
    pretty_midi.Note(velocity=100, pitch=81, start=2.7, end=2.85),
    pretty_midi.Note(velocity=100, pitch=84, start=2.85, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.15),
    pretty_midi.Note(velocity=100, pitch=76, start=3.15, end=3.3),
    pretty_midi.Note(velocity=100, pitch=79, start=3.3, end=3.45),
    pretty_midi.Note(velocity=100, pitch=81, start=3.45, end=3.6),
    pretty_midi.Note(velocity=100, pitch=84, start=3.6, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.9),
    pretty_midi.Note(velocity=100, pitch=76, start=3.9, end=4.05),
    pretty_midi.Note(velocity=100, pitch=79, start=4.05, end=4.2),
    pretty_midi.Note(velocity=100, pitch=81, start=4.2, end=4.35),
    pretty_midi.Note(velocity=100, pitch=84, start=4.35, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.65),
    pretty_midi.Note(velocity=100, pitch=76, start=4.65, end=4.8),
    pretty_midi.Note(velocity=100, pitch=79, start=4.8, end=4.95),
    pretty_midi.Note(velocity=100, pitch=81, start=4.95, end=5.1),
    pretty_midi.Note(velocity=100, pitch=84, start=5.1, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.4),
    pretty_midi.Note(velocity=100, pitch=76, start=5.4, end=5.55),
    pretty_midi.Note(velocity=100, pitch=79, start=5.55, end=5.7),
    pretty_midi.Note(velocity=100, pitch=81, start=5.7, end=5.85),
    pretty_midi.Note(velocity=100, pitch=84, start=5.85, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
