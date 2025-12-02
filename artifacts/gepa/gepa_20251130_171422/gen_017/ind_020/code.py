
import pretty_midi

# Initialize a MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# -------------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray sets the mood, tight and precise
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 60 BPM = 1 beat = 0.375 seconds, 1 bar = 1.5 seconds
# 1 bar = 4 beats = 16 eighth notes

bar1_start = 0.0
bar1_end = 1.5

# Create hihat on every eighth note
for i in range(16):
    time = bar1_start + i * 0.375
    note = pretty_midi.Note(velocity=64, pitch=hihat, start=time, end=time + 0.125)
    drums.notes.append(note)

# Kick on 1 and 3 (beats 1 and 3)
for i in [0, 2]:
    time = bar1_start + i * 0.75
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
    drums.notes.append(note)

# Snare on 2 and 4
for i in [1, 3]:
    time = bar1_start + i * 0.75
    note = pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125)
    drums.notes.append(note)

# -------------------
# Bar 2: Full Quartet (1.5 - 3.0s)
# Sax plays a simple, emotional motif — Fm7 -> Bb -> Eb -> Ab

bar2_start = 1.5
bar2_end = 3.0

# Sax: Tenor motif (Fm7 -> Bb -> Eb -> Ab)
# Fm7: F, Ab, C, Db
# Bb: Bb
# Eb: Eb
# Ab: Ab
# But we make it sing — a short, 3-note phrase that lingers

note1 = pretty_midi.Note(velocity=100, pitch=84, start=bar2_start, end=bar2_start + 0.4)
note2 = pretty_midi.Note(velocity=100, pitch=80, start=bar2_start + 0.4, end=bar2_start + 0.8)
note3 = pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 0.8, end=bar2_start + 1.2)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.2, end=bar2_start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Chromatic walking line (F, Gb, G, Ab, A, Bb, B, C)
# 8 notes over 1.5 seconds (0.1875 per note)

bass_notes = [77, 76, 78, 79, 80, 78, 80, 81]
for i, pitch in enumerate(bass_notes):
    start = bar2_start + i * 0.1875
    end = start + 0.1875
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords, comp on offbeats — F7, Bb7, Eb7, Ab7
# Dorian mode, angry but supportive

# F7 (F, A, C, Eb)
note1 = pretty_midi.Note(velocity=90, pitch=84, start=bar2_start + 0.25, end=bar2_start + 0.5)
note2 = pretty_midi.Note(velocity=90, pitch=87, start=bar2_start + 0.25, end=bar2_start + 0.5)
note3 = pretty_midi.Note(velocity=90, pitch=89, start=bar2_start + 0.25, end=bar2_start + 0.5)
note4 = pretty_midi.Note(velocity=90, pitch=83, start=bar2_start + 0.25, end=bar2_start + 0.5)
piano.notes.extend([note1, note2, note3, note4])

# Bb7 (Bb, D, F, Ab)
note1 = pretty_midi.Note(velocity=90, pitch=80, start=bar2_start + 0.75, end=bar2_start + 1.0)
note2 = pretty_midi.Note(velocity=90, pitch=83, start=bar2_start + 0.75, end=bar2_start + 1.0)
note3 = pretty_midi.Note(velocity=90, pitch=84, start=bar2_start + 0.75, end=bar2_start + 1.0)
note4 = pretty_midi.Note(velocity=90, pitch=79, start=bar2_start + 0.75, end=bar2_start + 1.0)
piano.notes.extend([note1, note2, note3, note4])

# Eb7 (Eb, G, Bb, Db)
note1 = pretty_midi.Note(velocity=90, pitch=76, start=bar2_start + 1.25, end=bar2_start + 1.5)
note2 = pretty_midi.Note(velocity=90, pitch=79, start=bar2_start + 1.25, end=bar2_start + 1.5)
note3 = pretty_midi.Note(velocity=90, pitch=80, start=bar2_start + 1.25, end=bar2_start + 1.5)
note4 = pretty_midi.Note(velocity=90, pitch=74, start=bar2_start + 1.25, end=bar2_start + 1.5)
piano.notes.extend([note1, note2, note3, note4])

# -------------------
# Bar 3: Repeat of Bar 2, with sax playing the same motif again
# No need for new content — let it breathe

bar3_start = 3.0
bar3_end = 4.5

