
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.25),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.5),  # C2
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),  # Ab2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # Ab4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - Start with F (65), Ab (60), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # Ab4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.0),  # C2
    pretty_midi.Note(velocity=90, pitch=53, start=4.0, end=4.25),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.25, end=4.5),  # Ab2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar
# Bar 3: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),   # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.25),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.5),  # C2
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.75),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=5.75, end=6.0),  # Ab2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chords each bar
# Bar 4: C7 (C, E, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: End with a clean G (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
