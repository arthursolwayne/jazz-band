
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define key and time signature
key = 'Dm'  # D minor
time_signature = (4, 4)

# Set up instruments
instrument_drums = pretty_midi.instruments.PercussionInstrument(program=0)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_sax = pretty_midi.Instrument(program=64)

pm.instruments = [instrument_drums, instrument_piano, instrument_bass, instrument_sax]

# Time per bar in seconds (60 / 160 = 0.375s per beat, 1.5s per bar)
time_per_beat = 0.375
time_per_bar = 1.5

# Define note durations
eighth = time_per_beat / 2
quarter = time_per_beat
half = time_per_beat * 2
whole = time_per_beat * 4

# Dm scale: D, Eb, F, G, Ab, Bb, C
# Dm7 chord: D, F, Ab, C

# BAR 1: Little Ray on drums (Kick on 1 & 3, snare on 2 & 4, hihat on every eighth)
# Time: 0.0s to 1.5s

# Kick on 1 and 3
kick_times = [0.0, 0.75]
kick_notes = [36, 36]  # Kick drum
for t, n in zip(kick_times, kick_notes):
    note = pretty_midi.Note(velocity=80, pitch=n, start=t, end=t + 0.1)
    instrument_drums.notes.append(note)

# Snare on 2 and 4
snare_times = [0.375, 1.125]
snare_notes = [38, 38]  # Snare drum
for t, n in zip(snare_times, snare_notes):
    note = pretty_midi.Note(velocity=90, pitch=n, start=t, end=t + 0.05)
    instrument_drums.notes.append(note)

# Hi-hats on every eighth
hihat_times = [0.0, 0.375, 0.75, 1.125]
hihat_notes = [42, 42, 42, 42]  # Closed hihat
for t, n in zip(hihat_times, hihat_notes):
    note = pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.075)
    instrument_drums.notes.append(note)

# BAR 2: Diane on piano (2 and 4, 7th chords, moving)
# Time: 1.5s to 3.0s

# Use Dm7 chord (D, F, Ab, C)
# Root on 2 and 4, but Dm7 is a voicing
# Diane plays a descending bass line on beat 2 and 4

piano_notes = [
    (1.5 + 0.375, 62, 100, 0.1),  # F (3rd)
    (1.5 + 0.75, 60, 100, 0.1),  # D (root)
    (1.5 + 1.125, 64, 100, 0.1),  # Ab (5th)
    (1.5 + 1.5, 67, 100, 0.1),   # C (7th)
]

for t, p, v, d in piano_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    instrument_piano.notes.append(note)

# BAR 2: Marcus on bass (walking line, chromatic movement)
# Time: 1.5s to 3.0s

# Dm7 walking line: D, Eb, F, G, Ab, Bb, C, D
# Start on beat 2, walk up to beat 4
bass_notes = [
    (1.5 + 0.375, 62, 90, 0.1),  # Eb
    (1.5 + 0.75, 64, 90, 0.1),  # F
    (1.5 + 1.125, 67, 90, 0.1),  # G
    (1.5 + 1.5, 69, 90, 0.1),   # Ab
]

for t, p, v, d in bass_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    instrument_bass.notes.append(note)

# BAR 2: Little Ray (same as before, but with subtle variation)
# Use same kick and snare, but vary hihat on last eighth

# Kick and snare same as before
# Hihat slightly different on 4th eighth
hihat_times = [1.5 + 0.0, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125]
hihat_notes = [42, 42, 42, 42]  # Closed hihat
for t, n in zip(hihat_times, hihat_notes):
    note = pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.075)
    instrument_drums.notes.append(note)

# BAR 3: Diane on piano (comping on 2 and 4, 7th chords, more motion)
# Time: 3.0s to 4.5s

# Dm7, then Gm7 (ii-V), chromatic movement

piano_notes = [
    (3.0 + 0.375, 62, 100, 0.1),  # F (3rd)
    (3.0 + 0.75, 60, 100, 0.1),  # D (root)
    (3.0 + 1.125, 64, 100, 0.1),  # Ab (5th)
    (3.0 + 1.5, 67, 100, 0.1),   # C (7th)
]

for t, p, v, d in piano_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    instrument_piano.notes.append(note)

# BAR 3: Marcus on bass (walking line, chromatic movement)
# Time: 3.0s to 4.5s

# Continue chromatic walk: Bb, C, D, Eb
bass_notes = [
    (3.0 + 0.375, 65, 90, 0.1),  # Bb
    (3.0 + 0.75, 67, 90, 0.1),  # C
    (3.0 + 1.125, 69, 90, 0.1),  # D
    (3.0 + 1.5, 71, 90, 0.1),   # Eb
]

for t, p, v, d in bass_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    instrument_bass.notes.append(note)

# BAR 3: Little Ray (same as before, but with subtle variation)
# Use same kick and snare, but vary hihat on last eighth

# Kick and snare same as before
# Hihat slightly different on 4th eighth
hihat_times = [3.0 + 0.0, 3.0 + 0.375, 3.0 + 0.75, 3.0 + 1.125]
hihat_notes = [42, 42, 42, 42]  # Closed hihat
for t, n in zip(hihat_times, hihat_notes):
    note = pretty_midi.Note(velocity=100, pitch=n, start=t, end=t + 0.075)
    instrument_drums.notes.append(note)

# BAR 4: You on sax — the motif. One short phrase, sing it, leave it hanging.

# Time: 4.5s to 6.0s
# Motif: D, F, Ab, C — Dm7 arpeggio, but with space and tension
# Start on beat 1, end on beat 2 with a rest

sax_notes = [
    (4.5, 62, 100, 0.1),  # F
    (4.5 + 0.375, 60, 100, 0.1),  # D
    (4.5 + 0.75, 64, 100, 0.1),  # Ab
    (4.5 + 1.125, 67, 100, 0.1),  # C
]

for t, p, v, d in sax_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    instrument_sax.notes.append(note)

# Write the MIDI to disk
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
