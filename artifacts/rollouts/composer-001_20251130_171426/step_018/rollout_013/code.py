
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

# Bar 1: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif (F, G#, B, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # G#
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # G#
]
sax.notes.extend(sax_notes)

# Bass line: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.25),  # G#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=2.5, end=2.75),  # A#
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (F7 and B7)
# Bar 2: F7 on beat 2 (1.75 - 2.0)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0),  # C
]
# Bar 2: B7 on beat 4 (2.75 - 3.0)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=95, pitch=74, start=2.75, end=3.0),  # D#
    pretty_midi.Note(velocity=95, pitch=76, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=95, pitch=78, start=2.75, end=3.0),  # G
])
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif (F, G#, B, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # G#
]
sax.notes.extend(sax_notes)

# Bass line: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.5),  # C#
    pretty_midi.Note(velocity=90, pitch=56, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=90, pitch=61, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (F7 and B7)
# Bar 3: F7 on beat 2 (3.25 - 3.5)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5),  # C
]
# Bar 3: B7 on beat 4 (4.25 - 4.5)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=95, pitch=74, start=4.25, end=4.5),  # D#
    pretty_midi.Note(velocity=95, pitch=76, start=4.25, end=4.5),  # F#
    pretty_midi.Note(velocity=95, pitch=78, start=4.25, end=4.5),  # G
])
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif (F, G#, B, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),   # G#
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),   # B
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # G#
]
sax.notes.extend(sax_notes)

# Bass line: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.5),  # C#
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (F7 and B7)
# Bar 4: F7 on beat 2 (4.75 - 5.0)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0),  # C
]
# Bar 4: B7 on beat 4 (5.75 - 6.0)
piano_notes.extend([
    pretty_midi.Note(velocity=95, pitch=71, start=5.75, end=6.0),  # B
    pretty_midi.Note(velocity=95, pitch=74, start=5.75, end=6.0),  # D#
    pretty_midi.Note(velocity=95, pitch=76, start=5.75, end=6.0),  # F#
    pretty_midi.Note(velocity=95, pitch=78, start=5.75, end=6.0),  # G
])
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3: 3.0 - 4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
