
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signature (4/4)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Define the key: F Major
key = 'F'

# Define the tempo
tempo = 160  # BPM
beat_duration = 60.0 / tempo  # seconds per beat
bar_duration = beat_duration * 4  # seconds per bar

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Key of F
f_major = ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']
f_notes = [pretty_midi.note_number_from_name(n) for n in f_major]

# Define the chords for each bar (open voicings)
chords = {
    0: [pretty_midi.note_number_from_name('F'), pretty_midi.note_number_from_name('A'), pretty_midi.note_number_from_name('C')],
    1: [pretty_midi.note_number_from_name('G'), pretty_midi.note_number_from_name('Bb'), pretty_midi.note_number_from_name('D')],
    2: [pretty_midi.note_number_from_name('A'), pretty_midi.note_number_from_name('C'), pretty_midi.note_number_from_name('E')],
    3: [pretty_midi.note_number_from_name('Bb'), pretty_midi.note_number_from_name('D'), pretty_midi.note_number_from_name('F')],
}

# Define bass line: roots and fifths with chromatic approaches
bass_line = [
    pretty_midi.note_number_from_name('F'),  # Bar 1
    pretty_midi.note_number_from_name('G'),  # Bar 2
    pretty_midi.note_number_from_name('A'),  # Bar 3
    pretty_midi.note_number_from_name('Bb'), # Bar 4
]

# Define timing for each bar
bar_start_times = [0, bar_duration, bar_duration * 2, bar_duration * 3]

# Define bass line (walking line)
for bar_idx, note in enumerate(bass_line):
    time = bar_start_times[bar_idx]
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + beat_duration))

# Define piano chords (comp on 2 and 4 of each bar)
for bar_idx, chord in chords.items():
    start_time = bar_start_times[bar_idx]
    chord_notes = [note + 12 for note in chord]  # Middle C octave
    for note in chord_notes:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time + 1 * beat_duration, end=start_time + 1 * beat_duration + 0.375))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time + 3 * beat_duration, end=start_time + 3 * beat_duration + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_idx in range(4):
    start_time = bar_start_times[bar_idx]
    
    # Kick on 1 and 3
    kick_time = start_time
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick)
    
    kick_time = start_time + 2 * beat_duration
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick)
    
    # Snare on 2 and 4
    snare_time = start_time + beat_duration
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare)
    
    snare_time = start_time + 3 * beat_duration
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare)
    
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start_time + i * (beat_duration / 8)
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.0625)
        drums.notes.append(hihat)

# Sax melody: short motif, leave it hanging
sax_notes = [pretty_midi.note_number_from_name('F'), pretty_midi.note_number_from_name('Bb'), pretty_midi.note_number_from_name('C'), pretty_midi.note_number_from_name('F')]
sax_durations = [0.25, 0.5, 0.25, 0.5]  # Total: 1.5 seconds (4 bars)

# Start the sax melody at bar 1 (time 0)
sax_time = 0
for i, note in enumerate(sax_notes):
    start = sax_time
    end = sax_time + sax_durations[i]
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))
    sax_time += sax_durations[i]

# Save the MIDI file
pm.write("jazz_intro_f_major.mid")

print("MIDI file generated: jazz_intro_f_major.mid")
