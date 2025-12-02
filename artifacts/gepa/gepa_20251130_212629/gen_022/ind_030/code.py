
import pretty_midi

# Create MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Alto Saxophone
bass = pretty_midi.Instrument(program=33)      # Electric Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum pitches
KICK = 36
SNARE = 38
HIHAT = 42

# --- Bar 1: Drums only (0.0 - 1.5s) ---
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=KICK, start=1.125, end=1.5),

    pretty_midi.Note(velocity=110, pitch=SNARE, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=SNARE, start=1.875, end=2.0),

    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.3125, end=1.5),

    # Syncopated hihat
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=0.875, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=HIHAT, start=1.6875, end=1.75)
]

for note in drum_notes:
    drums.notes.append(note)

# --- Bar 2: Full quartet (1.5 - 3.0s) ---
## Saxophone (Dm7 motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # G
]

## Bass (walking line)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=3.0),  # F
]

## Piano: Dm7 chord (D, F, Ab, C)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5)   # C
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# --- Bar 3: Sax and bass continue, piano comps (3.0 - 4.5s) ---
## Saxophone continues motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # Eb
]

## Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),  # G
]

## Piano: Comping Dm7 with rhythm
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.25),  # C

    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# --- Bar 4: Build-up and resolution (4.5 - 6.0s) ---
## Saxophone: Resolves on D (key note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # G
]

## Bass: Resolves with a D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),  # G
]

## Piano: Resolves on Dm7
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.75),  # C

    pretty_midi.Note(velocity=85, pitch=62, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=85, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=5.5, end=5.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=5.5, end=5.75)   # C
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Add all instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_jazz_piece.mid")
