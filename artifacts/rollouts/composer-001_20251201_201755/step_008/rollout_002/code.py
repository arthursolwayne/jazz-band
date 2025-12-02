
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2) -> G2 (F3) -> A2 (G3) -> Bb2 (A3) -> C3 (Bb3) (walking line with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # Bb2
]

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0), # F4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=3.0), # A4
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=3.0), # C5
    pretty_midi.Note(velocity=70, pitch=78, start=1.5, end=3.0), # E5
]

# Sax: Motif starts here. F4 -> G4 -> Ab4 -> F4 (melodic idea)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # F4
]

# Drums for Bar 2
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: C3 (Bb3) -> D3 (C4) -> Eb3 (D4) -> F3 (Eb4)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75), # D3
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # Eb3
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),  # F3
])

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5), # D5
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=4.5), # F5
    pretty_midi.Note(velocity=70, pitch=75, start=3.0, end=4.5), # Ab5
])

# Sax: Motif repeats but with a slight twist (F4 -> G4 -> Ab4 -> Bb4)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.125), # Ab4
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # Bb4
])

# Drums for Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F3 (Eb4) -> G3 (F4) -> A3 (G4) -> Bb3 (A4) -> C4 (Bb4)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # F3
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # G3
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625), # A3
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),  # Bb3
])

# Piano: F7 (F, A, C, E) - resolving back to F
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # F4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0), # A4
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=6.0), # C5
    pretty_midi.Note(velocity=70, pitch=78, start=4.5, end=6.0), # E5
])

# Sax: Complete the motif, return to F4
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # G4
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.625), # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # F4
])

# Drums for Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
])

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
