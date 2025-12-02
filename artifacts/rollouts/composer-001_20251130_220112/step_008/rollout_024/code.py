
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
]
sax.notes.extend(sax_notes)

# Bass line (F, G, E, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=80, pitch=44, start=2.0625, end=2.25), # D
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0),  # D
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=2.75),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5625, end=3.75), # G
]
sax.notes.extend(sax_notes)

# Bass walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=3.1875, end=3.375), # E
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.5625, end=3.75), # G
]
bass.notes.extend(bass_notes)

# Piano comping
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.5),  # D
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Drums for bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # G
]
sax.notes.extend(sax_notes)

# Bass walking line (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=80, pitch=49, start=5.0625, end=5.25), # A
]
bass.notes.extend(bass_notes)

# Piano comping
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.0),  # D
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
