
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set tempo to 160 BPM
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Create instruments for each player
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drums use the percussion bank

sax = pretty_midi.Instrument(program=saxophone_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [sax, bass, piano, drums]

# Define the key: Fm (F minor)
key = 'Fm'

# Define the time in seconds per bar (160 BPM, 4/4)
time_per_bar = 60.0 / 160 * 4
time_per_beat = time_per_bar / 4

# Helper function to convert note names to MIDI numbers
def note_to_midi(note):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1,
        'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6,
        'G': 7, 'G#': 8, 'Ab': 8,
        'A': 9, 'A#': 10, 'Bb': 10,
        'B': 11
    }
    octave = int(note[-1])
    note_name = note[:-1]
    midi = note_map[note_name] + (octave + 1) * 12
    return midi

# Define the Fm scale: F, Gb, G, Ab, A, Bb, B
Fm_notes = [note_to_midi('F4'), note_to_midi('Gb4'), note_to_midi('G4'), 
            note_to_midi('Ab4'), note_to_midi('A4'), note_to_midi('Bb4'), note_to_midi('B4')]

# --- Bar 1: Drums only, building tension ---
# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=1.5, end=1.875))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375))

# Hi-hat on every eighth note with slight dynamics
for i in range(0, 4):
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.0625
    velocity = 90 if i % 2 == 0 else 80
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=42, start=hihat_start, end=hihat_end))

# --- Bars 2-4: Full ensemble, sax takes the motif ---

# Define the saxophone motif (Fm, Ab, Bb, A, F) – simple, emotive, with space
sax_notes = [
    # Bar 2, beat 1
    pretty_midi.Note(velocity=105, pitch=note_to_midi('F4'), start=1.5, end=1.75),
    # Bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Ab4'), start=1.75, end=2.0),
    # Bar 2, beat 3
    pretty_midi.Note(velocity=95, pitch=note_to_midi('Bb4'), start=2.0, end=2.25),
    # Bar 2, beat 4
    pretty_midi.Note(velocity=90, pitch=note_to_midi('A4'), start=2.25, end=2.5),
    # Bar 3, beat 1
    pretty_midi.Note(velocity=105, pitch=note_to_midi('F4'), start=3.0, end=3.25),
    # Bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Ab4'), start=3.25, end=3.5),
    # Bar 3, beat 3
    pretty_midi.Note(velocity=95, pitch=note_to_midi('Bb4'), start=3.5, end=3.75),
    # Bar 3, beat 4
    pretty_midi.Note(velocity=90, pitch=note_to_midi('A4'), start=3.75, end=4.0),
    # Bar 4, beat 1
    pretty_midi.Note(velocity=105, pitch=note_to_midi('F4'), start=4.5, end=4.75),
    # Bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=note_to_midi('Ab4'), start=4.75, end=5.0),
    # Bar 4, beat 3
    pretty_midi.Note(velocity=95, pitch=note_to_midi('Bb4'), start=5.0, end=5.25),
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=note_to_midi('A4'), start=5.25, end=5.5),
]

sax.notes.extend(sax_notes)

# --- Bass line (walking with melodic intent in Fm) ---

# Bass line in Fm: F - Gb - G - A - Bb - B - C - Db - E - F
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=note_to_midi('F3'), start=1.5, end=1.75),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('Gb3'), start=1.75, end=2.0),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('G3'), start=2.0, end=2.25),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('A3'), start=2.25, end=2.5),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('Bb3'), start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('B3'), start=3.25, end=3.5),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('C3'), start=3.5, end=3.75),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('Db3'), start=3.75, end=4.0),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('E3'), start=4.5, end=4.75),
    pretty_midi.Note(velocity=70, pitch=note_to_midi('F3'), start=4.75, end=5.0),
]

bass.notes.extend(bass_notes)

# --- Piano comping with emotional tension (7th chords, 2 and 4) ---

# Define 7th chords in Fm
Fm7 = [note_to_midi('F3'), note_to_midi('Ab3'), note_to_midi('Bb3'), note_to_midi('C4')]
Ab7 = [note_to_midi('Ab3'), note_to_midi('B3'), note_to_midi('Db4'), note_to_midi('E4')]
Bb7 = [note_to_midi('Bb3'), note_to_midi('Db4'), note_to_midi('Eb4'), note_to_midi('F4')]
A7 = [note_to_midi('A3'), note_to_midi('C4'), note_to_midi('E4'), note_to_midi('G4')]

# Comp on beat 2 and 4 of each bar
piano_notes = []

# Bar 2, beat 2: Fm7
for note in Fm7:
    piano_notes.append(pretty_midi.Note(velocity=75, pitch=note, start=1.75, end=2.0))

# Bar 2, beat 4: Ab7
for note in Ab7:
    piano_notes.append(pretty_midi.Note(velocity=75, pitch=note, start=2.25, end=2.5))

# Bar 3, beat 2: Bb7
for note in Bb7:
    piano_notes.append(pretty_midi.Note(velocity=75, pitch=note, start=3.25, end=3.5))

# Bar 3, beat 4: A7
for note in A7:
    piano_notes.append(pretty_midi.Note(velocity=75, pitch=note, start=3.75, end=4.0))

# Bar 4, beat 2: Fm7 again
for note in Fm7:
    piano_notes.append(pretty_midi.Note(velocity=75, pitch=note, start=4.75, end=5.0))

# Bar 4, beat 4: Leave it hanging, only the root
piano_notes.append(pretty_midi.Note(velocity=70, pitch=note_to_midi('F3'), start=5.25, end=5.5))

piano.notes.extend(piano_notes)

# Save as a MIDI file
pm.write('jazz_intro_f_minor.mid')
