
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),      # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but it's the end of the bar)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#2 on 2 (chromatic approach to G2)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # E2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on last chord
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C4 (resolve on 4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing
# Start with D4, then E4, then D4 again (leaving it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E4 on 2
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D4 on 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D4 on 4 (hold)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2 on 1
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # Bb2 on 2 (chromatic approach to B2)
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # B2 on 3
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # E2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: F#7 (F# A# C# E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # A#4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # C#5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # E4 (resolve on 4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # E4 on 1
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F4 on 2
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G4 on 3
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4 on 4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # E2 on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # G2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2 on 3
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # E2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4 (resolve on 4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: End the motif on D4, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D4 on 2
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D4 on 3
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D4 on 4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),      # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4 (but it's the end of the piece)
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
