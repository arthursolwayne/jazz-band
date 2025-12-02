
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starting on D (D, F#, B) in 8th notes
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]

# Bass: Walking line in D minor (D, C, B, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),  # A
]

# Piano: 7th chords on 2 and 4, D7 on 2, Bm7 on 4
piano_notes = [
    # D7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C
    # Bm7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # D#
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # G
]

# Drums for Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif again, transposed down a half step (C#, E, A)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C#
])

# Bass: Walking line in D minor (D, C, B, A)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),   # A
])

# Piano: 7th chords on 2 and 4, Bm7 on 2, F#7 on 4
piano_notes.extend([
    # Bm7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),   # D#
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),   # F#
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),   # G
    # F#7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),    # F#
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),    # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),    # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),    # D
])

# Drums for Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif again, transposed down a half step (C#, E, A)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C#
])

# Bass: Walking line in D minor (D, C, B, A)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),   # A
])

# Piano: 7th chords on 2 and 4, F#7 on 2, D7 on 4
piano_notes.extend([
    # F#7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),   # F#
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),   # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),   # D
    # D7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),    # F#
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),    # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),    # C
])

# Drums for Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Add notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
