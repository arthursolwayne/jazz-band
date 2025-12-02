
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)  # 160 BPM

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instrument tracks
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Define time in seconds (1 bar = 1.5 seconds, 4 bars = 6 seconds)
bar_length = 1.5
note_duration = 0.375  # 1/4 note at 160 BPM
half_note = note_duration * 2
quarter_note = note_duration
eighth_note = note_duration / 2

# Define the key: F Major
key = 'F'
scale_degrees = [0, 2, 4, 5, 7, 9, 11]  # F major scale (C=0)
scale_notes = [f + 72 for f in [72 + i for i in scale_degrees]]  # F is MIDI note 72

# Set up time
time = 0.0

# ----------------------------- DRUMS -----------------------------
# Bar 1: Drums only
drums_notes = [
    # Kick on 1 and 3
    (0, 36, time + 0.0, quarter_note),  # Kick on 1
    (0, 36, time + 0.75, quarter_note), # Kick on 3
    # Snare on 2 and 4
    (0, 38, time + 0.375, quarter_note), # Snare on 2
    (0, 38, time + 1.125, quarter_note), # Snare on 4
    # Hi-hat on every eighth
    (0, 42, time + 0.0, eighth_note),
    (0, 42, time + 0.375, eighth_note),
    (0, 42, time + 0.75, eighth_note),
    (0, 42, time + 1.125, eighth_note),
    (0, 42, time + 1.5, eighth_note),
    (0, 42, time + 1.875, eighth_note),
    (0, 42, time + 2.25, eighth_note),
    (0, 42, time + 2.625, eighth_note),
]
for note in drums_notes:
    velocity, pitch, start, duration = note
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    drums.notes.append(note)
time += bar_length

# ----------------------------- BASS, PIANO, SAX -----------------------------
# Bar 2: Everyone in
# Bass line: Chromatic walking line, avoiding repetition
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
bass_notes = [
    (72, time + 0.0, eighth_note),  # F
    (73, time + 0.375, eighth_note), # Gb
    (74, time + 0.75, eighth_note),  # G
    (75, time + 1.125, eighth_note), # Ab
    (76, time + 1.5, eighth_note),   # A
    (77, time + 1.875, eighth_note), # Bb
    (78, time + 2.25, eighth_note),  # B
    (79, time + 2.625, eighth_note), # C
]
for note in bass_notes:
    pitch, start, duration = note
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = []
# F7 on 2
for pitch in [72, 76, 79, 81]:  # F, A, C, D
    piano_notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time + 0.375, end=time + 0.75))
# Bb7 on 4
for pitch in [77, 80, 82, 84]:  # Bb, D, F, G
    piano_notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time + 1.125, end=time + 1.5))
for note in piano_notes:
    piano.notes.append(note)

# Tenor Sax: Melody (short motif, sing, leave it hanging, come back)
sax_notes = [
    (76, time + 0.0, eighth_note),  # A
    (78, time + 0.375, eighth_note), # B
    (76, time + 0.75, eighth_note),  # A
    (74, time + 1.125, eighth_note), # G
    (72, time + 1.5, eighth_note),   # F
    (76, time + 1.875, eighth_note), # A
    (78, time + 2.25, eighth_note),  # B
    (76, time + 2.625, eighth_note), # A
]
for note in sax_notes:
    pitch, start, duration = note
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)
midi.instruments.append(sax)

# Save the MIDI file
midi.write("dante_intro.mid")
