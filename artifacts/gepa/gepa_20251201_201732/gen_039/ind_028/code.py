
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    # D2 (38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # C#2 (37) chromatic approach
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25),
    # G2 (43) fifth
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # F#2 (42) chromatic approach
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # C#5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif starts, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # B4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (38) walking line
bass_notes = [
    # D2 (38)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    # C#2 (37)
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.75),
    # G2 (43)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),
    # F#2 (42)
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # C#5
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (38) walking line
bass_notes = [
    # D2 (38)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    # C#2 (37)
    pretty_midi.Note(velocity=90, pitch=37, start=4.875, end=5.25),
    # G2 (43)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    # F#2 (42)
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Gmaj7 (G B D F#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # C#5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # C#5
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
