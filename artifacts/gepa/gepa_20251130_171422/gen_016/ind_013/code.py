
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)  # 160 BPM

# Define the time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: Dm (D minor)
# F = 70, Cm = 60, Dm = 62
# We’ll use a ii-V-i progression over 4 bars: F7, G7, Cm7, Dm7

# Time per bar (1.5 seconds), beat = 0.375s
BAR_DURATION = 1.5
BEAT_DURATION = 0.375
NOTE_DURATION = 0.25  # quarter note

# Create instruments
drum_program = pretty_midi.instrument_name_to_program("Acoustic Drums")
bass_program = pretty_midi.instrument_name_to_program("Double Bass")
piano_program = pretty_midi.instrument_name_to_program("Electric Piano 2")
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")

drum_instrument = pretty_midi.Instrument(program=drum_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_instrument, bass_instrument, piano_instrument, sax_instrument]

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    # Kick on 1 and 3
    kick_times = [bar * BAR_DURATION + i * BEAT_DURATION for i in [0, 2]]
    for t in kick_times:
        drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.05))

    # Snare on 2 and 4
    snare_times = [bar * BAR_DURATION + i * BEAT_DURATION for i in [1, 3]]
    for t in snare_times:
        drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.05))

    # Hihat on every eighth (8 notes per bar)
    for i in range(8):
        t = bar * BAR_DURATION + i * BEAT_DURATION / 2
        drum_instrument.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=t, end=t + 0.02))

# --- BASS: Marcus ---
# Walking line with chromatic approaches
# Key: Dm (D, F, A, C)
# Over 4 bars, we walk through F7, G7, Cm7, Dm7
# We’ll use a chromatic line with root, b7, root, b7, etc.

bass_notes = [
    # Bar 1: F7 -> root (F), b7 (E), F, E
    71, 70, 71, 70,
    # Bar 2: G7 -> root (G), b7 (F#), G, F#
    76, 75, 76, 75,
    # Bar 3: Cm7 -> root (C), b7 (Bb), C, Bb
    60, 62, 60, 62,
    # Bar 4: Dm7 -> root (D), b7 (C), D, C
    62, 60, 62, 60
]

for i, pitch in enumerate(bass_notes):
    time = i * BEAT_DURATION
    bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + NOTE_DURATION))

# --- PIANO: Diane ---
# Comp on 2 and 4, 7th chords
# F7, G7, Cm7, Dm7
# Comp on 2 and 4 of each bar

comp = [
    # Bar 1: F7 on beat 2
    (1 * BEAT_DURATION, 71, 70, 69, 67),  # F, A, C, E♭
    # Bar 1: G7 on beat 4
    (3 * BEAT_DURATION, 76, 78, 71, 69),  # G, B, D, F
    # Bar 2: G7 on beat 2 (same chord for now)
    (1 * BEAT_DURATION + BAR_DURATION, 76, 78, 71, 69),
    # Bar 2: Cm7 on beat 4
    (3 * BEAT_DURATION + BAR_DURATION, 60, 62, 58, 65),  # C, E♭, G, B♭
    # Bar 3: Cm7 on beat 2
    (1 * BEAT_DURATION + 2 * BAR_DURATION, 60, 62, 58, 65),
    # Bar 3: Dm7 on beat 4
    (3 * BEAT_DURATION + 2 * BAR_DURATION, 62, 64, 60, 59),  # D, F, A, C
    # Bar 4: Dm7 on beat 2
    (1 * BEAT_DURATION + 3 * BAR_DURATION, 62, 64, 60, 59),
    # Bar 4: Some final comp on beat 4
    (3 * BEAT_DURATION + 3 * BAR_DURATION, 62, 64, 60, 59)
]

for t, root, seventh, third, fifth in comp:
    # Play chord: root + third + fifth + seventh
    for pitch in [root, third, fifth, seventh]:
        piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.2))

# --- SAX: Dante Russo ---
# Short motif: D, F, A, C — but leave it hanging

# Bar 1: Start the motif
# D (62), F (65), A (69), C (60)
# Let it hang on the C, then come back on bar 4

sax_notes = [
    # Bar 1: D, F, A, C (ends on C)
    (0, 62, 0.25),
    (0.25, 65, 0.25),
    (0.5, 69, 0.25),
    (0.75, 60, 0.25),
    
    # Bar 2: Silence
    (1.0, 60, 0.0),  # nothing
    
    # Bar 3: Silence
    (2.0, 60, 0.0),  # nothing
    
    # Bar 4: Return with the motif, but finish it this time
    (3.0, 62, 0.25),
    (3.25, 65, 0.25),
    (3.5, 69, 0.25),
    (3.75, 60, 0.75)  # finish on C, slightly longer
]

for start, pitch, duration in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Save the MIDI file
pm.write('dante_jazz_intro.mid')
print("MIDI file saved as 'dante_jazz_intro.mid'")
