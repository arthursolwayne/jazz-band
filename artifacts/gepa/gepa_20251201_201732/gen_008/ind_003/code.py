
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Key signature: F minor
pm.key_signature_changes = [pretty_midi.KeySignature(midi=-3, time=0.0)]

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# BPM = 160 => beat = 0.375 seconds
# Bar duration = 1.5 seconds

# Helper functions
def note_to_midi(note_name):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1,
        'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6,
        'G': 7, 'G#': 8, 'Ab': 8,
        'A': 9, 'A#': 10, 'Bb': 10,
        'B': 11
    }
    return note_map[note_name]

def note_to_midi_with_octave(note_name, octave):
    note = note_to_midi(note_name)
    return note + 12 * (octave + 1)

def create_note(note, time, duration, velocity=100):
    return pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0.0 - 1.5 seconds
for bar in range(1):  # 4 bars total, but we're only doing bar 1 for drums
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick_times = [bar_start + 0.0, bar_start + 0.75]
    for t in kick_times:
        drums.notes.append(create_note(note_to_midi_with_octave('C', 3), t, 0.1))
    # Snare on 2 and 4
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    for t in snare_times:
        drums.notes.append(create_note(note_to_midi_with_octave('C', 3), t, 0.1))
    # Hihat on every eighth
    for i in range(8):
        hihat_time = bar_start + i * 0.375
        drums.notes.append(create_note(note_to_midi_with_octave('C', 5), hihat_time, 0.1))

# Bass line: Fm (F, Ab, D, C) with chromatic approaches and walking line in Fm
# Bar 1: F -> Eb -> D -> C
# Bar 2: Ab -> G -> F -> E
# Bar 3: D -> C -> Bb -> A
# Bar 4: C -> Bb -> B -> F

def bass_line():
    bars = 4
    bar_start = 0.0
    # Bar 1
    bass.notes.append(create_note(note_to_midi_with_octave('F', 2), bar_start, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('Eb', 2), bar_start + 0.375, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('D', 2), bar_start + 0.75, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('C', 2), bar_start + 1.125, 0.375))
    # Bar 2
    bar_start += 1.5
    bass.notes.append(create_note(note_to_midi_with_octave('Ab', 2), bar_start, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('G', 2), bar_start + 0.375, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('F', 2), bar_start + 0.75, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('E', 2), bar_start + 1.125, 0.375))
    # Bar 3
    bar_start += 1.5
    bass.notes.append(create_note(note_to_midi_with_octave('D', 2), bar_start, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('C', 2), bar_start + 0.375, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('Bb', 2), bar_start + 0.75, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('A', 2), bar_start + 1.125, 0.375))
    # Bar 4
    bar_start += 1.5
    bass.notes.append(create_note(note_to_midi_with_octave('C', 2), bar_start, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('Bb', 2), bar_start + 0.375, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('B', 2), bar_start + 0.75, 0.375))
    bass.notes.append(create_note(note_to_midi_with_octave('F', 2), bar_start + 1.125, 0.375))

bass_line()

# Piano: Open voicings, different chord each bar, resolve on the last
def piano_comp():
    bar_start = 0.0
    # Bar 1: Fm7 (F, Ab, C, Eb)
    piano.notes.append(create_note(note_to_midi_with_octave('F', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('Ab', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('C', 5), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('Eb', 5), bar_start + 0.0, 0.375))
    # Bar 2: F7 (F, A, C, Eb)
    bar_start += 1.5
    piano.notes.append(create_note(note_to_midi_with_octave('F', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('A', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('C', 5), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('Eb', 5), bar_start + 0.0, 0.375))
    # Bar 3: Bb7 (Bb, D, F, Ab)
    bar_start += 1.5
    piano.notes.append(create_note(note_to_midi_with_octave('Bb', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('D', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('F', 5), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('Ab', 5), bar_start + 0.0, 0.375))
    # Bar 4: Cm7 (C, Eb, G, Bb)
    bar_start += 1.5
    piano.notes.append(create_note(note_to_midi_with_octave('C', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('Eb', 4), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('G', 5), bar_start + 0.0, 0.375))
    piano.notes.append(create_note(note_to_midi_with_octave('Bb', 5), bar_start + 0.0, 0.375))

piano_comp()

# Sax: Motif — F, Ab, D, C (Fm triad with D as passing tone)
def sax_line():
    bar_start = 1.5  # Start on bar 2
    # First note: F on beat 1
    sax.notes.append(create_note(note_to_midi_with_octave('F', 6), bar_start, 0.375))
    # Second note: Ab on beat 2
    sax.notes.append(create_note(note_to_midi_with_octave('Ab', 6), bar_start + 0.375, 0.375))
    # Third note: D on beat 3
    sax.notes.append(create_note(note_to_midi_with_octave('D', 6), bar_start + 0.75, 0.375))
    # Fourth note: C on beat 4
    sax.notes.append(create_note(note_to_midi_with_octave('C', 6), bar_start + 1.125, 0.375))

sax_line()

# Save the MIDI file
pm.write('four_bar_intro.mid')
