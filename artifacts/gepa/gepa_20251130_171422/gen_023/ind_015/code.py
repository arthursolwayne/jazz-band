
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define key: F Major
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major is key number 5

# Define note durations in seconds
note_duration = 0.375  # 1/8 note at 160 BPM
bar_duration = 1.5     # 4/4 bar at 160 BPM

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # for MIDI drum kit

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

# Add instruments to the MIDI file
pm.instruments = [sax, bass, piano, drums]

# --- BAR 1: DRUMS ONLY ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 4):
    time = i * note_duration
    # Kick on 1 and 3
    if i % 2 == 0:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_duration)
        drums.notes.append(kick)
    # Snare on 2 and 4
    if i % 2 == 1:
        snare = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + note_duration)
        drums.notes.append(snare)
    # Hi-hat on every eighth
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + note_duration)
    drums.notes.append(hihat)

# --- BAR 2: SAX INTRO (F7 - G7 - A#7 - F7) ---
# The saxophone motif is a simple but haunting four-note phrase starting on F7
# (F7 is the 7th of F major — the leading tone, unresolved)
sax_notes = [113, 115, 118, 113]  # F7, G7, A#7, F7
for i, pitch in enumerate(sax_notes):
    start = bar_duration + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# --- BAR 2: PIANO COMPING (7th chords on 2 and 4) ---
# F7, Bb7 on beat 2 and 4
piano_notes = [
    (113, 0), (117, 0), (110, 0), (112, 0),  # F7
    (119, 0), (113, 0), (107, 0), (109, 0),  # Bb7
]
for i, (pitch, velocity) in enumerate(piano_notes):
    start = bar_duration + (i % 4) * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# --- BAR 2: BASS WALKING LINE (F - G - Ab - A - Bb - C - D - Eb) ---
# Chromatic walking line, resolving to Bb (the 4th)
bass_notes = [53, 55, 57, 58, 59, 60, 62, 63]  # F, G, Ab, A, Bb, C, D, Eb
for i, pitch in enumerate(bass_notes):
    start = bar_duration + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# --- BAR 3: SAX REPEAT + PIANO COMPLAINING ---
# Repeat the saxophone motif but with slight variation (a half-step up)
sax_notes_var = [114, 116, 119, 114]  # F#7, G#7, B7, F#7
for i, pitch in enumerate(sax_notes_var):
    start = 2 * bar_duration + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# PIANO: same pattern but with a sense of tension
piano_notes_var = [
    (114, 0), (118, 0), (111, 0), (113, 0),  # F#7
    (119, 0), (113, 0), (107, 0), (109, 0),  # Bb7
]
for i, (pitch, velocity) in enumerate(piano_notes_var):
    start = 2 * bar_duration + (i % 4) * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# --- BAR 3: BASS WALKING LINE (A - Bb - C - D - Eb - F - G - Ab) ---
# Chromatic walking line, resolving to Ab
bass_notes_var = [58, 59, 60, 62, 63, 53, 55, 57]  # A, Bb, C, D, Eb, F, G, Ab
for i, pitch in enumerate(bass_notes_var):
    start = 2 * bar_duration + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# --- BAR 4: SAX RESOLUTION (F7 -> G7) ---
# The saxophone motif ends on G7, unresolved and haunting
sax_notes_res = [113, 115, 118, 115]  # F7, G7, A#7, G7
for i, pitch in enumerate(sax_notes_res):
    start = 3 * bar_duration + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# --- BAR 4: PIANO COMPLAINING (G7 CHORD) ---
# G7 chord with a lot of tension
piano_notes_res = [
    (115, 0), (119, 0), (112, 0), (114, 0),  # G7 chord
]
for i, (pitch, velocity) in enumerate(piano_notes_res):
    start = 3 * bar_duration + (i % 4) * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# --- BAR 4: BASS WALKING LINE (G - A - Bb - B - C - D - Eb - F) ---
# Chromatic walking line, resolving to F
bass_notes_res = [55, 57, 59, 60, 60, 62, 63, 53]  # G, A, Bb, B, C, D, Eb, F
for i, pitch in enumerate(bass_notes_res):
    start = 3 * bar_duration + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Save the MIDI file
pm.write('cellar_intro.mid')

print("MIDI file created: 'cellar_intro.mid'")
