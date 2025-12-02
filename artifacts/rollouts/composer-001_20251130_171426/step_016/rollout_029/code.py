
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F#
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F#
]

# Sax: short motif, start it, leave it hanging, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # D
]

# Bar 3 (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F#
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F#
])

# Sax: continuation of motif
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),   # D
])

# Bar 4 (4.5 - 6.0s)
# Bass: walking line, chromatic approaches
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # F#
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=6.0, end=6.375),   # B
    pretty_midi.Note(velocity=90, pitch=65, start=6.0, end=6.375),   # F#
])

# Sax: finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),    # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),    # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),    # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),    # E
])

# Add all notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
