
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # F2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # E5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in F, one short phrase, singable
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # C5
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # G2 (third)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # G2 (third)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # A5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # C6
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # C5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Full bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # D3 (seventh)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # F2 (root)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Fmaj7 (resolution)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # E5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # C5
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # C5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Full bar
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
