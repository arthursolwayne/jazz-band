
import pretty_midi

# Create a MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note values (pitch numbers)
# Dm7 = D (62), F (64), A (69), C (60)
# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray (drums) - 0.0 to 1.5 seconds
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3

    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 4

    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),

    # Syncopated hihat for tension
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.75)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 to 3.0 seconds)
# Saxophone: Melodic motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Dm7 - C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Dm7 - D
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Dm7 - C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Dm7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Dm7 - C
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # Dm7 - D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=58, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 comping on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.75),  # C

    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_jazz_piece.mid")
