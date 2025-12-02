
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, tension through space and texture

# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125))

# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5))

# Hihat on every eighth (beat 0, 0.375, 0.75, 1.125), with subtle dynamics
drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif - D minor, concise, emotional
# D - F - G - Bb - Bb - G - F - D
# Start at 1.5s, finish at 3.5s

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),   # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),   # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)    # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking, chromatic, melodic
# D - Eb - E - F - F - G - G - Ab
# Start at 1.5s, finish at 3.5s

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),   # Eb4
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),   # E4
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),   # F4
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),   # F4
    pretty_midi.Note(velocity=80, pitch=66, start=2.75, end=3.0),   # G4
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),   # G4
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5)    # Ab4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - comping on 2 and 4, 7th chords
# D7 (D, F#, A, C) on beat 2 (1.75s)
# G7 (G, B, D, F) on beat 4 (3.25s)

piano_notes = [
    # D7 on beat 2 (1.75s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),   # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=75, pitch=60, start=1.75, end=2.0),   # C4
    # G7 on beat 4 (3.25s)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),   # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),   # B4
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5),   # D5
    pretty_midi.Note(velocity=75, pitch=65, start=3.25, end=3.5)    # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Drums continue in bars 2-4 (1.5 - 6.0s)
# Same pattern: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Repeat for bars 2-4 (1.5 - 3.0, 3.0 - 4.5, 4.5 - 6.0)

# Bar 2 (1.5 - 3.0)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0))

# Bar 3 (3.0 - 4.5)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5))

# Bar 4 (4.5 - 6.0)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to disk
midi.write("dante_intro.mid")
