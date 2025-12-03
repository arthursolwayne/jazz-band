
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
    # Hihat on every eighth
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
# Bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # A#2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # C5
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # F5
    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (D4, F4, G4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    # Bar 3: Leave it hanging (no notes)
    # Bar 4: Come back and finish it (D4, F4, G4)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: same pattern as bar 1
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Add drum notes for bar 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