note1 = pretty_midi.Note(velocity=100, pitch=84, start=bar3_start, end=bar3_start + 0.4)
note2 = pretty_midi.Note(velocity=100, pitch=80, start=bar3_start + 0.4, end=bar3_start + 0.8)
note3 = pretty_midi.Note(velocity=100, pitch=76, start=bar3_start + 0.8, end=bar3_start + 1.2)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 1.2, end=bar3_start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Same chromatic line, transposed to start at bar3
bass_notes = [77, 76, 78, 79, 80, 78, 80, 81]
for i, pitch in enumerate(bass_notes):
    start = bar3_start + i * 0.1875
    end = start + 0.1875
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Same chords, transposed to bar3
note1 = pretty_midi.Note(velocity=90, pitch=84, start=bar3_start + 0.25, end=bar3_start + 0.5)
note2 = pretty_midi.Note(velocity=90, pitch=87, start=bar3_start + 0.25, end=bar3_start + 0.5)
note3 = pretty_midi.Note(velocity=90, pitch=89, start=bar3_start + 0.25, end=bar3_start + 0.5)
note4 = pretty_midi.Note(velocity=90, pitch=83, start=bar3_start + 0.25, end=bar3_start + 0.5)
piano.notes.extend([note1, note2, note3, note4])

note1 = pretty_midi.Note(velocity=90, pitch=80, start=bar3_start + 0.75, end=bar3_start + 1.0)
note2 = pretty_midi.Note(velocity=90, pitch=83, start=bar3_start + 0.75, end=bar3_start + 1.0)
note3 = pretty_midi.Note(velocity=90, pitch=84, start=bar3_start + 0.75, end=bar3_start + 1.0)
note4 = pretty_midi.Note(velocity=90, pitch=79, start=bar3_start + 0.75, end=bar3_start + 1.0)
piano.notes.extend([note1, note2, note3, note4])

note1 = pretty_midi.Note(velocity=90, pitch=76, start=bar3_start + 1.25, end=bar3_start + 1.5)
note2 = pretty_midi.Note(velocity=90, pitch=79, start=bar3_start + 1.25, end=bar3_start + 1.5)
note3 = pretty_midi.Note(velocity=90, pitch=80, start=bar3_start + 1.25, end=bar3_start + 1.5)
note4 = pretty_midi.Note(velocity=90, pitch=74, start=bar3_start + 1.25, end=bar3_start + 1.5)
piano.notes.extend([note1, note2, note3, note4])

# -------------------
# Bar 4: Repeat of Bar 2 and 3, but sax finishes the motif
# Important: end on a strong note, not open

bar4_start = 4.5
bar4_end = 6.0

note1 = pretty_midi.Note(velocity=100, pitch=84, start=bar4_start, end=bar4_start + 0.4)
note2 = pretty_midi.Note(velocity=100, pitch=80, start=bar4_start + 0.4, end=bar4_start + 0.8)
note3 = pretty_midi.Note(velocity=100, pitch=76, start=bar4_start + 0.8, end=bar4_start + 1.2)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.2, end=bar4_start + 1.5)
sax.notes.extend([note1, note2, note3, note4])

# Bass: Same chromatic line, transposed to bar4
bass_notes = [77, 76, 78, 79, 80, 78, 80, 81]
for i, pitch in enumerate(bass_notes):
    start = bar4_start + i * 0.1875
    end = start + 0.1875
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Same chords, transposed to bar4
note1 = pretty_midi.Note(velocity=90, pitch=84, start=bar4_start + 0.25, end=bar4_start + 0.5)
note2 = pretty_midi.Note(velocity=90, pitch=87, start=bar4_start + 0.25, end=bar4_start + 0.5)
note3 = pretty_midi.Note(velocity=90, pitch=89, start=bar4_start + 0.25, end=bar4_start + 0.5)
note4 = pretty_midi.Note(velocity=90, pitch=83, start=bar4_start + 0.25, end=bar4_start + 0.5)
piano.notes.extend([note1, note2, note3, note4])

note1 = pretty_midi.Note(velocity=90, pitch=80, start=bar4_start + 0.75, end=bar4_start + 1.0)
note2 = pretty_midi.Note(velocity=90, pitch=83, start=bar4_start + 0.75, end=bar4_start + 1.0)
note3 = pretty_midi.Note(velocity=90, pitch=84, start=bar4_start + 0.75, end=bar4_start + 1.0)
note4 = pretty_midi.Note(velocity=90, pitch=79, start=bar4_start + 0.75, end=bar4_start + 1.0)
piano.notes.extend([note1, note2, note3, note4])

note1 = pretty_midi.Note(velocity=90, pitch=76, start=bar4_start + 1.25, end=bar4_start + 1.5)
note2 = pretty_midi.Note(velocity=90, pitch=79, start=bar4_start + 1.25, end=bar4_start + 1.5)
note3 = pretty_midi.Note(velocity=90, pitch=80, start=bar4_start + 1.25, end=bar4_start + 1.5)
note4 = pretty_midi.Note(velocity=90, pitch=74, start=bar4_start + 1.25, end=bar4_start + 1.5)
piano.notes.extend([note1, note2, note3, note4])

# -------------------
# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
