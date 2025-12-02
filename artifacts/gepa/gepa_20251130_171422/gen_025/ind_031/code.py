
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
instrument = pretty_midi.Instrument(program=64)  # Tenor Saxophone
pm.instruments.append(instrument)

# Define note durations and velocities
BAR_LENGTH = 6.0  # 6 seconds for 4 bars
BEAT_LENGTH = BAR_LENGTH / 4  # 1.5 seconds per beat
NOTE_DURATION = BEAT_LENGTH / 4  # 0.375 seconds per 8th note
VEL_RANGE = (40, 100)  # Dynamic range for melody

# Generate Fm7 chord (F, Ab, C, Eb)
Fm7_notes = [76, 79, 84, 87]  # MIDI pitches for Fm7

# Define the melody for the sax as a motif
# Bar 1: Drums only — create tension with space
# Bar 2-4: Sax melody, with a motif that lingers
melody = [
    (76, 0.375, 75),  # F, 8th note, soft
    (79, 0.375, 90),  # Ab, 8th note, louder
    (84, 0.375, 95),  # C, 8th note, intense
    (77, 0.375, 85),  # Gb (half-step below F), 8th note, unresolved
    (80, 0.375, 92),  # Bb (chromatic), 8th note
    (76, 0.375, 75),  # F, 8th note, back to start
    (79, 0.375, 90),  # Ab, 8th note
    (84, 0.375, 100), # C, 8th note, resolves slightly
]

# Assign each note in melody to the sax instrument
for note, duration, velocity in melody:
    note_obj = pretty_midi.Note(
        velocity=velocity,
        pitch=note,
        start=0,
        end=duration
    )
    instrument.notes.append(note_obj)

# Add a simple walking bass line (Marcus)
bass_instrument = pretty_midi.Instrument(program=33)  # Double Bass
pm.instruments.append(bass_instrument)

bass_line = [
    (70, 0.375),  # E (Fm7 root 3rd)
    (69, 0.375),  # D (chromatic)
    (70, 0.375),  # E
    (72, 0.375),  # F (chromatic up)
    (71, 0.375),  # E
    (70, 0.375),  # D
    (69, 0.375),  # C (chromatic down)
    (70, 0.375),  # D
]

for note, duration in bass_line:
    note_obj = pretty_midi.Note(
        velocity=60,
        pitch=note,
        start=0,
        end=duration
    )
    bass_instrument.notes.append(note_obj)

# Add piano comping (Diane)
piano_instrument = pretty_midi.Instrument(program=0)  # Acoustic Piano
pm.instruments.append(piano_instrument)

# Fm7, comp on 2 and 4
comping = [
    (76, 0.0), (79, 0.0), (84, 0.0), (87, 0.0),  # Fm7
    (76, 0.5), (79, 0.5), (84, 0.5), (87, 0.5),  # Fm7 on beat 2
    (76, 0.0), (79, 0.0), (84, 0.0), (87, 0.0),  # Fm7
    (76, 0.5), (79, 0.5), (84, 0.5), (87, 0.5),  # Fm7 on beat 4
]

# Simulate the piano comping with rhythmic space
for i, (pitch, start) in enumerate(comping):
    duration = 0.375
    if i % 2 == 0:
        start = i * 0.375
        note_obj = pretty_midi.Note(
            velocity=65,
            pitch=pitch,
            start=start,
            end=start + duration
        )
        piano_instrument.notes.append(note_obj)

# Add drums (Little Ray)
drums_instrument = pretty_midi.Instrument(program=112)  # Drums
pm.instruments.append(drums_instrument)

# Kick on 1 and 3
kick_notes = [
    (36, 0.0), (36, 1.5), (36, 3.0), (36, 4.5)
]
for pitch, start in kick_notes:
    note_obj = pretty_midi.Note(
        velocity=100,
        pitch=pitch,
        start=start,
        end=start + 0.375
    )
    drums_instrument.notes.append(note_obj)

# Snare on 2 and 4
snare_notes = [
    (38, 0.75), (38, 2.25), (38, 3.75), (38, 5.25)
]
for pitch, start in snare_notes:
    note_obj = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=start,
        end=start + 0.25
    )
    drums_instrument.notes.append(note_obj)

# Hi-hat on every 8th
hihat_notes = [
    (42, 0.0), (42, 0.375), (42, 0.75), (42, 1.125),
    (42, 1.5), (42, 1.875), (42, 2.25), (42, 2.625),
    (42, 3.0), (42, 3.375), (42, 3.75), (42, 4.125),
    (42, 4.5), (42, 4.875), (42, 5.25), (42, 5.625)
]

for pitch, start in hihat_notes:
    note_obj = pretty_midi.Note(
        velocity=80,
        pitch=pitch,
        start=start,
        end=start + 0.125
    )
    drums_instrument.notes.append(note_obj)

# Write the MIDI file
pm.write("jazz_intro_4bars_Fm.mid")
