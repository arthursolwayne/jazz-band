
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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
# Sax melody: C - E - G - Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),
]
sax.notes.extend(sax_notes)

# Bass line: walking line in C, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75),
    # Bar 2, beat 4: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motifs: repeat and vary
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),
]
sax.notes.extend(sax_notes)

# Bass line: chromatic again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.125),  # D#
    pretty_midi.Note(velocity=80, pitch=55, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5),  # G
]
bass.notes.extend(bass_notes)

# Piano chords: comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.25),
    # Bar 3, beat 4: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),
]
sax.notes.extend(sax_notes)

# Bass line: chromatic again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=80, pitch=61, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0),  # A#
]
bass.notes.extend(bass_notes)

# Piano chords: comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.75),
    # Bar 4, beat 4: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),
]
piano.notes.extend(piano_notes)

# Add drum fill for Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.625, end=4.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=5.0),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0),  # Kick
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
