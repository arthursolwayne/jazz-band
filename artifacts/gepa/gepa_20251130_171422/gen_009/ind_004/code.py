
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Bb, D, F#, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),
]

# Bass: Walking line in D (D, C#, B, A, G, F#, E, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=58, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=56, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
]

# Piano: 7th chords on 2 and 4 (G7, C7)
piano_notes = [
    # G7 on beat 2 (1.875 - 2.125)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.125),
    # C7 on beat 4 (2.625 - 2.875)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875),
]

# Drums in Bar 2
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but lower by a whole step (Bb, D, F#, Bb)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),
])

# Bass: Walking line in D (D, C#, B, A, G, F#, E, D)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
])

# Piano: 7th chords on 2 and 4 (G7, C7)
piano_notes.extend([
    # G7 on beat 2 (3.375 - 3.625)
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.625),
    # C7 on beat 4 (4.125 - 4.375)
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.375),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.375),
])

# Drums in Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a trill or glissando on Bb
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
])

# Bass: Walking line in D (D, C#, B, A, G, F#, E, D)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=58, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=56, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=62, start=6.25, end=6.5),
])

# Piano: 7th chords on 2 and 4 (G7, C7)
piano_notes.extend([
    # G7 on beat 2 (4.875 - 5.125)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.125),
    # C7 on beat 4 (5.625 - 5.875)
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.875),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.875),
])

# Drums in Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

# Add notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
