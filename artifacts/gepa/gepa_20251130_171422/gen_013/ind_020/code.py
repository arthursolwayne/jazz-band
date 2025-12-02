
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Acoustic Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Bar 1 (0.0 - 1.5s): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick_notes = [bar1_start, bar1_start + 0.75]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.25)
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [bar1_start + 0.5, bar1_start + 1.25]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.25)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_notes = [bar1_start + i * 0.375 for i in range(4)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2 (1.5 - 3.0s): Sax, Bass, Piano enter
# Dante's melody: F - G - Bb (with space), then repeat on 2nd bar
bar2_start = 1.5
bar2_end = 3.0

# Saxophone: F, G, Bb (F6, G6, Bb6) with slight space between
note1 = pretty_midi.Note(velocity=100, pitch=84, start=bar2_start, end=bar2_start + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=87, start=bar2_start + 0.5, end=bar2_start + 0.875)
note3 = pretty_midi.Note(velocity=100, pitch=81, start=bar2_start + 1.0, end=bar2_start + 1.375)

sax.notes.extend([note1, note2, note3])

# Bass: Chromatic walking line, F - E - D - C - Bb (F3, E3, D3, C3, Bb3)
bass_notes = [
    (bar2_start, 78),  # F3
    (bar2_start + 0.375, 76),  # E3
    (bar2_start + 0.75, 74),  # D3
    (bar2_start + 1.125, 72),  # C3
    (bar2_start + 1.5, 70),  # Bb3
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comping on the offbeats
# F7: F, A, C, E (F4, A4, C5, E4)
# Play on the offbeats (2 and 4) with some tension
chord1 = [65, 68, 72, 69]  # F7
chord2 = [65, 68, 72, 67]  # F7 altered or Fmi7b5 (Bb in root position)

# Bar 2, beat 2 (offbeat)
note_start = bar2_start + 0.5
for pitch in chord1:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.25)
    piano.notes.append(note)

# Bar 2, beat 4 (offbeat)
note_start = bar2_start + 1.25
for pitch in chord2:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.25)
    piano.notes.append(note)

# Bar 3 (3.0 - 4.5s): Repeat sax melody with variation
# Repeat the F-G-Bb motif, but with a slight syncopation
bar3_start = 3.0
bar3_end = 4.5

note1 = pretty_midi.Note(velocity=100, pitch=84, start=bar3_start + 0.25, end=bar3_start + 0.625)
note2 = pretty_midi.Note(velocity=100, pitch=87, start=bar3_start + 0.75, end=bar3_start + 1.125)
note3 = pretty_midi.Note(velocity=100, pitch=81, start=bar3_start + 1.375, end=bar3_start + 1.75)

sax.notes.extend([note1, note2, note3])

# Bass: Chromatic again
bar3_notes = [
    (bar3_start, 78),  # F3
    (bar3_start + 0.375, 76),  # E3
    (bar3_start + 0.75, 74),  # D3
    (bar3_start + 1.125, 72),  # C3
    (bar3_start + 1.5, 70),  # Bb3
]
for time, pitch in bar3_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: Another 7th chord variation
# Bar 3, beat 2
note_start = bar3_start + 0.5
for pitch in chord2:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.25)
    piano.notes.append(note)

# Bar 3, beat 4
note_start = bar3_start + 1.25
for pitch in chord1:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.25)
    piano.notes.append(note)

# Bar 4 (4.5 - 6.0s): Repeat sax melody with resolution
bar4_start = 4.5
bar4_end = 6.0

note1 = pretty_midi.Note(velocity=100, pitch=84, start=bar4_start, end=bar4_start + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=87, start=bar4_start + 0.5, end=bar4_start + 0.875)
note3 = pretty_midi.Note(velocity=100, pitch=81, start=bar4_start + 1.0, end=bar4_start + 1.375)

sax.notes.extend([note1, note2, note3])

# Bass: Chromatic again
bar4_notes = [
    (bar4_start, 78),  # F3
    (bar4_start + 0.375, 76),  # E3
    (bar4_start + 0.75, 74),  # D3
    (bar4_start + 1.125, 72),  # C3
    (bar4_start + 1.5, 70),  # Bb3
]
for time, pitch in bar4_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: Final chord on beat 4
note_start = bar4_start + 1.25
for pitch in chord1:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.25)
    piano.notes.append(note)

# Drums in Bar 3 and 4: repeat the same pattern
# Bar 3
bar3_start = 3.0
bar3_end = 4.5

# Kick on 1 and 3
kick_notes = [bar3_start, bar3_start + 0.75]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.25)
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [bar3_start + 0.5, bar3_start + 1.25]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.25)
    drums.notes.append(note)

# Hihat on every eighth
hihat_notes = [bar3_start + i * 0.375 for i in range(4)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 4
bar4_start = 4.5
bar4_end = 6.0

# Kick on 1 and 3
kick_notes = [bar4_start, bar4_start + 0.75]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.25)
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [bar4_start + 0.5, bar4_start + 1.25]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.25)
    drums.notes.append(note)

# Hihat on every eighth
hihat_notes = [bar4_start + i * 0.375 for i in range(4)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.125)
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
