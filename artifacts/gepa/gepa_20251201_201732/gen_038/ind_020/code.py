
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Marcus: Walking bass line (F2, G2, Ab2, A2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=54, start=2.625, end=3.0),  # A2
]

# Diane: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # Ab4
]

# Dante: Melody (bar 2: F, Ab, Bb, C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # C4
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Marcus: Walking bass (Bb2, B2, C2, D2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=100, pitch=54, start=4.125, end=4.5),  # D2
]

# Diane: Gm7 (G, Bb, D, F) -> open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
]

# Dante: Melody (bar 3: D, Bb, C, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=61, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Marcus: Walking bass (Eb2, F2, G2, Ab2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # Ab2
]

# Diane: Cm7 (C, Eb, G, Bb) -> open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb4
]

# Dante: Melody (bar 4: F, Ab, Bb, C) - resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # C4
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
# midi.write disabled
