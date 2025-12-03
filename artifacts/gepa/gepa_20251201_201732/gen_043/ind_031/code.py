
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
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s)
# Sax melody: start with a short motif, leave it hanging

# F7 chord (F A C E) -> F7sus4 (F Bb C E) -> Gm7 (G Bb D F)
# Diane plays open voicings: F7sus4 (F, Bb, C, E) on beat 2

# Bass line: F -> Bb -> C -> D (walking line with chromatic approach)

# Sax: F (beat 1), Bb (beat 2), rest (beat 3), F (beat 4) — incomplete

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.875),  # F (beat 4)
]

piano_notes_bar2 = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # E
]

bass_notes_bar2 = [
    pretty_midi.Note(velocity=70, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=49, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=70, pitch=50, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=70, pitch=52, start=2.625, end=3.0),  # D
]

# Bar 3 (3.0 - 4.5s)
# Sax continues the motif, resolves on beat 2

# Diane plays Gm7 (G, Bb, D, F)

# Bass continues walking line: D -> F -> G -> A

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # Bb
])

piano_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
]

bass_notes_bar3 = [
    pretty_midi.Note(velocity=70, pitch=52, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=70, pitch=55, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=70, pitch=57, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=70, pitch=59, start=4.125, end=4.5),  # A
]

drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

# Bar 4 (4.5 - 6.0s)
# Sax resolves the motif

# Diane plays Am7 (A, C, E, G)

# Bass continues walking line: A -> Bb -> C -> D

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # A
])

piano_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # G
]

bass_notes_bar4 = [
    pretty_midi.Note(velocity=70, pitch=59, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=70, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=70, pitch=62, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=70, pitch=64, start=5.625, end=6.0),  # D
]

drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

# Add all drum notes for bar 3 and 4
drums.notes.extend(drum_notes_bar3)
drums.notes.extend(drum_notes_bar4)

# Add sax notes
sax.notes.extend(sax_notes)

# Add piano notes
piano.notes.extend(piano_notes_bar2)
piano.notes.extend(piano_notes_bar3)
piano.notes.extend(piano_notes_bar4)

# Add bass notes
bass.notes.extend(bass_notes_bar2)
bass.notes.extend(bass_notes_bar3)
bass.notes.extend(bass_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
