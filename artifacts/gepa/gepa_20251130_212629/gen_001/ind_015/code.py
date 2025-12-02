
import pretty_midi
import numpy as np

# Constants
BPM = 160
TEMPO = 60 / BPM  # seconds per beat
BEAT_DURATION = TEMPO
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
NOTE_DURATION = BEAT_DURATION / 2  # Half note duration (quarter note is 0.375s)

# Create a MIDI file
pm = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor sax
pm.instruments.append(instrument)

# --- Bar 1: Little Ray on drums (0.0 - 1.5s) ---

# Create a drum track
drums = pretty_midi.Instrument(program=0)
pm.instruments.append(drums)

# Kick on 1 and 3
for bar in range(1):
    kick_on = [0.0, 0.75]  # beats 1 and 3
    for beat in kick_on:
        time = bar * 4 * BEAT_DURATION + beat * BEAT_DURATION
        note = pretty_midi.Note(
            velocity=100,
            pitch=36,  # Kick
            start=time,
            end=time + 0.1
        )
        drums.notes.append(note)

# Snare on 2 and 4
for bar in range(1):
    snare_on = [1.0, 2.0]  # beats 2 and 4
    for beat in snare_on:
        time = bar * 4 * BEAT_DURATION + beat * BEAT_DURATION
        note = pretty_midi.Note(
            velocity=80,
            pitch=38,  # Snare
            start=time,
            end=time + 0.08
        )
        drums.notes.append(note)

# Hihat on every eighth
for bar in range(1):
    for beat in range(0, 4):
        for eighth in [0, 0.5]:
            time = bar * 4 * BEAT_DURATION + beat * BEAT_DURATION + eighth * BEAT_DURATION / 2
            note = pretty_midi.Note(
                velocity=60,
                pitch=42,  # Hihat
                start=time,
                end=time + 0.04
            )
            drums.notes.append(note)

# --- Bar 2–4: All instruments enter ---

# Key: F major
# Notes in F major: F, G, A, Bb, C, D, E

# ✅ Tenor sax (Dante) melody: spaced, with a pause
# Motif: F - G - rest - Bb - rest - C - rest - D
# Each note is a quarter note, but with rests

note_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

notes = [
    (65, 0.0, 0.375),  # F (65)
    (67, 0.375, 0.75),  # G (67)
    (None, 0.75, 1.125),  # rest
    (69, 1.125, 1.5),  # Bb (69)
    (None, 1.5, 1.875),  # rest
    (60, 1.875, 2.25),  # C (60)
    (None, 2.25, 2.625),  # rest
    (62, 2.625, 3.0)  # D (62)
]

for pitch, start_time, end_time in notes:
    if pitch is not None:
        note = pretty_midi.Note(
            velocity=100,
            pitch=pitch,
            start=start_time,
            end=end_time
        )
        instrument.notes.append(note)

# --- Marcus: Walking bass line in F major (chromatic approaches) ---

# Walking bass in F major with chromatic approaches
# Pattern: F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F (chromatic)
bass_notes = [
    (53, 0.0, 0.375),  # F (53)
    (54, 0.375, 0.75),  # Gb (54)
    (55, 0.75, 1.125),  # G (55)
    (56, 1.125, 1.5),  # Ab (56)
    (57, 1.5, 1.875),  # A (57)
    (58, 1.875, 2.25),  # Bb (58)
    (59, 2.25, 2.625),  # B (59)
    (60, 2.625, 3.0),  # C (60)
    (62, 3.0, 3.375),  # D (62)
    (63, 3.375, 3.75),  # Eb (63)
    (64, 3.75, 4.125),  # E (64)
    (65, 4.125, 4.5)  # F (65)
]

bass_instrument = pretty_midi.Instrument(program=33)  # Upright bass
pm.instruments.append(bass_instrument)

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(
        velocity=80,
        pitch=pitch,
        start=start,
        end=end
    )
    bass_instrument.notes.append(note)

# --- Diane: Piano (7th chords, comping on 2 and 4) ---

# 7th chords in F major: F7, G7, Am7, Bb7, C7, D7, E7
# Comp on beats 2 and 4

piano_instrument = pretty_midi.Instrument(program=0)  # Acoustic piano
pm.instruments.append(piano_instrument)

# F7 (F, A, C, E)
# Duration: quarter note (0.375s)
for bar in [1, 2, 3]:
    time = bar * 4 * BEAT_DURATION + 1.0 * BEAT_DURATION  # beat 2
    chord = [65, 68, 72, 69]
    for pitch in chord:
        note = pretty_midi.Note(
            velocity=80,
            pitch=pitch,
            start=time,
            end=time + NOTE_DURATION
        )
        piano_instrument.notes.append(note)

    time = bar * 4 * BEAT_DURATION + 2.0 * BEAT_DURATION  # beat 4
    chord = [65, 68, 72, 69]
    for pitch in chord:
        note = pretty_midi.Note(
            velocity=80,
            pitch=pitch,
            start=time,
            end=time + NOTE_DURATION
        )
        piano_instrument.notes.append(note)

# --- Save the MIDI file ---

pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.save('dante_intro.mid')

print("MIDI file created: 'dante_intro.mid'")
