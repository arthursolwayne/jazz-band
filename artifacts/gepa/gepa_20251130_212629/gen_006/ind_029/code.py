
import pretty_midi
from pretty_midi import Note, Instrument

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: F major
key = 'F'

# Define the tempo in BPM
bpm = 160
beat_duration = 60 / bpm  # seconds per beat
bar_duration = beat_duration * 4  # seconds per bar

# Create instruments
drums = Instrument(program=12, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# -----------------------------
# Bar 1: Drums only — tension and space
# -----------------------------

# Define the drum pattern for Bar 1 (starting at time 0)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 4 beats
time = 0.0

# Kick (Bass Drum) on 1 and 3
drums.notes.append(Note(36, 100, time, time + 0.15))
drums.notes.append(Note(36, 100, time + beat_duration * 2, time + beat_duration * 2 + 0.15))

# Snare (Snare Drum) on 2 and 4
drums.notes.append(Note(38, 100, time + beat_duration, time + beat_duration + 0.1))
drums.notes.append(Note(38, 100, time + beat_duration * 3, time + beat_duration * 3 + 0.1))

# Hi-Hat on every 8th note
for i in range(8):
    hihat_time = time + (beat_duration / 8) * i
    drums.notes.append(Note(42, 80, hihat_time, hihat_time + 0.05))

# -----------------------------
# Bar 2-4: Full ensemble — melody, bass, piano, sax
# -----------------------------

# Time starts at bar 1 end (bar 1 = 6 seconds)
time = bar_duration  # Start of Bar 2

# -----------------------------
# Bass line: Chromatic, walking, grounded
# -----------------------------
# F major: F, G, A, Bb, C, D, Eb
# Bass line: F, G#, A, Bb, C, D, Eb, F
# Bars 2-4 = 12 beats total

bass_notes = [
    (0, 72, 60, 0.3),  # F
    (0, 74, 60, 0.3),  # G#
    (0, 76, 60, 0.3),  # A
    (0, 77, 60, 0.3),  # Bb
    (0, 79, 60, 0.3),  # C
    (0, 81, 60, 0.3),  # D
    (0, 83, 60, 0.3),  # Eb
    (0, 72, 60, 0.3),  # F
    (0, 74, 60, 0.3),  # G#
    (0, 76, 60, 0.3),  # A
    (0, 77, 60, 0.3),  # Bb
    (0, 79, 60, 0.3),  # C
]

for i, (pitch, velocity, duration) in enumerate(bass_notes):
    note = Note(pitch, velocity, time + i * beat_duration, time + i * beat_duration + duration)
    bass.notes.append(note)

# -----------------------------
# Piano: 7th chords, comp on 2 and 4
# -----------------------------
# Use Fmaj7 (F, A, C, E), G7 (G, Bb, D, F)
# Comp on beats 2 and 4 of bars 2 and 3
# Bar 2: beat 2: Fmaj7, beat 4: G7
# Bar 3: beat 2: Fmaj7, beat 4: G7
# Bar 4: beat 2: Fmaj7, beat 4: rest

piano_notes = [
    (60, 90, 0.3, time + beat_duration * 1),  # F (Fmaj7) - beat 2 of bar 2
    (64, 90, 0.3, time + beat_duration * 1),
    (67, 90, 0.3, time + beat_duration * 1),
    (69, 90, 0.3, time + beat_duration * 1),
    
    (62, 90, 0.3, time + beat_duration * 3),  # G7 (beat 4 of bar 2)
    (65, 90, 0.3, time + beat_duration * 3),
    (67, 90, 0.3, time + beat_duration * 3),
    (69, 90, 0.3, time + beat_duration * 3),

    (60, 90, 0.3, time + beat_duration * 5),  # Fmaj7 (beat 2 of bar 3)
    (64, 90, 0.3, time + beat_duration * 5),
    (67, 90, 0.3, time + beat_duration * 5),
    (69, 90, 0.3, time + beat_duration * 5),

    (62, 90, 0.3, time + beat_duration * 7),  # G7 (beat 4 of bar 3)
    (65, 90, 0.3, time + beat_duration * 7),
    (67, 90, 0.3, time + beat_duration * 7),
    (69, 90, 0.3, time + beat_duration * 7),

    (60, 90, 0.3, time + beat_duration * 9),  # Fmaj7 (beat 2 of bar 4)
    (64, 90, 0.3, time + beat_duration * 9),
    (67, 90, 0.3, time + beat_duration * 9),
    (69, 90, 0.3, time + beat_duration * 9),
]

for pitch, velocity, duration, start_time in piano_notes:
    note = Note(pitch, velocity, start_time, start_time + duration)
    piano.notes.append(note)

# -----------------------------
# Drums: Same pattern as Bar 1, repeated for Bars 2-4
# -----------------------------
# Copy the bar 1 drum pattern to bars 2-4
for i in range(3):  # 3 more bars
    for note in drums.notes:
        new_note = Note(note.pitch, note.velocity, note.start + bar_duration * (i + 1), note.end + bar_duration * (i + 1))
        drums.notes.append(new_note)

# -----------------------------
# Tenor Sax: Melody — one short motif
# -----------------------------
# Start at the beginning of Bar 2 (time = bar_duration)
# Motif: F, G#, A, Bb (ascending, but with a twist)
# Play the motif on beats 1 and 2 of bar 2, then leave it hanging until bar 4

# Let's make it a call and response — F -> G# -> A -> Bb -> (rest)
# Notes: F (60), G# (62), A (65), Bb (62), then rest

sax_notes = [
    (60, 100, 0.3, time),  # F on beat 1
    (62, 100, 0.3, time + beat_duration),  # G# on beat 2
    (65, 100, 0.3, time + beat_duration * 2),  # A on beat 3
    (62, 100, 0.3, time + beat_duration * 3),  # Bb on beat 4
    (60, 100, 0.3, time + beat_duration * 4),  # F again on beat 5 (repeat)
    (62, 100, 0.3, time + beat_duration * 5),  # G# again on beat 6
    (65, 100, 0.3, time + beat_duration * 6),  # A again on beat 7
    (62, 100, 0.3, time + beat_duration * 7),  # Bb again on beat 8
    (60, 100, 0.3, time + beat_duration * 8),  # F again on beat 9
    (62, 100, 0.3, time + beat_duration * 9),  # G# again on beat 10
    (65, 100, 0.3, time + beat_duration * 10),  # A again on beat 11
    (62, 100, 0.3, time + beat_duration * 11),  # Bb again on beat 12
]

for pitch, velocity, duration, start_time in sax_notes:
    note = Note(pitch, velocity, start_time, start_time + duration)
    sax.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")

print("MIDI file created: 'dante_russo_intro.mid'")
