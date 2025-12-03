
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

# Bass line (F2, Bb2, B2, C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # B2
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano chords (F7, Bb7, Bm7, C7)
# Bar 2: F7 (F, A, C, E) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (E4)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # Bb (F4)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # C (A4)
]
# Bar 3: Bb7 (Bb, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5),  # Bb (E4)
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=4.5),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5),  # A (G4)
])
# Bar 4: Bm7 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # D (A4)
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=6.0),  # F# (C5)
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # A (C5)
])
piano.notes.extend(piano_notes)

# Sax melody (start at 1.5s)
# Motif: F (G4) - Bb (A4) - B (B4) - F (G4) 
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),   # F (G4)
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.25),  # Bb (A4)
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.625),  # B (B4)
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # F (G4)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (1.5 - 3.0s)
# Same pattern as Bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend(drum_notes)

# Bar 4: Drums (3.0 - 4.5s)
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend(drum_notes)

# Bar 5: Drums (4.5 - 6.0s)
for note in drum_notes:
    note.start += 4.5
    note.end += 4.5
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
