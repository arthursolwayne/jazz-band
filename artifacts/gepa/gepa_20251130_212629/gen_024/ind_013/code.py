
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set up key signature (F major)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major is key number 5

# Define the time in seconds per bar
bpm = 160
beats_per_bar = 4
seconds_per_bar = 60.0 / bpm * beats_per_bar
seconds_per_beat = seconds_per_bar / beats_per_bar

# Define the note durations
note_duration = 0.25  # quarter note

# Define the tempo in ticks per beat (default is 480)
ticks_per_beat = pm.resolution

# Define the time in ticks for each bar
ticks_per_bar = ticks_per_beat * beats_per_bar

# Define the instruments
# 1. Drums (Little Ray)
program_drums = 0
instrument_drums = pretty_midi.Instrument(program=program_drums)
pm.instruments.append(instrument_drums)

# 2. Bass (Marcus)
program_bass = 33
instrument_bass = pretty_midi.Instrument(program=program_bass)
pm.instruments.append(instrument_bass)

# 3. Piano (Diane)
program_piano = 0
instrument_piano = pretty_midi.Instrument(program=program_piano)
pm.instruments.append(instrument_piano)

# 4. Tenor Sax (You)
program_sax = 64
instrument_sax = pretty_midi.Instrument(program=program_sax)
pm.instruments.append(instrument_sax)

# Bar 1: Drums only
# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
def add_drum_notes(instrument, bar_start, kick_notes, snare_notes, hihat_notes):
    for note in kick_notes:
        time = bar_start + note
        instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.25))
    for note in snare_notes:
        time = bar_start + note
        instrument.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.25))
    for note in hihat_notes:
        time = bar_start + note
        instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bar 1 (0 to 1.5 seconds)
kick = [0.0]
snare = [0.5, 1.0]
hihat = np.arange(0.0, 1.5, 0.125)
add_drum_notes(instrument_drums, 0.0, kick, snare, hihat)

# Bar 2: Everyone enters. Tenor sax starts with a motif.
# Tenor sax motif: F (G4), Bb (A4), C (B4), Eb (C5) — searching, unresolved
notes_sax = [
    (0.0, 66, 100),  # F (G4)
    (0.25, 69, 100), # Bb (A4)
    (0.5, 71, 100),  # C (B4)
    (0.75, 64, 100)  # Eb (C5)
]
for time, pitch, velocity in notes_sax:
    instrument_sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25))

# Bass line: Walking line in F (F, G, A, Bb, C, D, Eb, F)
bass_notes = [
    (0.0, 65, 70),  # F3
    (0.25, 67, 70), # G3
    (0.5, 69, 70),  # A3
    (0.75, 66, 70), # Bb3
    (1.0, 71, 70),  # C3
    (1.25, 72, 70), # D3
    (1.5, 64, 70),  # Eb3
]
for time, pitch, velocity in bass_notes:
    instrument_bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
def add_piano_notes(instrument, bar_start, chords, times):
    for time, chord in zip(times, chords):
        start = bar_start + time
        for note in chord:
            instrument.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25))

# Chords: F7 (F, A, C, Eb) on 2 and 4
chords = [
    [65, 69, 71, 64],  # F7 (F3, A3, C4, Eb4)
    [65, 69, 71, 64]   # F7 again
]
times = [0.5, 1.0]
add_piano_notes(instrument_piano, 0.0, chords, times)

# Save the MIDI file
pm.write("jazz_intro_moment.mid")
