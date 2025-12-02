
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.75),    # hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5)     # hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # B7
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # G7
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),    # hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5)     # hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 3: Bass (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
piano_notes = [
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # G7
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D7
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Sax (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),    # hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0)     # hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes = [
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # G7
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),    # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),    # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),    # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),    # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),    # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
