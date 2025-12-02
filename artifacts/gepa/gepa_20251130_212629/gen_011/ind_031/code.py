
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key to D minor (key number 1)
pm.key_signature_changes = [pretty_midi.KeySignature(1, 0.0)]

# Create instruments for each player
tenor_sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drums use same program

# Add instruments
tenor = pretty_midi.Instrument(program=tenor_sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program, is_drum=True)

pm.instruments = [tenor, bass, piano, drums]

# Define the tempo and time per bar (in seconds)
BPM = 160
beats_per_bar = 4
time_per_beat = 60.0 / BPM
time_per_bar = time_per_beat * beats_per_bar  # 1.5 seconds

# Bar 1: Little Ray (drums) sets up tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use MIDI note numbers for the drums

# MIDI note numbers for drums:
# Kick: 36
# Snare: 38
# Hihat closed: 42

# Bar 1: 4 beats, each beat has 2 eighth notes
for beat in range(4):
    time = beat * time_per_beat

    # Hihat on every eighth
    for eighth in range(2):
        note = pretty_midi.Note(
            velocity=80,
            pitch=42,
            start=time + eighth * time_per_beat / 2,
            end=time + eighth * time_per_beat / 2 + 0.05
        )
        drums.notes.append(note)

    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(
            velocity=100,
            pitch=36,
            start=time,
            end=time + 0.1
        )
        drums.notes.append(note)

    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(
            velocity=90,
            pitch=38,
            start=time,
            end=time + 0.1
        )
        drums.notes.append(note)

# Bar 2: Full band enters
# Tenor sax melody in Dm: starts with a simple motif

# Tenor sax part
# Dm scale: D Eb F G Ab Bb C
# We'll use a descending motif with space and tension
# D - Eb - F - rest (then repeat)
notes = [62, 63, 65, 0]  # D, Eb, F, rest
durations = [0.3, 0.3, 0.3, 0.3]

# Start time for the melody is bar 1.5 (the start of bar 2)
start_time = 1.5
for i, note in enumerate(notes):
    if note != 0:
        tenor_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=start_time + i * durations[i],
            end=start_time + i * durations[i] + durations[i]
        )
        tenor.notes.append(tenor_note)

# Bassline: Walking line in Dm, chromatic approaches
# Dm: D - Eb - F - G - Ab - Bb - C - D
# Walking bass line: D - Eb - F - G - Ab - Bb - C - D (with chromatic approaches)
bass_notes = [62, 63, 65, 67, 68, 70, 72, 62]
bass_durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

for i, note in enumerate(bass_notes):
    bass_note = pretty_midi.Note(
        velocity=75,
        pitch=note,
        start=start_time + i * 0.25,
        end=start_time + i * 0.25 + 0.25
    )
    bass.notes.append(bass_note)

# Piano (Diane) comping on 2 and 4 with 7th chords
# Dm7 = D, F, Ab, C
# We'll play it on beats 2 and 4 of bars 2 and 3
chord_notes = [62, 65, 68, 72]  # D, F, Ab, C
chord_duration = 0.25

# Bar 2 (beat 2)
piano_note = pretty_midi.Note(
    velocity=85,
    pitch=62,
    start=start_time + 0.5,
    end=start_time + 0.5 + chord_duration
)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(
    velocity=85,
    pitch=65,
    start=start_time + 0.5,
    end=start_time + 0.5 + chord_duration
)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(
    velocity=85,
    pitch=68,
    start=start_time + 0.5,
    end=start_time + 0.5 + chord_duration
)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(
    velocity=85,
    pitch=72,
    start=start_time + 0.5,
    end=start_time + 0.5 + chord_duration
)
piano.notes.append(piano_note)

# Bar 3 (beat 4)
piano_note = pretty_midi.Note(
    velocity=85,
    pitch=62,
    start=start_time + 1.5,
    end=start_time + 1.5 + chord_duration
)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(
    velocity=85,
    pitch=65,
    start=start_time + 1.5,
    end=start_time + 1.5 + chord_duration
)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(
    velocity=85,
    pitch=68,
    start=start_time + 1.5,
    end=start_time + 1.5 + chord_duration
)
piano.notes.append(piano_note)

piano_note = pretty_midi.Note(
    velocity=85,
    pitch=72,
    start=start_time + 1.5,
    end=start_time + 1.5 + chord_duration
)
piano.notes.append(piano_note)

# Write the MIDI file to disk
pm.write("dante_russo_intro.mid")

print("MIDI file written as 'dante_russo_intro.mid'")
