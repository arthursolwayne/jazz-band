
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2, G2, A2, C3) with chromatic approaches
# Bar 2: F2 -> F#2 -> G2 -> G2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # F#2
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0), # F (C4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0), # A (E4)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0), # C (G4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0), # E (A4)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75), # A (E4)
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # C (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # A (E4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # A (E4)
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # C (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # A (E4)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (G2, A2, Bb2, C3) with chromatic approaches
# Bar 3: G2 -> G#2 -> A2 -> A2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # G#2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5), # A2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5), # Bb (D4)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5), # D (F4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5), # F (A4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # Ab (Bb4)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # A (E4)
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),   # C (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),   # A (E4)
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),   # G (D4)
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),   # A (E4)
    pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5),   # G (D4)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (A2, Bb2, B2, C3) with chromatic approaches
# Bar 4: A2 -> A#2 -> B2 -> B2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875), # A2
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # A#2
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625), # B2
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0), # B2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0), # C (A4)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0), # E (C5)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # G (E5)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # B (G5)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Resolve the motif, leave a lingering note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # A (E4)
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),   # C (G4)
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),   # A (E4)
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),   # G (D4)
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),   # A (E4)
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),   # A (E4)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999), # Kick on 3

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
