
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
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line with chromatic approaches
# Diane on piano: 7th chords, comp on 2 and 4
# Dante on sax: motif starts here
# Little Ray: same pattern as before

# Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Diane
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625), # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # G
]
piano.notes.extend(piano_notes)

# Dante on sax: motif starts on bar 2, 1st beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dm
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Drums in bar 2
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick, snare, hihat])

# Bar 3 (3.0 - 4.5s)
# Marcus: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Diane: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # G
]
piano.notes.extend(piano_notes)

# Dante: motif continues
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Dm
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick, snare, hihat])

# Bar 4 (4.5 - 6.0s)
# Marcus: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),   # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # G
]
piano.notes.extend(piano_notes)

# Dante: motif ends on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Dm
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick, snare, hihat])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
