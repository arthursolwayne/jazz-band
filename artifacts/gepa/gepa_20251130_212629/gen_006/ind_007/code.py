
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a track for each instrument
track_drums = pretty_midi.Instrument(program=10)  # Drums
track_piano = pretty_midi.Instrument(program=0)    # Piano
track_bass = pretty_midi.Instrument(program=33)    # Bass
track_sax = pretty_midi.Instrument(program=64)     # Tenor Sax

# Define D major scale for reference
D_major = [2, 4, 5, 7, 9, 11, 12]

# Time per beat in seconds
beat = 0.375
bar = 1.5  # 4 beats per bar

# Function to convert MIDI note number to pitch name
def note_to_name(note):
    return pretty_midi.note_number_to_name(note)

# ====================
# DRUMS: Little Ray
# ====================
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: Same pattern but with a few fills and variations
kick_note = pretty_midi.note_number_to_midi(36)  # C2
snare_note = pretty_midi.note_number_to_midi(38)  # D2
hihat_note = pretty_midi.note_number_to_midi(42)  # F#2

def add_drums(track, start_time):
    # Bar 1
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time, end=start_time + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=snare_note, start=start_time + beat, end=start_time + beat + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + beat/2, end=start_time + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + beat + beat/2, end=start_time + beat + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + beat*2, end=start_time + beat*2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + beat*2 + beat/2, end=start_time + beat*2 + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + beat*2, end=start_time + beat*2 + 0.1))

    # Bar 2
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + bar, end=start_time + bar + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=snare_note, start=start_time + bar + beat, end=start_time + bar + beat + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar + beat/2, end=start_time + bar + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar + beat + beat/2, end=start_time + bar + beat + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar + beat*2, end=start_time + bar + beat*2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar + beat*2 + beat/2, end=start_time + bar + beat*2 + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + bar + beat*2, end=start_time + bar + beat*2 + 0.1))

    # Bar 3
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + bar*2, end=start_time + bar*2 + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=snare_note, start=start_time + bar*2 + beat, end=start_time + bar*2 + beat + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*2 + beat/2, end=start_time + bar*2 + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*2 + beat + beat/2, end=start_time + bar*2 + beat + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*2 + beat*2, end=start_time + bar*2 + beat*2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*2 + beat*2 + beat/2, end=start_time + bar*2 + beat*2 + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + bar*2 + beat*2, end=start_time + bar*2 + beat*2 + 0.1))

    # Bar 4
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + bar*3, end=start_time + bar*3 + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=snare_note, start=start_time + bar*3 + beat, end=start_time + bar*3 + beat + 0.1))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*3 + beat/2, end=start_time + bar*3 + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*3 + beat + beat/2, end=start_time + bar*3 + beat + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*3 + beat*2, end=start_time + bar*3 + beat*2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=hihat_note, start=start_time + bar*3 + beat*2 + beat/2, end=start_time + bar*3 + beat*2 + beat/2 + 0.05))
    track.notes.append(pretty_midi.Note(velocity=100, pitch=kick_note, start=start_time + bar*3 + beat*2, end=start_time + bar*3 + beat*2 + 0.1))

add_drums(track_drums, 0.0)

# ====================
# PIANO: Diane
# ====================
# 7th chords, comp on 2 and 4
# D7 (D F# A C)
D7 = [50, 53, 57, 60]  # MIDI notes for D, F#, A, C
Bm7b5 = [59, 62, 64, 66]  # Bm7b5 (B D F A)
G7 = [67, 70, 74, 77]     # G7

# Bar 1: rest
# Bar 2: D7 on beat 2
# Bar 3: Bm7b5 on beat 2
# Bar 4: G7 on beat 2

def add_piano(track, start_time):
    # Bar 2: D7 on beat 2
    for note in D7:
        track.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start_time + beat, end=start_time + beat + 0.25))
    
    # Bar 3: Bm7b5 on beat 2
    for note in Bm7b5:
        track.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start_time + 2 * beat, end=start_time + 2 * beat + 0.25))
    
    # Bar 4: G7 on beat 2
    for note in G7:
        track.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start_time + 3 * beat, end=start_time + 3 * beat + 0.25))

add_piano(track_piano, 0.0)

# ====================
# BASS: Marcus
# ====================
# Walking line in D, chromatic approaches, no repetition
# D - Eb - E - F - F# - G - G# - A - A# - B - C - C# - D
# Bar 1: Rest
# Bar 2: D Eb E F F# G G# A
# Bar 3: A# B C C# D
# Bar 4: Eb E F F# G G# A

def add_bass(track, start_time):
    # Bar 2
    bass_notes = [50, 51, 52, 53, 54, 55, 56, 57]
    for i, note in enumerate(bass_notes):
        track.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start_time + i * beat, end=start_time + i * beat + 0.1))

    # Bar 3
    bass_notes = [58, 59, 60, 61, 62]
    for i, note in enumerate(bass_notes):
        track.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start_time + bar + i * beat, end=start_time + bar + i * beat + 0.1))

    # Bar 4
    bass_notes = [51, 52, 53, 54, 55, 56, 57]
    for i, note in enumerate(bass_notes):
        track.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start_time + bar*2 + i * beat, end=start_time + bar*2 + i * beat + 0.1))

add_bass(track_bass, 0.0)

# ====================
# SAX: Dante
# ====================
# Tenor sax — short motif, start it, leave it hanging, come back and finish it.
# The motif:
# - Bar 1: Rest
# - Bar 2: D (50) — quarter note
# - Bar 2: E (52) — eighth note
# - Bar 2: F# (53) — eighth note
# - Bar 3: Rest (half note)
# - Bar 4: D (50) — quarter note
# - Bar 4: F# (53) — quarter note

def add_sax(track, start_time):
    # Bar 2
    track.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start_time + 0, end=start_time + 0.75))  # D
    track.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=start_time + 0.75, end=start_time + 0.875))  # E
    track.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=start_time + 0.875, end=start_time + 1.25))  # F#

    # Bar 4
    track.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start_time + 2 * bar, end=start_time + 2 * bar + 0.75))  # D
    track.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=start_time + 2 * bar + 0.75, end=start_time + 2 * bar + 1.5))  # F#

add_sax(track_sax, 0.0)

# Add instruments to the PrettyMIDI object
pm.instruments.append(track_drums)
pm.instruments.append(track_piano)
pm.instruments.append(track_bass)
pm.instruments.append(track_sax)

# Save the MIDI file
pm.write("dante_intro.mid")
