
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Full quartet starts
# Bass: walking line, D2 (38) to G2 (43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),     # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),    # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),    # G2
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),     # A#2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s): G7 (G-B-D-F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),  # F#5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s): Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, haunting, incomplete
# Start with the motif on bar 2, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D#4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start = 1.5 + i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start = 3.0 + i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start = 4.5 + i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
