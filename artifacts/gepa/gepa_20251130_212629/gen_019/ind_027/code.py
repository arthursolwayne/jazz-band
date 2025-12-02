
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)          # Saxophone
bass = pretty_midi.Instrument(program=33)         # Electric Bass
piano = pretty_midi.Instrument(program=0)         # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: note numbers
# Kick = 36, Snare = 38, Hi-Hat = 42, Open Hi-Hat = 46, Ride = 56, etc.

# Bar 1: Drums (0.0 - 1.5s)
# Groove with kick on 1 & 3, snare on 2 & 4, hihat on every 8th
drum_notes = [
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-Hat (every 8th)
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
    # Syncopation
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.75)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Saxophone (1.5 - 3.0s)
# Melody: Dm7 - D, F, Ab, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),     # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),     # F
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.25),     # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),     # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),     # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),     # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2-4: Bass (Walking Line)
# Chromatic line in Dm7
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=61, start=1.5, end=1.75),   # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),   # G
    pretty_midi.Note(velocity=80, pitch=59, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 2-4: Piano (Comping - Fm7, Dm7)
# Chord tones on 2nd and 4th beats
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),    # D
    pretty_midi.Note(velocity=85, pitch=65, start=1.75, end=2.0),    # F
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),    # Ab
    pretty_midi.Note(velocity=85, pitch=64, start=1.75, end=2.0),    # C
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),    # D
    pretty_midi.Note(velocity=85, pitch=65, start=2.75, end=3.0),    # F
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),    # Ab
    pretty_midi.Note(velocity=85, pitch=64, start=2.75, end=3.0),    # C
]

for note in piano_notes:
    piano.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_jazz_quartet.mid")
