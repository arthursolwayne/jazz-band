
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key signature (F minor)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0.0)]  # 5 = F minor

# Define note durations (in seconds) based on 160 BPM
beat = 60.0 / 160.0  # 0.375 seconds per beat
bar = 4 * beat  # 1.5 seconds per bar

# Define instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# -- Bar 1: Little Ray (Drums) sets the mood
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_idx in range(1):
    bar_start = bar_idx * bar

    # Kick on 1 and 3
    kick_times = [bar_start + beat * i for i in [0, 2]]
    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)

    # Snare on 2 and 4
    snare_times = [bar_start + beat * i for i in [1, 3]]
    for time in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.1)
        drums.notes.append(note)

    # Hihat on every eighth
    for i in range(8):
        time = bar_start + beat * i / 2
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

# -- Bars 2-4: Full ensemble, with sax taking the melody
# Define sax melody: one short motif, starting on E (Fm7: F, Ab, Bb, D)
# E (D#) is the upper leading tone
# Motif: E, F, D, Bb — ascending and descending, with a note left hanging

melody = [
    (36, 0.5),  # E (D#) - start with the upper leading tone
    (37, 0.5),  # F
    (34, 0.5),  # D
    (30, 1.0),  # Bb (hang on the last note)
]

# Start the melody at bar 1.5 (start of bar 2)
melody_start = bar * 1.5  # 1.5 seconds in
time = melody_start

for pitch, duration in melody:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)
    time += duration

# -- Bass line: Marcus, walking line in Fm
# Fm7: F, Ab, Bb, D
# Chromatic approaches, no repeated notes

bass_line = [
    # Bar 1: F -> Gb (chromatic up)
    (36, 0.5),  # F
    (37, 0.5),  # Gb
    # Bar 2:
    (34, 0.5),  # D
    (35, 0.5),  # Eb
    # Bar 3:
    (30, 0.5),  # Bb
    (29, 0.5),  # A
    # Bar 4:
    (36, 0.5),  # F
    (37, 0.5),  # Gb
]

time = 0.0
for pitch, duration in bass_line:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)
    time += duration

# -- Piano: Diane, 7th chords on 2 and 4, moving the harmony
# Fm7 (F, Ab, Bb, D), Eb7 (Eb, G, Bb, D), Bb7 (Bb, D, F, Ab), Ab7 (Ab, C, Eb, G)

piano_notes = []

# Bar 2: Fm7 on 2 (beat 2)
time = bar * 1.5 + beat  # start of bar 2, beat 2
for pitch in [36, 48, 46, 50]:  # F, Ab, Bb, D
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.5)
    piano_notes.append(note)

# Bar 3: Eb7 on 2
time = bar * 2.5 + beat
for pitch in [46, 49, 46, 50]:  # Eb, G, Bb, D
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.5)
    piano_notes.append(note)

# Bar 4: Bb7 on 2
time = bar * 3.5 + beat
for pitch in [46, 50, 36, 48]:  # Bb, D, F, Ab
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.5)
    piano_notes.append(note)

piano.notes.extend(piano_notes)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
