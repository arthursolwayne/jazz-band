
import pretty_midi
import numpy as np

# Setup the MIDI file
pm = pretty_midi.PrettyMidi()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the key: F minor (F, Gb, Ab, Bb, C, Db, Eb)
# We'll use F minor for all instruments
key = 'Fm'
root = pretty_midi.note_number_from_name('F3')  # F3 is the root note in the middle register
tempo = 160  # BPM
bar_length = 6.0  # 4 bars = 6 seconds at 160 BPM
beat_length = bar_length / 4  # 1.5 seconds per beat
beat_division = 8  # 8 notes per beat (eighth notes)
note_length = beat_length / beat_division  # 0.1875 seconds per eighth note

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# --- Drum Pattern (Bar 1 - 1 beat of kick, 1 beat of snare, hihat every 8th)
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3 (beats 0 and 2)
kick_times = [0.0, 2.0]
kick_notes = [36]  # Kick drum
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + note_length)
    drums.notes.append(note)

# Snare on 2 and 4 (beats 1 and 3)
snare_times = [1.0, 3.0]
snare_notes = [38]  # Snare drum
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + note_length)
    drums.notes.append(note)

# Hihat on every eighth note (0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625)
hihat_times = np.arange(0, 1.5, 0.375)
hihat_notes = [42]  # Hihat
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + note_length)
    drums.notes.append(note)

# --- Bass Line (Bar 1: Walking line in Fm, chromatic approaches)

# Fm scale: F, Gb, Ab, Bb, C, Db, Eb

# Bar 1 walking bass line (chromatic approach to F)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=0.0, end=0.375),  # F (C3)
    pretty_midi.Note(velocity=100, pitch=52, start=0.375, end=0.75),  # Gb (Bb3)
    pretty_midi.Note(velocity=100, pitch=50, start=0.75, end=1.125),  # Ab (Ab3)
    pretty_midi.Note(velocity=100, pitch=48, start=1.125, end=1.5),  # Bb (Bb3)
]

# Add to bass instrument
for note in bass_notes:
    bass.notes.append(note)

# --- Piano (Bars 2-4: Comping on 2 and 4, 7th chords)

# Define 7th chords for Fm: F7, Bb7, Eb7, Ab7
# Root positions with 7th
chords = {
    0: [53, 57, 59, 60],  # F7
    1: [50, 54, 56, 57],  # Bb7
    2: [47, 51, 53, 54],  # Eb7
    3: [44, 48, 50, 51],  # Ab7
}

# Bar 2: F7 (beats 2 and 4)
for i in [1, 3]:
    time = i * beat_length
    for pitch in chords[0]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_length)
        piano.notes.append(note)

# Bar 3: Bb7 (beats 2 and 4)
for i in [1, 3]:
    time = i * beat_length + bar_length
    for pitch in chords[1]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_length)
        piano.notes.append(note)

# Bar 4: Eb7 (beats 2 and 4)
for i in [1, 3]:
    time = i * beat_length + bar_length * 2
    for pitch in chords[2]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + note_length)
        piano.notes.append(note)

# --- Saxophone (Bars 2-4: Melody with tension, space, and a question)

# Melody: A motive that starts, then leaves it hanging
# Fm: F, Gb, Ab, Bb, C, Db, Eb
# Melody in Fm: F -> Ab -> Bb -> C -> (rest) -> Db -> (rest) -> Eb

# Bar 2: F -> Ab -> Bb -> C
note_1 = pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.5 + 0.2)
note_2 = pretty_midi.Note(velocity=110, pitch=50, start=1.7, end=1.7 + 0.2)
note_3 = pretty_midi.Note(velocity=110, pitch=48, start=1.9, end=1.9 + 0.2)
note_4 = pretty_midi.Note(velocity=110, pitch=50, start=2.1, end=2.1 + 0.2)

# Bar 3: Rest
# Bar 4: Db -> Rest -> Eb
note_5 = pretty_midi.Note(velocity=110, pitch=47, start=3.0, end=3.0 + 0.2)
note_6 = pretty_midi.Note(velocity=110, pitch=44, start=3.4, end=3.4 + 0.2)

# Add to sax
for note in [note_1, note_2, note_3, note_4, note_5, note_6]:
    sax.notes.append(note)

# Write the MIDI file
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' generated successfully.")
