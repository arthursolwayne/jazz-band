
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 4 bars at 160 BPM (6 seconds total)
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.instruments = []

# Set tempo
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Function to create a note
def note_on(time, pitch, velocity, duration, instrument):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    instrument.notes.append(note)

# Create instruments
bass = pretty_midi.Instrument(program=33)  # Acoustic Bass
piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums
sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Time per bar: 1.5 seconds at 160 BPM
bar_duration = 1.5
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# BAR 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time for bar 1
time = 0.0
# Kick on 1
note_on(time, pretty_midi.note_name_to_number('C1'), 90, beat_duration, drums)
# Snare on 2
note_on(time + beat_duration, pretty_midi.note_name_to_number('C2'), 90, beat_duration, drums)
# Kick on 3
note_on(time + 2*beat_duration, pretty_midi.note_name_to_number('C1'), 90, beat_duration, drums)
# Snare on 4
note_on(time + 3*beat_duration, pretty_midi.note_name_to_number('C2'), 90, beat_duration, drums)

# Hihat on every eighth
for i in range(8):
    note_on(time + i * beat_duration / 2, pretty_midi.note_name_to_number('C6'), 60, beat_duration / 2, drums)

# BAR 2: Everyone in. Diane (Piano) plays a chord, Marcus (Bass) walks, sax enters

time = bar_duration

# Diane - Open voicings, resolve on the last bar
# Bar 2: Fm7 -> Bb7 -> Eb7 -> Am7 (Fm -> Bb -> Eb -> Am)
# Let's use these chords in open voicings, comp on 2 and 4

# Fm7: F (root), Ab (minor 3rd), Bb (perfect 4th), C (major 7th)
note_on(time, pretty_midi.note_name_to_number('F4'), 80, beat_duration * 0.25, piano)
note_on(time, pretty_midi.note_name_to_number('Ab4'), 80, beat_duration * 0.25, piano)
note_on(time, pretty_midi.note_name_to_number('Bb4'), 80, beat_duration * 0.25, piano)
note_on(time, pretty_midi.note_name_to_number('C5'), 80, beat_duration * 0.25, piano)

# Marcus - Walking bass line (roots and fifths, chromatic approaches)
# Fm7 -> Bb7 -> Eb7 -> Am7
# Bass notes: F, Ab, D, Bb, Eb, G, A, C
note_on(time, pretty_midi.note_name_to_number('F2'), 80, beat_duration, bass)
note_on(time + beat_duration, pretty_midi.note_name_to_number('Ab2'), 80, beat_duration, bass)
note_on(time + 2*beat_duration, pretty_midi.note_name_to_number('D2'), 80, beat_duration, bass)
note_on(time + 3*beat_duration, pretty_midi.note_name_to_number('Bb2'), 80, beat_duration, bass)

# BAR 3: Sax enters with a motif

# Melody: F (start), Ab (chromatic), Bb (fifth), F (return), Eb (step down), D (chromatic down)
note_on(time + beat_duration * 0.3, pretty_midi.note_name_to_number('F5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 0.6, pretty_midi.note_name_to_number('Ab5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 0.9, pretty_midi.note_name_to_number('Bb5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 1.2, pretty_midi.note_name_to_number('F5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 1.5, pretty_midi.note_name_to_number('Eb5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 1.8, pretty_midi.note_name_to_number('D5'), 100, beat_duration * 0.3, sax)

# BAR 4: Resolve with a Bb7 chord, sax finishes motif

time = 2 * bar_duration

# Bb7 chord
note_on(time, pretty_midi.note_name_to_number('Bb4'), 80, beat_duration * 0.25, piano)
note_on(time, pretty_midi.note_name_to_number('D4'), 80, beat_duration * 0.25, piano)
note_on(time, pretty_midi.note_name_to_number('F4'), 80, beat_duration * 0.25, piano)
note_on(time, pretty_midi.note_name_to_number('Ab4'), 80, beat_duration * 0.25, piano)

# Marcus continues walking
note_on(time, pretty_midi.note_name_to_number('Eb2'), 80, beat_duration, bass)
note_on(time + beat_duration, pretty_midi.note_name_to_number('G2'), 80, beat_duration, bass)
note_on(time + 2*beat_duration, pretty_midi.note_name_to_number('A2'), 80, beat_duration, bass)
note_on(time + 3*beat_duration, pretty_midi.note_name_to_number('C3'), 80, beat_duration, bass)

# Sax finishes the motif
note_on(time + beat_duration * 0.3, pretty_midi.note_name_to_number('Bb5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 0.6, pretty_midi.note_name_to_number('F5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 0.9, pretty_midi.note_name_to_number('D5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 1.2, pretty_midi.note_name_to_number('Bb5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 1.5, pretty_midi.note_name_to_number('F5'), 100, beat_duration * 0.3, sax)
note_on(time + beat_duration * 1.8, pretty_midi.note_name_to_number('Eb5'), 100, beat_duration * 0.3, sax)

# Save the MIDI
pm.write("dante_russo_intro.mid")
