
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time settings (in seconds)
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))
# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))
# Hi-hats on every eighth note
for i in range(0, 6):
    start = i * BEAT_DURATION
    end = start + BEAT_DURATION
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 2-4: Full band (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (1.5, 64),     # F
    (1.875, 65),   # F#
    (2.25, 64),    # F
    (2.625, 62),   # D (chromatic approach)
    (3.0, 65),     # F#
    (3.375, 67),   # A
    (3.75, 65),    # F#
    (4.125, 64),   # F
    (4.5, 63),     # E (chromatic approach)
    (4.875, 65),   # F#
    (5.25, 67),    # A
    (5.625, 69),   # B (chromatic approach)
    (6.0, 67)      # A
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + BEAT_DURATION))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64, 80),     # F7 (F, A, C, E♭)
    (1.875, 64, 80),   # F7
    (2.25, 64, 80),    # F7
    (2.625, 64, 80),   # F7
    (3.0, 67, 80),     # A7 (A, C#, E, G)
    (3.375, 67, 80),   # A7
    (3.75, 67, 80),    # A7
    (4.125, 67, 80),   # A7
    (4.5, 69, 80),     # B7 (B, D#, F#, A)
    (4.875, 69, 80),   # B7
    (5.25, 69, 80),    # B7
    (5.625, 69, 80),   # B7
    (6.0, 64, 80)      # F7
]

for start, pitch, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + BEAT_DURATION))

# Sax (Dante): One short, singing motif — a question, a memory
# Start with a motif beginning on bar 2, leave it hanging, return to finish it
# F (64), B♭ (62), E (60), F (64)
sax_notes = [
    (2.25, 64, 100),   # F
    (2.625, 62, 100),  # B♭
    (3.0, 60, 100),    # E
    (3.375, 64, 100),  # F (hang on)
    (3.75, 62, 100),   # B♭ (return)
    (4.125, 60, 100),  # E
    (4.5, 64, 100)     # F
]

for start, pitch, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + BEAT_DURATION))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
