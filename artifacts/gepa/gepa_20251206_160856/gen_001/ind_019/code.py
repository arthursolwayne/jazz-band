
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (38) - G2 (43), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),     # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),    # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),    # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),     # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Start the motif
# D4 - F#4 - Bb4 - D5 (short motif, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),   # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (43) - Bb2 (42) - D2 (38) - F#2 (41)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # F#2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F4 (resolve)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif
# G4 - Bb4 - D4 - G4 (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),   # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),   # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),   # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (38) - F#2 (41) - A2 (45) - C#3 (46) - D3 (47)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),   # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),   # F#2
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625),   # A2
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),    # C#3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # C4 (resolve)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Repeat motif, slightly varied
# D4 - F#4 - Bb4 - D5 (short motif, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25),   # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0),

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
