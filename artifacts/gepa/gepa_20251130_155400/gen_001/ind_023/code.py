
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.instruments = []

# Define constants
BPM = 160
TEMPO = pretty_midi.MidiFile().time_signature_changes[0].tempo  # Default is 500,000 microseconds per beat
BEAT_DURATION = pretty_midi.note_number_to_hz(60) * 60 / BPM  # 1 beat in seconds
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time

# Function to convert beat to time
def beat_to_time(beat):
    return beat * BEAT_DURATION

# 1. Drums - Little Ray (Kick, Snare, Hihat)
drums = pretty_midi.Instrument(program=0)
drums.name = "Drums"

# Kick on 1 and 3
for bar in range(1):  # only 1 bar for kicks
    for beat in [0, 2]:  # beats 1 and 3 (0-based)
        note = pretty_midi.Note(
            velocity=100,
            pitch=36,  # Kick drum
            start=beat_to_time(beat),
            end=beat_to_time(beat) + 0.2
        )
        drums.notes.append(note)

# Snare on 2 and 4
for beat in [1, 3]:  # beats 2 and 4 (0-based)
    note = pretty_midi.Note(
        velocity=100,
        pitch=38,  # Snare drum
        start=beat_to_time(beat),
        end=beat_to_time(beat) + 0.2
    )
    drums.notes.append(note)

# Hihat on every eighth note
for beat in range(4):
    for eighth in range(2):
        time = beat_to_time(beat) + eighth * BEAT_DURATION / 2
        note = pretty_midi.Note(
            velocity=80,
            pitch=42,  # Hihat
            start=time,
            end=time + 0.1
        )
        drums.notes.append(note)

pm.instruments.append(drums)

# 2. Bass - Marcus (Walking line, chromatic, no repeated notes)
bass = pretty_midi.Instrument(program=33)
bass.name = "Bass"

# Bar 1: Little Ray alone (no bass)
# Bar 2-4: Walking bass line in F major
# Key: F major
# Chromatic walking line starting from F and moving up chromatically

# We'll use a simple chromatic pattern: F, F#, G, G#, A, A#, B, C, C#, D, D#, E, F
# Let's use 12 chromatic notes over 12 beats (each beat has a note)
chromatic_notes = [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]  # F to E chromatic

# Walking bass line over 3 bars (12 beats total)
for i in range(12):
    note = pretty_midi.Note(
        velocity=80,
        pitch=chromatic_notes[i % 12],
        start=beat_to_time(i),
        end=beat_to_time(i) + 0.25
    )
    bass.notes.append(note)

pm.instruments.append(bass)

# 3. Piano - Diane (7th chords on 2 and 4)
piano = pretty_midi.Instrument(program=0)
piano.name = "Piano"

# Chords in F major: F7, Bb7, C7, E7 (if you go to F major key, but in 4 bars, we'll use F7, Gm7, C7, F7)
# For comping, we'll play 7th chords on beats 2 and 4 in each bar

# Define 7th chords (root, 3rd, 7th)
def make_seventh_chord(root, type='major'):
    note = root
    if type == 'major':
        thirds = [4, 7]  # major 3rd, major 7th
    elif type == 'dominant':
        thirds = [4, 10]  # major 3rd, minor 7th
    elif type == 'minor':
        thirds = [3, 10]  # minor 3rd, minor 7th

    seventh_notes = [note + t for t in thirds]
    return seventh_notes

# Bar 1: No comping (Little Ray alone)
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: C7 (C, E, G, B)

# Bar 2: F7 on beat 2 and 4
chord_notes = make_seventh_chord(71, 'dominant')  # F7
for beat in [1, 3]:
    for note in chord_notes:
        piano_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=beat_to_time(beat),
            end=beat_to_time(beat) + 0.5
        )
        piano.notes.append(piano_note)

# Bar 3: Bb7 on beat 2 and 4
chord_notes = make_seventh_chord(70, 'dominant')  # Bb7
for beat in [1, 3]:
    for note in chord_notes:
        piano_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=beat_to_time(beat),
            end=beat_to_time(beat) + 0.5
        )
        piano.notes.append(piano_note)

# Bar 4: C7 on beat 2 and 4
chord_notes = make_seventh_chord(67, 'dominant')  # C7
for beat in [1, 3]:
    for note in chord_notes:
        piano_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=beat_to_time(beat),
            end=beat_to_time(beat) + 0.5
        )
        piano.notes.append(piano_note)

pm.instruments.append(piano)

# 4. Sax - Dante (Melody: unique motif that feels like a question or memory)
sax = pretty_midi.Instrument(program=64)
sax.name = "Saxophone"

# The sax line is the key. A simple, emotional motif that hangs and sings.
# Pattern: F, C, B, A, (rest), F (next bar start)

# Bar 1: Rest for setup
# Bar 2: Motif (F, C, B, A)
# Bar 3: Rest or continuation?
# Bar 4: End with F, resolving the question

# Bar 1: Rest
# Bar 2 (beat 0):
note = pretty_midi.Note(
    velocity=100,
    pitch=78,  # F
    start=beat_to_time(0),
    end=beat_to_time(0) + 0.5
)
sax.notes.append(note)

# Bar 2 (beat 1): C
note = pretty_midi.Note(
    velocity=100,
    pitch=72,  # C
    start=beat_to_time(1),
    end=beat_to_time(1) + 0.5
)
sax.notes.append(note)

# Bar 2 (beat 2): B
note = pretty_midi.Note(
    velocity=100,
    pitch=76,  # B
    start=beat_to_time(2),
    end=beat_to_time(2) + 0.5
)
sax.notes.append(note)

# Bar 2 (beat 3): A
note = pretty_midi.Note(
    velocity=100,
    pitch=74,  # A
    start=beat_to_time(3),
    end=beat_to_time(3) + 0.5
)
sax.notes.append(note)

# Bar 3: Rest or open space
# Bar 4: Return to F (resolution)
note = pretty_midi.Note(
    velocity=100,
    pitch=78,  # F
    start=beat_to_time(6),  # 6 beats in = 3rd bar, beat 0 of the 4th bar
    end=beat_to_time(6) + 0.5
)
sax.notes.append(note)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
