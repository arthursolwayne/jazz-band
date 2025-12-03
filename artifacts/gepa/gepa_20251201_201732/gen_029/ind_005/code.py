
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif starts here, short and haunting
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # C (fifth)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # A5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif variation, tension and release
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # C (fifth)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # F5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif resolution, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
