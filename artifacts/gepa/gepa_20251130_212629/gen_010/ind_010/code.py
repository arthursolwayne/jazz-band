
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hi_hat = 42

# Duration of one bar in seconds (160 BPM, 4/4 time)
bar_duration = 1.5  # 60 / 160 * 4 = 1.5

# Bar 1: Little Ray alone (Drums only)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=bar_1_start, end=bar_1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=bar_1_start + 0.75, end=bar_1_start + 1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=bar_1_start + 0.375, end=bar_1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=bar_1_start + 1.125, end=bar_1_start + 1.5))

# Hi-hat on every eighth
for i in range(8):
    start = bar_1_start + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=hi_hat, start=start, end=end))

# Bar 2: Full ensemble starts
bar_2_start = bar_duration

# BASS: Walking line in F minor, chromatic approach to Bb
# F - Gb - G - A - Bb - B - C - Db
# Each quarter note
notes = [77, 76, 78, 80, 79, 81, 83, 82]  # F, Gb, G, A, Bb, B, C, Db
for i, note in enumerate(notes):
    start = bar_2_start + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# PIANO: 7th chords on 2 and 4, comping
# Bar 2: F7 on 2 and 4
f7 = [77, 80, 82, 84]  # F, A, C, Eb
for i, note in enumerate(f7):
    start = bar_2_start + (0.375 * 2)  # On beat 2
    end = start + 0.375
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

    start = bar_2_start + (0.375 * 4)  # On beat 4
    end = start + 0.375
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# SAX: Motif (start on beat 1)
# F - G - Bb - Ab - G - F (6 notes)
# Haunting, minor, with tension
sax_notes = [77, 78, 79, 76, 78, 77]
sax_durations = [0.375, 0.375, 0.375, 0.375, 0.375, 0.375]
for i, note in enumerate(sax_notes):
    start = bar_2_start + i * sax_durations[i]
    end = start + sax_durations[i]
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 3: Full ensemble
bar_3_start = bar_2_start + bar_duration

# BASS: Walking line again
notes = [77, 76, 78, 80, 79, 81, 83, 82]
for i, note in enumerate(notes):
    start = bar_3_start + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# PIANO: G7 on 2 and 4
g7 = [79, 81, 83, 85]  # G, B, D, F
for i, note in enumerate(g7):
    start = bar_3_start + (0.375 * 2)
    end = start + 0.375
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

    start = bar_3_start + (0.375 * 4)
    end = start + 0.375
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# SAX: Motif again, starting on beat 1
sax_notes = [77, 78, 79, 76, 78, 77]
for i, note in enumerate(sax_notes):
    start = bar_3_start + i * sax_durations[i]
    end = start + sax_durations[i]
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 4: Full ensemble
bar_4_start = bar_3_start + bar_duration

# BASS: Walking line again
notes = [77, 76, 78, 80, 79, 81, 83, 82]
for i, note in enumerate(notes):
    start = bar_4_start + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# PIANO: Cm7 on 2 and 4
cm7 = [83, 85, 87, 80]  # C, Eb, G, Bb
for i, note in enumerate(cm7):
    start = bar_4_start + (0.375 * 2)
    end = start + 0.375
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

    start = bar_4_start + (0.375 * 4)
    end = start + 0.375
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# SAX: Motif again, starting on beat 1
sax_notes = [77, 78, 79, 76, 78, 77]
for i, note in enumerate(sax_notes):
    start = bar_4_start + i * sax_durations[i]
    end = start + sax_durations[i]
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
