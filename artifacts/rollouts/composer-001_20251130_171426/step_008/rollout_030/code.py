
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Fm b9
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # Fm 9
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # Fm 11
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # Fm7 3
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25), # Fm7 7
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25), # Fm7 b9
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25), # Fm7 11
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),  # Fm7 3
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # Fm7 7
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # Fm7 b9
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # Fm7 11
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at 1.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # G (Fm7 9)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # Bb (Fm7 11)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # G (Fm7 9)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # Bb (Fm7 11)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # Fm 11
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # Fm 9
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125), # Fm b9
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # Fm root
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # Fm7 3
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # Fm7 7
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75), # Fm7 b9
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # Fm7 11
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # Fm7 3
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # Fm7 7
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # Fm7 b9
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # Fm7 11
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # G (Fm7 9)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # Bb (Fm7 11)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C (Fm7 13)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # G (Fm7 9)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # Fm b9
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # Fm 9
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),  # Fm 11
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25), # Fm7 3
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # Fm7 7
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25), # Fm7 b9
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25), # Fm7 11
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # Fm7 3
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # Fm7 7
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # Fm7 b9
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # Fm7 11
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # G (Fm7 9)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # Bb (Fm7 11)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # C (Fm7 13)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # D (Fm7 13)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
