
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
# Saxophone: Motif starting on D (D4), B (B4), F# (F#4), A (A4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
# D, C, B, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=59, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 on beat 2 (C#4, E4, G4, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # C#4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: Repeat motif, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
# D, C, B, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3: D7 on beat 2 (C#4, E4, G4, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),  # C#4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: Finish the motif with a resolution to G (G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # C#5
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # D5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
# D, C, B, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4: D7 on beat 2 (C#4, E4, G4, B4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),  # C#4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A4
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
