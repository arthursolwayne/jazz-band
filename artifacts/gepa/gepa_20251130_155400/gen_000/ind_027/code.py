
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
    # Bar 1: 0.0 - 1.5s
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif starting on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # D
]

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F7 (F, A, C, D)
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # F7 again
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif on beat 1
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
])

# Bass: Walking line in Dm
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # D
])

# Piano: Comp on 2 and 4 with 7th chords
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),   # F7 again
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif on beat 1
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
])

# Bass: Walking line in Dm
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # D
])

# Piano: Comp on 2 and 4 with 7th chords
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # F7 again
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),
])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    # Bar 2: 1.5 - 3.0s
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4

    # Bar 3: 3.0 - 4.5s
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4

    # Bar 4: 4.5 - 6.0s
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
])

# Add notes to instruments
drums.notes.extend(drum_notes)
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
