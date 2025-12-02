
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D (D4), F# (F#4), A (A4), B (B4) - motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.5),  # G3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # D5
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.25),  # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # Ab3
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # A3
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),  # C4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Return to motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=5.0),  # Db4
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # F4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
