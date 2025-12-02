
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
    # Hi-hats on every eighth note
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass - walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # A#
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4
# Use F7 (F A C E) on beat 2 and beat 4 of bar 2
# Comp on beat 2
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # E
    # Comp on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # E
]
piano.notes.extend(diane_notes)

# Dante on sax - short motif, whisper then cry
# Start with F (65), then Bb (62), then F# (66), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.25),
    # Come back and finish it with a descending line
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)

# Marcus continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=56, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=90, pitch=58, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=4.25, end=4.5),  # D#
]
bass.notes.extend(bass_notes)

# Diane continues comping on 2 and 4
# Use F7 again
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # E
]
piano.notes.extend(diane_notes)

# Little Ray continues with the same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hats on every eighth note
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

# Bar 4 (4.5 - 6.0s)

# Marcus continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=61, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),  # G#
    pretty_midi.Note(velocity=90, pitch=65, start=5.75, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Diane continues comping on 2 and 4
# Use F7 again
diane_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # E
]
piano.notes.extend(diane_notes)

# Dante finishes the melody with a return to F and a descending trill
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=61, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=55, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write('dante_russo_intro.mid')
