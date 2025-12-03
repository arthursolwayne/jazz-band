
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
piano_notes = [
    # Dm7 (D-F-A-C) - open voicing
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # C5
    # Bb7 (Bb-D-F-A) - open voicing
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # F5
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # A5
    # Gm7 (G-Bb-D-F) - open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G5
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # F5
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Dm melodic motif: D - F - Bb - D
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),   # F4
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),   # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D4
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Continue the rhythm and motif
# Drums (Bar 2-4)
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
    drums.notes.extend([n.copy() for n in drum_notes])

# Bass (Bar 2-4)
for i in range(2):
    for note in bass_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
    bass.notes.extend([n.copy() for n in bass_notes])

# Piano (Bar 2-4)
for i in range(2):
    for note in piano_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
    piano.notes.extend([n.copy() for n in piano_notes])

# Sax (Bar 2-4)
for i in range(2):
    for note in sax_notes:
        note.start += 1.5 * (i + 1)
        note.end += 1.5 * (i + 1)
    sax.notes.extend([n.copy() for n in sax_notes])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
