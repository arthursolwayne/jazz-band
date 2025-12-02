
import pretty_midi
import numpy as np

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Set key to D major
key = 'D'

# Define time for 4 bars at 160 BPM (each bar = 1.5 seconds)
bar_length = 1.5
total_length = 4 * bar_length

# Initialize instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define note values in seconds
beat_duration = 0.375  # 160 BPM, 4/4 time
half_beat = beat_duration / 2
quarter_beat = beat_duration
eighth_beat = beat_duration / 2
dotted_eighth = beat_duration * 1.5

# --- DRUMS: Little Ray (Bars 1-4) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0, end=0.375))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75))  # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5))  # Hihat on 4

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25))  # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0))  # Hihat on 4

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75))  # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5))  # Hihat on 4

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25))  # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625))  # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))  # Hihat on 4

# --- BASS: Marcus (Bars 1-4) ---
# Walking line with chromatic approaches, never the same note twice, in D major

# D = 62
# Chromatic line: D -> C# -> B -> A -> G -> F# -> E -> D

bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]  # 8 notes, one beat each

for i, pitch in enumerate(bass_notes):
    start_time = i * beat_duration
    end_time = start_time + beat_duration
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=end_time))

# --- PIANO: Diane (Bars 1-4) ---
# 7th chords on 2 and 4, D7, A7, D7, A7

def chord_notes(root, seventh):
    d7 = [62, 67, 72, 76]
    a7 = [69, 74, 79, 81]
    return [d7, a7][root == 69]

# Bar 1: D7 on beat 2
bar1 = chord_notes(62, 76)
for note in bar1:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=0.375, end=0.75))

# Bar 2: A7 on beat 2
bar2 = chord_notes(69, 81)
for note in bar2:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.875, end=2.25))

# Bar 3: D7 on beat 2
bar3 = chord_notes(62, 76)
for note in bar3:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.375, end=3.75))

# Bar 4: A7 on beat 2
bar4 = chord_notes(69, 81)
for note in bar4:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.875, end=5.25))

# --- SAX: Dante (Bars 1-4) ---
# Melody: short motif, sing, leave it hanging, finish it

# Motif: D (62) -> F# (67) -> B (71) -> D (62), but delayed on last note

# First phrase
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=0, end=0.375))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=0.375, end=0.75))  # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=0.75, end=1.125))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D

# Add a slight delay on the last note
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25))  # D (delayed)

# Save the MIDI file
pm.write('dante_intro.mid')
