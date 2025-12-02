
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key (F minor)
key = 'Fm'

# Time per bar (160 BPM, 4/4 time)
time_per_bar = 60.0 / 160 * 4  # 1.5 seconds per bar
time_per_beat = time_per_bar / 4  # 0.375 seconds per beat

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# Bar 1: Drums only — setting the mood
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in range(1):
    for beat in range(4):
        time = bar * time_per_bar + beat * time_per_beat

        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)

        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.1)
            drums.notes.append(note)

        # Hihat on every 8th
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bar 2: All instruments in
# Time starts at 1.5 seconds

# Bass line – walking line in F minor (F, Gb, Ab, A, Bb, B, C, Db)
# Using chromatic approaches, no repeated notes
bass_notes = [71, 69, 67, 66, 64, 65, 67, 65]  # F, Gb, Ab, A, Bb, B, C, Db
for i, pitch in enumerate(bass_notes):
    time = i * time_per_beat + time_per_bar  # start at bar 2 (1.5 seconds)
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano – 7th chords, comp on 2 and 4
# F7, Ab7, Bb7, C7 (simplified for clarity)
chords = [
    [53, 57, 60, 62],  # F7 (F, A, C, Eb)
    [58, 62, 64, 67],  # Ab7 (Ab, C, Db, F)
    [55, 58, 60, 62],  # Bb7 (Bb, D, F, Ab)
    [57, 60, 64, 67],  # C7 (C, E, G, Bb)
]
for beat, chord in enumerate(chords):
    time = beat * time_per_beat + time_per_bar
    for pitch in chord:
        note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Sax – One short motif, sing it, leave it hanging, finish it
# F (65), Ab (67), F (65), Bb (62) – a simple, melodic idea
sax_notes = [65, 67, 65, 62]
for i, pitch in enumerate(sax_notes):
    time = i * time_per_beat + time_per_bar
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Save the MIDI file
pm.write('4_bar_intro_Fm.mid')

print("MIDI file '4_bar_intro_Fm.mid' has been generated.")
