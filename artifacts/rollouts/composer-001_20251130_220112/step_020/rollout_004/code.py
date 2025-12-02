
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full band (1.5 - 3.0s)
# Bassline: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=2.25),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody - short motif, starts on D, ends on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full band (3.0 - 4.5s)
# Bassline: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.75),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Melody - continuation, ends on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full band (4.5 - 6.0s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bassline: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=5.25),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody - continuation, ends on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
