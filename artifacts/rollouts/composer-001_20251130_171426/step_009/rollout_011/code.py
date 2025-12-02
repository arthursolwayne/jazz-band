
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
# Sax motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # E3
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.25),  # C#3
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),  # C3
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),  # E3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # B4
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),  # D4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - repeat motif, but with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # C4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # E3
    pretty_midi.Note(velocity=80, pitch=44, start=3.5, end=3.75),  # C#3
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.0),  # C3
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5),  # E3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),  # B4
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # D4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # C4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0),  # E3
    pretty_midi.Note(velocity=80, pitch=44, start=5.0, end=5.25),  # C#3
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.5),  # C3
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),  # E3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),  # B4
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # G4
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # D4
]

for note in piano_notes:
    piano.notes.append(note)

# Drums in bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
