
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor
key = 'Fm'

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drums_program)

tenor_sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
tenor = pretty_midi.Instrument(program=tenor_sax_program)

pm.instruments = [bass, piano, drums, tenor]

# Define time in seconds per bar (160 BPM = 6/160 = 0.375 seconds per beat)
bar_length = 1.5  # 4/4 at 160 BPM
beat_length = 0.375  # 1 beat is 0.375 seconds
beat_offset = 0.0

# --- Bar 1: Little Ray on drums only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=beat_offset, end=beat_offset + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=beat_offset + 2*beat_length, end=beat_offset + 2*beat_length + 0.1))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_offset + beat_length, end=beat_offset + beat_length + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_offset + 3*beat_length, end=beat_offset + 3*beat_length + 0.1))

# Hi-hat on every eighth note
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=beat_offset + i * beat_length / 2, end=beat_offset + i * beat_length / 2 + 0.05))

# --- Bar 2: Everyone in, tenor begins the melody ---
beat_offset += bar_length

# Bass line: walking line, roots and fifths with chromatic approaches
# Fm7: F, Ab, C, Eb
# Bass line: F -> Gb (chromatic approach to G) -> G -> Ab -> A (chromatic approach to Bb) -> Bb -> C -> Db (chromatic approach to D) -> D -> Eb (root)
bass_notes = [
    (37, 0.0, 0.1),     # F
    (39, 0.375, 0.4),    # Gb
    (40, 0.75, 0.85),    # G
    (38, 1.125, 1.225),  # Ab
    (41, 1.5, 1.6),      # A
    (42, 1.875, 1.975),  # Bb
    (44, 2.25, 2.35),    # C
    (45, 2.625, 2.725),  # Db
    (46, 2.999, 3.099)   # D (end of bar)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# Piano chords: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Open voicing: F, C, Ab, Eb
piano_notes = [
    (53, 0.0, 0.1),  # F (C4)
    (55, 0.0, 0.1),  # Ab (C4)
    (58, 0.0, 0.1),  # C (C5)
    (60, 0.0, 0.1),  # Eb (C5)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# Tenor sax: short motif, make it sing
# Motif: F (Ab), D (Bb), Eb (C), F (Ab) — a simple, descending melodic idea with chromatic tension
tenor_notes = [
    (53, 0.0, 0.3),  # F (C4) with space
    (51, 0.6, 0.9),  # D (Bb3)
    (55, 1.2, 1.5),  # Eb (C4)
    (53, 1.8, 2.1)   # F (C4) — resolving back
]
for pitch, start, end in tenor_notes:
    tenor.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# --- Bar 3: Drums continue, piano adds comp, tenor continues motif ---
beat_offset += bar_length

# Continue drumming the same pattern
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=beat_offset + i * beat_length / 2, end=beat_offset + i * beat_length / 2 + 0.05))

# Piano: D7sus (D, F#, A, D)
# Open voicing: D, A, F#, D
piano_notes = [
    (50, 0.0, 0.1),   # D
    (57, 0.0, 0.1),   # A
    (55, 0.0, 0.1),   # F#
    (50, 0.0, 0.1),   # D
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# Tenor sax: continues motif with a slight variation
tenor_notes = [
    (53, 0.0, 0.3),  # F (C4)
    (51, 0.6, 0.9),  # D (Bb3)
    (55, 1.2, 1.5),  # Eb (C4)
    (53, 1.8, 2.1)   # F (C4)
]
for pitch, start, end in tenor_notes:
    tenor.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# --- Bar 4: Resolution, everyone plays, tenor finishes the motif ---
beat_offset += bar_length

# Drums: same pattern
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=beat_offset + i * beat_length / 2, end=beat_offset + i * beat_length / 2 + 0.05))

# Piano: Cm7 (C, Eb, G, Bb)
# Open voicing: C, G, Eb, Bb
piano_notes = [
    (52, 0.0, 0.1),  # C
    (58, 0.0, 0.1),  # G
    (55, 0.0, 0.1),  # Eb
    (53, 0.0, 0.1),  # Bb
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# Bass: resolves to C (root of Cm7)
bass_notes = [
    (52, 0.0, 0.1),  # C
]
bass.notes.append(pretty_midi.Note(velocity=70, pitch=52, start=beat_offset, end=beat_offset + 0.1))

# Tenor sax: finishes the motif with a final note
tenor_notes = [
    (53, 0.0, 0.3),  # F (C4)
]
for pitch, start, end in tenor_notes:
    tenor.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + beat_offset, end=end + beat_offset))

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
