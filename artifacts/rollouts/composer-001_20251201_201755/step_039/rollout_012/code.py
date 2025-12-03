
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2-C3-G2-A2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=81, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=80, pitch=79, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=80, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 2: Fmaj7 (F-A-C-E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # E
    # Bar 3: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=88, start=3.0, end=4.5),  # A
    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif (F - Bb - G - Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=79, start=2.625, end=3.0),   # Bb
    # Repeat motif with slight variation
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=79, start=4.125, end=4.5),   # Bb
    # Final variation to resolve
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=79, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=82, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=79, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: Same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Same pattern as bar 1
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
