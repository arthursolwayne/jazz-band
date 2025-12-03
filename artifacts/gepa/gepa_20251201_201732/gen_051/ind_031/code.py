
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (F root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2 (F5)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # E2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=3.0),  # A (E4)
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=3.0),  # C (G4)
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=3.0),  # E (B4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (F, Bb, E, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),   # Bb (E4)
    pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.25),   # E (G4)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.5),   # D (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass: walking line (Bb2, A2, G2, F2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Bb2 (F root)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # G2 (F5)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # F2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # Bb (D4)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # D (F4)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # F (E4)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # Ab (G4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (Bb, F, D, C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Bb (D4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),   # F (E4)
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75),   # D (F4)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),   # C (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass: walking line (E2, D2, C2, Bb2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # E2 (F root)
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # D2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),  # C2 (F5)
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Bb2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),  # A (E4)
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=6.0),  # C (G4)
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=6.0),  # E (B4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (F, Bb, E, D) - return to the beginning
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),   # Bb (E4)
    pretty_midi.Note(velocity=100, pitch=78, start=5.0, end=5.25),   # E (G4)
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.5),   # D (F4)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
