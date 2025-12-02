
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3 (0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=bar1_start, end=bar1_start + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=bar1_start + 0.75, end=bar1_start + 0.85))

# Snare on 2 and 4 (0.375 and 1.125s)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=SNARE, start=bar1_start + 0.375, end=bar1_start + 0.475))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=SNARE, start=bar1_start + 1.125, end=bar1_start + 1.225))

# Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125)
for i in range(0, 4):
    start = bar1_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=HIHAT, start=start, end=start + 0.1))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# SAX: Motif - D (D4), F# (F#4), A (A4), B (B4) - short, ascending, then leave it hanging
note_lengths = [0.25, 0.25, 0.25, 0.25]  # quarter notes
start = 1.5

# D4 (D), F# (F#4), A (A4), B (B4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + note_lengths[0]))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + note_lengths[0], end=start + note_lengths[0] + note_lengths[1]))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=start + note_lengths[0] + note_lengths[1], end=start + note_lengths[0] + note_lengths[1] + note_lengths[2]))

# Leave the B hanging
# sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start + note_lengths[0] + note_lengths[1] + note_lengths[2], end=start + note_lengths[0] + note_lengths[1] + note_lengths[2] + 0.5))

# Marcus: Walking bass line in D minor (D, C, B, A) - chromatic approaches
bass_notes = [62, 60, 59, 60]  # D, C, B, A
for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start + i * 0.5, end=start + i * 0.5 + 0.5))

# Diane: 7th chords on 2 and 4
# Bar 2: D7 (D, F#, A, C) - comp on beat 2 and 4
piano_notes = [62, 66, 69, 60]  # D7
for i in range(0, 4):
    if i == 1 or i == 3:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=piano_notes[i], start=start + i * 0.5, end=start + i * 0.5 + 0.5))

# Bar 3 (3.0 - 4.5s)
# SAX: Repeat motif, but finish it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=start + 2.0, end=start + 2.0 + 0.25))

# Marcus: Walking bass line - chromatic approaches again
bass_notes = [60, 59, 60, 62]  # C, B, C, D
for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start + 1.5 + i * 0.5, end=start + 1.5 + i * 0.5 + 0.5))

# Diane: 7th chords on 2 and 4
piano_notes = [62, 66, 69, 60]  # D7 again
for i in range(0, 4):
    if i == 1 or i == 3:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=piano_notes[i], start=start + 1.5 + i * 0.5, end=start + 1.5 + i * 0.5 + 0.5))

# Bar 4 (4.5 - 6.0s)
# SAX: Motif again, but with variation - maybe a half-step down
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=start + 3.0, end=start + 3.0 + 0.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=start + 3.0 + 0.25, end=start + 3.0 + 0.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=start + 3.0 + 0.5, end=start + 3.0 + 0.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=start + 3.0 + 0.75, end=start + 3.0 + 1.0))

# Marcus: Walking bass line - chromatic approach again
bass_notes = [62, 60, 59, 60]  # D, C, B, A
for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start + 3.0 + i * 0.5, end=start + 3.0 + i * 0.5 + 0.5))

# Diane: 7th chords on 2 and 4
piano_notes = [62, 66, 69, 60]  # D7
for i in range(0, 4):
    if i == 1 or i == 3:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=piano_notes[i], start=start + 3.0 + i * 0.5, end=start + 3.0 + i * 0.5 + 0.5))

# Drums for bars 2-4
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=bar_start, end=bar_start + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=bar_start + 0.75, end=bar_start + 0.85))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=SNARE, start=bar_start + 0.375, end=bar_start + 0.475))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=SNARE, start=bar_start + 1.125, end=bar_start + 1.225))
    # Hi-hat on every eighth
    for i in range(0, 4):
        start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=HIHAT, start=start, end=start + 0.1))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
