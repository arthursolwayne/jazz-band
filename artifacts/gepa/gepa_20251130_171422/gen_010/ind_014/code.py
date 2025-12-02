
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# -----------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# 160 BPM = 1 beat = 0.375 sec, 1 bar = 1.5 sec

bar_duration = 1.5
bar_start = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar_start, end=bar_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))

# Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start, end=bar_start + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 0.375, end=bar_start + 0.375 + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 0.75, end=bar_start + 0.75 + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 1.125, end=bar_start + 1.125 + 0.1875))

# -----------------
# Bar 2-4: Full quartet (1.5 - 6.0s)
# Key: F minor (F, Gb, Ab, Bb, Cb, Db, Eb)
# All instruments join in now. Fm7, Ab, Bb, Db chords

bar_start = 1.5

# -----------------
# Drums: same pattern for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar_start, end=bar_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))

# Hihat on every 8th
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start, end=bar_start + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 0.375, end=bar_start + 0.375 + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 0.75, end=bar_start + 0.75 + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 1.125, end=bar_start + 1.125 + 0.1875))

# -----------------
# Bass line: chromatic walk, F -> Gb -> Ab -> Bb -> Cb -> Db -> Eb -> F
# 1 bar = 4 beats, 1 beat = 0.375 sec
# 1 bar duration = 1.5 sec, 4 beats = 4 notes
# Start at bar_start (1.5)

bass_notes = [77, 76, 74, 73, 72, 71, 69, 77]  # F, Gb, Ab, Bb, Cb, Db, Eb, F
note_durations = [0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375]

for i in range(len(bass_notes)):
    note_start = bar_start + i * 0.375
    note_end = note_start + note_durations[i]
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=note_start, end=note_end))

# -----------------
# Piano: 7th chords, comp on offbeats
# Fm7 = F, Ab, Bb, Db
# Ab7 = Ab, Bb, Db, Eb
# Bb7 = Bb, Db, Eb, F
# Db7 = Db, Eb, F, Gb

# Bar 2: Fm7 (beat 1), Ab7 (beat 3)
piano_notes = [
    # Bar 2
    (77, 76, 73, 71, 0.375, 0.375),  # F, Ab, Bb, Db on beat 1
    (76, 73, 71, 69, 0.375, 0.375),  # Ab, Bb, Db, Eb on beat 3
    # Bar 3
    (73, 71, 69, 76, 0.375, 0.375),  # Bb, Db, Eb, Ab on beat 1
    (71, 69, 76, 74, 0.375, 0.375),  # Db, Eb, Ab, Bb on beat 3
    # Bar 4
    (76, 74, 71, 77, 0.375, 0.375),  # Ab, Bb, Db, F on beat 1
    (74, 71, 77, 76, 0.375, 0.375)   # Bb, Db, F, Ab on beat 3
]

for i, (note1, note2, note3, note4, duration1, duration2) in enumerate(piano_notes):
    bar = i // 2
    beat = i % 2
    start = bar_start + bar * 1.5 + beat * 0.375
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note1, start=start, end=start + duration1))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note2, start=start, end=start + duration1))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note3, start=start, end=start + duration1))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note4, start=start, end=start + duration2))

# -----------------
# Sax: Motif (F, Ab, Bb, F) on beat 1 of bar 2, then repeat on beat 3 of bar 4
# Start at bar_start (1.5), beat 1 (0.0), then repeat on beat 3 of bar 4 (4.5)

motif_notes = [77, 76, 73, 77]
motif_durations = [0.375, 0.375, 0.375, 0.375]

for i, (note, duration) in enumerate(zip(motif_notes, motif_durations)):
    start = bar_start + 0.0 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Repeat the motif on beat 3 of bar 4 (4.5)
for i, (note, duration) in enumerate(zip(motif_notes, motif_durations)):
    start = bar_start + 4.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# -----------------
# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
