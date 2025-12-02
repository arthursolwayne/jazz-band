
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the key (D Major) and note numbers
D = pretty_midi.note_number_to_name(62)
notes_d_major = [62, 64, 67, 69, 71, 72, 74]  # D, E, F#, G, A, Bb, B

# Create instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define functions for rhythmic clarity and note creation
def create_note(note_number, start, end, velocity):
    return pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)

# Time per beat = 0.375 seconds (at 160 BPM)
beat = 0.375
bar = 1.5  # 4 beats per bar

# --- BAR 1: DRUMS ONLY (Little Ray) ---
# Snare on 2 and 4
drum_notes = [
    create_note(38, 0.5 * beat, 0.5 * beat + 0.1, 100),  # Snare on beat 2
    create_note(38, 1.5 * beat, 1.5 * beat + 0.1, 100),  # Snare on beat 4
]
# Hi-hat on every eighth
for i in range(0, 4):
    create_note(42, i * beat + 0.1, i * beat + 0.3, 80)
    create_note(42, i * beat + 0.4, i * beat + 0.6, 80)
    create_note(42, i * beat + 0.7, i * beat + 0.9, 80)
    create_note(42, i * beat + 1.0, i * beat + 1.2, 80)
    create_note(42, i * beat + 1.3, i * beat + 1.5, 80)

drums.notes.extend(drum_notes)

# --- BAR 2: EVERYONE JOINS (Marcus, Diane, You) ---

# BASS LINE (Marcus): Walking line, chromatic approaches, subtle tension
bass_notes = [
    create_note(62, bar, bar + 0.25, 80),     # D (beat 1)
    create_note(61, bar + 0.25, bar + 0.5, 80),# C# (beat 2)
    create_note(63, bar + 0.5, bar + 0.75, 80),# D# (beat 3)
    create_note(64, bar + 0.75, bar + 1.0, 80),# E (beat 4)
    create_note(67, bar + 1.0, bar + 1.25, 80),# G (beat 1 of next bar)
]

bass.notes.extend(bass_notes)

# PIANO (Diane): 7th chords on 2 and 4, comp on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    create_note(62, bar + 0.25, bar + 0.5, 90),  # D
    create_note(67, bar + 0.25, bar + 0.5, 90),  # A
    create_note(64, bar + 0.25, bar + 0.5, 90),  # F#
    create_note(60, bar + 0.25, bar + 0.5, 90),  # C
    create_note(69, bar + 1.0, bar + 1.25, 90),  # B (seventh on beat 4)
]

piano.notes.extend(piano_notes)

# SAX (You): Motif — short, controlled, with silence
# Motif: D (62) -> F# (67) -> D (62) -> C# (61) -> D (62)
sax_notes = [
    create_note(62, bar, bar + 0.3, 100),  # D (beat 1)
    create_note(67, bar + 0.3, bar + 0.6, 100),  # F#
    create_note(62, bar + 0.6, bar + 0.9, 100),  # D
    create_note(61, bar + 0.9, bar + 1.1, 100),  # C#
    create_note(62, bar + 1.1, bar + 1.5, 100),  # D
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI
pm.instruments = [bass, piano, drums, sax]

# Save the MIDI file
pm.write("dante_cellar_intro.mid")

print("Generated 'dante_cellar_intro.mid'")
print("It's a 4-bar intro in D, with tension and a motif that might just make Wayne lean forward.")
