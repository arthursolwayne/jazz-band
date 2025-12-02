
import pretty_midi
import numpy as np

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes = [time_signature]

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Set the key to D (scale degrees: D, E, F#, G, A, B, C#)
# Root: D (62), F#: 67, A: 69, B: 71

# Time per bar: 1.5 seconds (160 BPM, 4/4)
bar_duration = 1.5
beat_duration = 0.375  # 1/4 note

# ----------------------
# DRUMS: Bars 1-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Only hihat
# Bar 2: Kick on 1, snare on 2, hihat on eighths
# Bar 3: Kick on 1, snare on 2, hihat on eighths
# Bar 4: Kick on 1, snare on 2, hihat on eighths

# Hit on every eighth note (8 hits per bar)
for bar in range(4):
    for i in range(8):
        time = bar * bar_duration + i * beat_duration / 2
        note = pretty_midi.Note(
            velocity=80,
            pitch=42,  # hihat
            start=time,
            end=time + 0.05
        )
        drums.notes.append(note)

# Kick on 1 and 3 of bars 2-4
for bar in range(2, 4):
    time = bar * bar_duration
    note = pretty_midi.Note(
        velocity=100,
        pitch=36,  # kick
        start=time,
        end=time + 0.05
    )
    drums.notes.append(note)

    time = bar * bar_duration + 2 * beat_duration
    note = pretty_midi.Note(
        velocity=100,
        pitch=36,  # kick
        start=time,
        end=time + 0.05
    )
    drums.notes.append(note)

# Snare on 2 and 4 of bars 2-4
for bar in range(2, 4):
    time = bar * bar_duration + beat_duration
    note = pretty_midi.Note(
        velocity=100,
        pitch=38,  # snare
        start=time,
        end=time + 0.05
    )
    drums.notes.append(note)

    time = bar * bar_duration + 4 * beat_duration
    note = pretty_midi.Note(
        velocity=100,
        pitch=38,  # snare
        start=time,
        end=time + 0.05
    )
    drums.notes.append(note)

# ----------------------
# BASS: Walking line, roots and fifths with chromatic approaches
# Key: D (62)
# Bar 1: A (69) -> B (71) chromatic approach
# Bar 2: D (62) -> F# (67)
# Bar 3: G (67) -> A (69)
# Bar 4: B (71) -> C# (73)

bass_notes = [
    # Bar 1 (0-1.5s)
    (69, 0.0, 0.375),  # A (69)
    (71, 0.375, 0.75),  # B (71)
    (70, 0.75, 1.125),  # Bb (70) chromatic
    (69, 1.125, 1.5),  # A (69)
    
    # Bar 2 (1.5-3.0s)
    (62, 1.5, 1.875),  # D (62)
    (67, 1.875, 2.25),  # F# (67)
    (65, 2.25, 2.625),  # F (65) chromatic
    (62, 2.625, 3.0),  # D (62)
    
    # Bar 3 (3.0-4.5s)
    (67, 3.0, 3.375),  # G (67)
    (69, 3.375, 3.75),  # A (69)
    (70, 3.75, 4.125),  # Bb (70)
    (69, 4.125, 4.5),  # A (69)
    
    # Bar 4 (4.5-6.0s)
    (71, 4.5, 4.875),  # B (71)
    (73, 4.875, 5.25),  # C# (73)
    (72, 5.25, 5.625),  # C (72)
    (71, 5.625, 6.0),  # B (71)
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(
        velocity=100,
        pitch=pitch,
        start=start,
        end=end
    )
    bass.notes.append(note)

# ----------------------
# PIANO: Open voicings, resolve on the last beat of each bar
# Bar 1: Dmaj7 (D, F#, A, C#)
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: D7 (D, F#, A, C)
# Bar 4: Dmaj7 (D, F#, A, C#)

# Bar 1: Dmaj7
for pitch in [62, 67, 69, 73]:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=0,
        end=1.5
    )
    piano.notes.append(note)

# Bar 2: Dm7
for pitch in [62, 65, 69, 71]:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=1.5,
        end=3.0
    )
    piano.notes.append(note)

# Bar 3: D7
for pitch in [62, 67, 69, 71]:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=3.0,
        end=4.5
    )
    piano.notes.append(note)

# Bar 4: Dmaj7
for pitch in [62, 67, 69, 73]:
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=4.5,
        end=6.0
    )
    piano.notes.append(note)

# ----------------------
# SAX: Tenor sax — your motif
# One short, haunting motif — 4 notes over 3 beats, ending on the 4th beat
# D (62), F# (67), A (69), B (71)

# Bar 1 (0.0 - 1.5s): No sax, just drums
# Bar 2 (1.5s): D (62)
# Bar 3 (1.875s): F# (67)
# Bar 4 (2.25s): A (69)
# Bar 5 (2.625s): B (71)

sax_notes = [
    (62, 1.5, 1.875),
    (67, 1.875, 2.25),
    (69, 2.25, 2.625),
    (71, 2.625, 3.0)
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(
        velocity=105,
        pitch=pitch,
        start=start,
        end=end
    )
    sax.notes.append(note)

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file written to 'dante_intro.mid'")
