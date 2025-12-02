
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

# Bass line (Marcus)
# Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # F
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # F
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # F
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # F
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # F
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # F
]
piano.notes.extend(piano_notes)

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Bb - F (1 bar)
# Then leave it hanging for a beat, then return with the same motif an octave higher
sax_notes = [
    # Bar 2, beat 1: F
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),
    # Bar 2, beat 2: G
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),
    # Bar 2, beat 3: Bb
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625),
    # Bar 2, beat 4: F (end of motif)
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),
    # Bar 3, beat 1: Leave it hanging (rest)
    # Bar 3, beat 2: F (octave higher)
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75),
    # Bar 3, beat 3: G (octave higher)
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125),
    # Bar 3, beat 4: Bb (octave higher)
    pretty_midi.Note(velocity=110, pitch=73, start=4.125, end=4.5),
    # Bar 4, beat 1: F (octave higher, end of motif)
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Hi-hat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
