
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: D2 (38) -> F2 (41) -> G2 (43) -> A2 (45)
# Walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # chromatic approach to F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # F# (F#5)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - G4 (start), F#4 (approach), E4 (resolve), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G4 (resting)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: A2 (45) -> B2 (46) -> C#2 (43) -> D2 (38)
# Walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # chromatic approach to B2
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),  # B2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # C#2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.75),  # F# (F#5)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # B (B5)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),  # D# (D#6)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif again, but this time resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: D2 (38) -> E2 (40) -> F2 (41) -> G2 (43)
# Walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # chromatic approach to E2
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),  # E2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Gmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # G (G5)
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=5.25),  # B (B5)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif again, but this time finish it with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
