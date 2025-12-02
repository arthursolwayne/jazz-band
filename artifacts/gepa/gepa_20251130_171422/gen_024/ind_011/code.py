
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time per bar (160 BPM = 60/160 = 0.375 seconds per beat, 1.5 seconds per bar)
BAR_DURATION = 1.5
NOTE_DURATION = 0.375  # quarter note in 160 BPM

# Create instruments
drums = Instrument(program=Program(0), is_drum=True, name='Drums')
bass = Instrument(program=Program(33), name='Bass')
piano = Instrument(program=Program(0), name='Piano')
sax = Instrument(program=Program(64), name='Saxophone')

pm.instruments = [drums, bass, piano, sax]

# --- BAR 1: Drums only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * NOTE_DURATION
    if beat % 2 == 0:  # Kick on 1 and 3
        note = Note(36, time, duration=NOTE_DURATION)
        drums.notes.append(note)
    else:  # Snare on 2 and 4
        note = Note(38, time, duration=NOTE_DURATION)
        drums.notes.append(note)
    # Hi-hat on every eighth
    for eighth in [0, 0.5]:
        note = Note(42, time + eighth, duration=0.125)
        drums.notes.append(note)

# --- BAR 2: Full Ensemble ---
# Time: 1.5 seconds
time = BAR_DURATION

# Bass: Walking line in Fm (F, G#, Bb, C, Eb, F, G#, Bb, etc.)
bass_notes = [45, 47, 44, 46, 41, 45, 47, 44]  # F, G#, Bb, C, Eb, F, G#, Bb
for note_num, duration in zip(bass_notes, [NOTE_DURATION] * len(bass_notes)):
    note = Note(note_num, time, duration=NOTE_DURATION)
    bass.notes.append(note)
    time += NOTE_DURATION

# Piano: 7th chords on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Gm7 = G, Bb, D, F
# Amaj7 = A, C#, E, G#

time = BAR_DURATION
chords = [
    (45, 47, 46, 44),  # Fm7 (F, Ab, C, Eb)
    (44, 46, 45, 47),  # Bb7 (Bb, D, F, Ab)
    (47, 44, 46, 45),  # Gm7 (G, Bb, D, F)
    (45, 47, 46, 44)   # Fm7 again
]

for i, (root, seventh, third, fifth) in enumerate(chords):
    chord_time = BAR_DURATION + i * NOTE_DURATION
    if i % 2 == 1:  # comp on 2 and 4
        for note_num in [root, seventh, third, fifth]:
            note = Note(note_num, chord_time, duration=NOTE_DURATION)
            piano.notes.append(note)

# Sax: Melodic motif (F, G#, Bb, rest), then resolve later
sax_notes = [
    (45, BAR_DURATION, NOTE_DURATION),  # F
    (47, BAR_DURATION + NOTE_DURATION, NOTE_DURATION),  # G#
    (44, BAR_DURATION + 2 * NOTE_DURATION, NOTE_DURATION),  # Bb
    (45, BAR_DURATION + 3 * NOTE_DURATION, 0.5),  # F (shorter note to hang)
    (47, BAR_DURATION + 3.5 * NOTE_DURATION, 0.5),  # G#
    (44, BAR_DURATION + 4 * NOTE_DURATION, 0.5),  # Bb
]

for note_num, start, duration in sax_notes:
    note = Note(note_num, start, duration=duration)
    sax.notes.append(note)

# --- BAR 3 and 4: Drums continue, Bass and Piano continue, Sax resolves and breathes ---
# Drums (already added in bar 1, continuing pattern)
# Bass walking line continued (we already added 8 notes in bar 2)
# Piano: add a rest on 1, then comp again on 3
piano.notes.append(Note(0, BAR_DURATION * 2, duration=NOTE_DURATION))  # rest on 1

# Sax: resolve and end with a short, open note
note = Note(46, BAR_DURATION * 2 + 0.25, duration=0.25)  # C (resolution)
sax.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
