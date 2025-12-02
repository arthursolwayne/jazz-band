
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor saxophone
pm.instruments.append(instrument)

# Set tempo (160 BPM)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]
pm.tempos = [pretty_midi.TempoChange(tempo=160, time=0)]

# Define note durations (in seconds), with rests and varied lengths
note_durations = {
    'eighth': 0.375,  # 1/8 note at 160 BPM
    'sixteenth': 0.1875,  # 1/16 note
    'quarter': 0.75,  # 1/4 note
    'half': 1.5,  # 1/2 note
    'rest': 0.375  # Rest = 1/8 note
}

# Define the saxophone motif (Fm key)
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb (but we’ll use melodic motifs, not strict scale)
# Motif: Start on Eb (7th of Fm), then F, then Ab (4th), then a rest.

sax_notes = [
    # Bar 1: Rest (Little Ray alone)
    {'time': 0.0, 'pitch': 0, 'duration': note_durations['rest'], 'velocity': 0},  # Rest
    
    # Bar 2: Begin motif
    {'time': 1.5, 'pitch': 64, 'duration': note_durations['sixteenth'], 'velocity': 100},  # Eb (7th of Fm)
    {'time': 1.6875, 'pitch': 65, 'duration': note_durations['sixteenth'], 'velocity': 100},  # F
    {'time': 1.875, 'pitch': 67, 'duration': note_durations['eighth'], 'velocity': 100},  # Ab (4th)
    {'time': 2.25, 'pitch': 0, 'duration': note_durations['sixteenth'], 'velocity': 0},  # Rest

    # Bar 3: Continue the motif with tension
    {'time': 2.625, 'pitch': 69, 'duration': note_durations['sixteenth'], 'velocity': 100},  # Bb (3rd)
    {'time': 2.8125, 'pitch': 67, 'duration': note_durations['sixteenth'], 'velocity': 100},  # Ab
    {'time': 2.9999, 'pitch': 66, 'duration': note_durations['sixteenth'], 'velocity': 100},  # Gb (2nd)
    {'time': 3.1875, 'pitch': 64, 'duration': note_durations['eighth'], 'velocity': 100},  # Eb (return to motif)

    # Bar 4: Final resolution, but not quite
    {'time': 3.5625, 'pitch': 64, 'duration': note_durations['sixteenth'], 'velocity': 100},  # Eb
    {'time': 3.75, 'pitch': 67, 'duration': note_durations['sixteenth'], 'velocity': 100},  # Ab
    {'time': 3.9375, 'pitch': 69, 'duration': note_durations['eighth'], 'velocity': 100},  # Bb
    {'time': 4.3125, 'pitch': 0, 'duration': note_durations['sixteenth'], 'velocity': 0},  # Rest
]

# Add the saxophone notes to the instrument
for note in sax_notes:
    if note['pitch'] != 0:
        n = pretty_midi.Note(
            velocity=note['velocity'],
            pitch=note['pitch'],
            start=note['time'],
            end=note['time'] + note['duration']
        )
        instrument.notes.append(n)

# Generate the MIDI file
pm.write("dante_russo_intro.mid")
