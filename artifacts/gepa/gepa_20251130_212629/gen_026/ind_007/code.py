
import pretty_midi
import numpy as np

# Initialize the MIDI file and set tempo
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

# Add instruments to the MIDI file
midi.instruments = [sax, bass, piano, drums]

# Define basic parameters
bpm = 160
bar_length = 1.5  # seconds per bar at 160 BPM
beat_length = 0.375  # seconds per beat
time = 0.0

# --- BAR 1: Little Ray (Drums) — Tension and anticipation (0.0 - 1.5s) ---

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=bar_length * 0.5, end=bar_length * 0.5 + 0.05))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar_length * 0.25, end=bar_length * 0.25 + 0.05))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar_length * 0.75, end=bar_length * 0.75 + 0.05))

# Hi-hat on every eighth
for i in range(8):
    start = i * (beat_length / 2)
    if i % 2 == 0:
        velocity = 100
    else:
        velocity = 85
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=42, start=start, end=start + 0.02))

time = bar_length

# --- BAR 2-4: Full Quartet (1.5 - 6.0s) ---

# --- Drums ---
# Repeat the same pattern
for i in range(3):  # 3 bars
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=np.random.randint(75, 90), pitch=36, start=time, end=time + 0.05))
    drums.notes.append(pretty_midi.Note(velocity=np.random.randint(75, 90), pitch=36, start=time + beat_length * 0.5, end=time + beat_length * 0.5 + 0.05))

    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=np.random.randint(85, 100), pitch=38, start=time + beat_length * 0.25, end=time + beat_length * 0.25 + 0.05))
    drums.notes.append(pretty_midi.Note(velocity=np.random.randint(85, 100), pitch=38, start=time + beat_length * 0.75, end=time + beat_length * 0.75 + 0.05))

    # Hi-hat on every eighth
    for j in range(8):
        start = j * (beat_length / 2)
        if j % 2 == 0:
            velocity = np.random.randint(90, 100)
        else:
            velocity = np.random.randint(80, 95)
        drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=42, start=time + start, end=time + start + 0.02))

    time += bar_length

# --- Bass: Walking line, chromatic approach --- (Marcus)
# Dm7 -> G7 -> Cm7 -> F7
# 12 bars but we're only doing 3 (bars 2-4)
bass_notes = [
    # Bar 2
    (1.5, 62, 0.25),     # D
    (1.75, 61, 0.25),    # C#
    (2.0, 64, 0.25),     # E
    (2.25, 62, 0.25),    # D
    (2.5, 65, 0.25),     # F
    (2.75, 64, 0.25),    # E
    (3.0, 62, 0.25),     # D
    (3.25, 60, 0.25),    # C

    # Bar 3
    (3.5, 60, 0.25),     # C
    (3.75, 62, 0.25),    # D
    (4.0, 64, 0.25),     # E
    (4.25, 69, 0.25),    # G
    (4.5, 67, 0.25),     # F#
    (4.75, 69, 0.25),    # G
    (5.0, 67, 0.25),     # F#
    (5.25, 65, 0.25),    # E

    # Bar 4
    (5.5, 65, 0.25),     # E
    (5.75, 62, 0.25),    # D
    (6.0, 60, 0.25),     # C
    (6.25, 58, 0.25),    # B
    (6.5, 60, 0.25),     # C
    (6.75, 62, 0.25),    # D
    (7.0, 64, 0.25),     # E
    (7.25, 67, 0.25),    # F#
]
for start, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + duration))

# --- Piano: Diane — 7th chords, comp on 2 and 4 (Bars 2-4) ---

# Bar 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=75, pitch=64, start=1.5, end=1.75))  # F

# Bar 3: G7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=3.5, end=3.75))  # B
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=75, pitch=64, start=3.5, end=3.75))  # F

# Bar 4: Cm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=5.5, end=5.75))  # E
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75))  # G
piano.notes.append(pretty_midi.Note(velocity=75, pitch=60, start=5.5, end=5.75))  # C

# --- Sax: Dante — Melody (bars 2-4) ---

# Motif: D - Bb - E - D (with dynamics and rests)
# Bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25))   # E
sax.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75))  # D

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25))  # E
sax.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75))   # G
sax.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=4.0, end=4.25))   # D
sax.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5))   # G

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5))  # G
sax.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0))   # E
sax.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=6.0, end=6.25))   # D

# Save the MIDI
midi.write("dante_intro.mid")

print("MIDI file generated: dante_intro.mid")
print("This intro is set to make Wayne Shorter lean forward.")
print("It’s tense, emotional, and full of promise.")
print("A doorway — and a question.")
