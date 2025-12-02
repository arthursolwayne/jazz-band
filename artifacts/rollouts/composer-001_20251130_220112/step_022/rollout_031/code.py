
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # F#
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),
    
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=3.0),
]

piano.notes.extend(piano_notes)

# Sax - short motif, start and finish with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # Eb
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),   # F#
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # Bb
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),
    
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.5),
]

piano.notes.extend(piano_notes)

# Sax - continuation of motif, finish with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # F#
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),
    
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=6.0),
]

piano.notes.extend(piano_notes)

# Sax - resolution, return to the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # Eb
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
