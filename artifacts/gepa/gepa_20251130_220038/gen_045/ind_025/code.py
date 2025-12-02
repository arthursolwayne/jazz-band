
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # 480 ticks per quarter note

# Tempo
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempos = [pretty_midi.TempoChange(160.0, 0)]

# Function to create a note
def create_note(midi_note, start, end, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=midi_note, start=start, end=end)
    return note

# Define the time per bar (160 BPM, 4/4 = 1.5 seconds per bar)
bar_length = 1.5  # seconds
beat_length = bar_length / 4  # 0.375 seconds per beat
tick_per_beat = pm.resolution * beat_length  # ticks per beat
tick_per_bar = tick_per_beat * 4  # ticks per bar

# Create instruments
drum_program = pretty_midi.Instrument(program=10)  # Drums
piano_program = pretty_midi.Instrument(program=0)   # Piano
bass_program = pretty_midi.Instrument(program=33)   # Electric Bass
sax_program = pretty_midi.Instrument(program=64)    # Tenor Sax

pm.instruments = [drum_program, piano_program, bass_program, sax_program]

# --- DRUMS (Little Ray) ---
# Kick on 1 & 3
# Snare on 2 & 4
# Hi-hat on every eighth
for bar in range(4):
    bar_start = bar * tick_per_bar

    # Kick on 1 & 3
    kick_beats = [0, 2]
    for kick_beat in kick_beats:
        kick_start = bar_start + kick_beat * tick_per_beat
        kick_end = kick_start + 0.25 * tick_per_beat
        drum_program.notes.append(create_note(36, kick_start, kick_end, velocity=100))

    # Snare on 2 & 4
    snare_beats = [1, 3]
    for snare_beat in snare_beats:
        snare_start = bar_start + snare_beat * tick_per_beat
        snare_end = snare_start + 0.25 * tick_per_beat
        drum_program.notes.append(create_note(38, snare_start, snare_end, velocity=100))

    # Hi-hat on every eighth
    for eighth in range(8):
        eighth_start = bar_start + (eighth / 2) * tick_per_beat
        eighth_end = eighth_start + 0.125 * tick_per_beat
        drum_program.notes.append(create_note(42, eighth_start, eighth_end, velocity=70))

    # Subtle fills
    if bar == 1:
        fill_start = bar_start + 2.5 * tick_per_beat
        fill_end = fill_start + 0.25 * tick_per_beat
        drum_program.notes.append(create_note(46, fill_start, fill_end, velocity=90))
    elif bar == 3:
        fill_start = bar_start + 1.5 * tick_per_beat
        fill_end = fill_start + 0.25 * tick_per_beat
        drum_program.notes.append(create_note(46, fill_start, fill_end, velocity=90))

# --- PIANO (Diane) ---
# Chords on beats 2 and 4: Dm7, F7, Bbm7, G7
chord_intervals = [
    (['D', 'F', 'A', 'C'], 1),  # Dm7
    (['F', 'A', 'C', 'E'], 2),  # F7
    (['Bb', 'D', 'F', 'A'], 3), # Bbm7
    (['G', 'B', 'D', 'F'], 4)   # G7
]

for bar in range(4):
    bar_start = bar * tick_per_bar
    for i, (notes, beat) in enumerate(chord_intervals):
        if i < len(chord_intervals) and bar == i:
            beat_start = bar_start + beat * tick_per_beat
            beat_end = beat_start + 0.25 * tick_per_beat
            for note_name in notes:
                midi_note = pretty_midi.note_number_from_name(note_name)
                piano_program.notes.append(create_note(midi_note, beat_start, beat_end, velocity=80))

# --- BASS (Marcus) ---
# Walking line with chromatic movements
bass_notes = [62, 60, 59, 57, 55, 53, 52, 62, 60, 59, 57, 55, 53, 52, 62, 60]  # D to C with chromatics
bass_start = 0

for i, note in enumerate(bass_notes):
    note_start = bass_start + i * (tick_per_beat / 4)
    note_end = note_start + (tick_per_beat / 4)
    bass_program.notes.append(create_note(note, note_start, note_end, velocity=90))

# --- SAX (You) ---
# First note: F (65), E (64), D (62) on beat 1 of bar 1
sax_notes = [
    (65, 0 * tick_per_beat, 0.25 * tick_per_beat),  # F
    (64, 0 * tick_per_beat, 0.25 * tick_per_beat),  # E
    (62, 0 * tick_per_beat, 0.25 * tick_per_beat),  # D

    # Silence for bar 2
    (0, 1 * tick_per_bar, 2 * tick_per_bar),  # Silence
    (0, 2 * tick_per_bar, 3 * tick_per_bar),  # Silence
    (0, 3 * tick_per_bar, 4 * tick_per_bar),  # Silence

    # Repeat the motif but change the last note to C (60)
    (65, 3 * tick_per_bar, 3.25 * tick_per_bar),  # F
    (64, 3 * tick_per_bar, 3.25 * tick_per_bar),  # E
    (60, 3 * tick_per_bar, 3.25 * tick_per_bar)   # C
]

for note, start, end in sax_notes:
    sax_program.notes.append(create_note(note, start, end, velocity=100))

# Write to MIDI file
pm.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
