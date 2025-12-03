
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F7 chord: F, A, C, E (MIDI 53, 58, 60, 64)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F root
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=1.875),  # A fifth
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C third
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # E seventh
    # Chromatic approach to G (MIDI 55)
    pretty_midi.Note(velocity=60, pitch=54, start=1.875, end=2.0),
    # G root
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.375),
    # Chromatic approach to A (MIDI 58)
    pretty_midi.Note(velocity=60, pitch=57, start=2.375, end=2.625),
    # A root
    pretty_midi.Note(velocity=80, pitch=58, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # F7 (MIDI 53, 58, 60, 64)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    # G7 (MIDI 55, 60, 62, 67)
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # A7 (MIDI 58, 63, 65, 70)
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    # F7 again (resolve)
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (MIDI 53), Bb (MIDI 58), D (MIDI 62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=2.875, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Repeat the quartet pattern
# Drums
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Bass
for note in bass_notes:
    note.start += 3.0
    note.end += 3.0
bass.notes.extend([note.copy() for note in bass_notes])

# Piano
for note in piano_notes:
    note.start += 3.0
    note.end += 3.0
piano.notes.extend([note.copy() for note in piano_notes])

# Sax: Repeat the motif
for note in sax_notes:
    note.start += 3.0
    note.end += 3.0
sax.notes.extend([note.copy() for note in sax_notes])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
