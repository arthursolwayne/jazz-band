
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)
instrument_list = []

# Create instruments for each player
# 1. Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
instrument_list.append(sax)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)
instrument_list.append(bass)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
instrument_list.append(piano)

# 4. Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)
instrument_list.append(drums)

# ----------------------------- BAR 1 (0.0 - 1.5s) -----------------------------
# Drums (Little Ray): hihat on every eighth, kick on 1 and 3, snare on 2 and 4
# + Space. Build tension with rhythmic clarity and space.

# Kick on 1 and 3
kick_notes = [36, 36]  # C2
kick_times = [0.0, 0.75]

# Snare on 2 and 4
snare_notes = [38, 38]  # D2
snare_times = [0.375, 1.125]

# Hihat on every eighth
hihat_notes = [42] * 8  # F#4
hihat_times = np.arange(0.0, 1.5, 0.125)

# Add to drums
for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=note, start=time, end=time + 0.05))
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))

# ----------------------------- BAR 2 (1.5 - 3.0s) -----------------------------
# You (Tenor Sax): Start the melody. One short motif, make it sing. Open-ended, searching.

# Dm7 chord: D F A C (Dm7)
# Melody in Dm: F, A, D, G (Dm scale, but with a twist)
# Bar 2: F (beat 1), A (beat 2), D (beat 3), rest (beat 4)

# Tenor sax melody
note_times = [1.5, 1.875, 2.25, 2.625]
note_pitches = [70, 74, 72, 0]  # F, A, D, rest
note_velocities = [100, 105, 110, 0]

for note, time, vel in zip(note_pitches, note_times, note_velocities):
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.125))

# Bass (Marcus): Walking line, chromatic approach to D
# Dm7 chord: D F A C
# Walking line: C (beat 1), Eb (beat 2), F (beat 3), G (beat 4)

bass_notes = [72, 64, 67, 69]  # C, Eb, F, G
bass_times = [1.5, 1.875, 2.25, 2.625]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano (Diane): 7th chords on 2 and 4 (Dm7)
# Dm7: D F A C (in root position)
# On beat 2 and 4

# Bar 2: Dm7 on beat 2 (1.875)
piano_notes = [72, 74, 76, 79]  # D, F, A, C
piano_times = [1.875, 1.875, 1.875, 1.875]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# ----------------------------- BAR 3 (3.0 - 4.5s) -----------------------------
# Tenor Sax: Continue the melody — open-ended, searching. Let it breathe.
# F (beat 1), A (beat 2), D (beat 3), rest (beat 4)

note_times = [3.0, 3.375, 3.75, 4.125]
note_pitches = [70, 74, 72, 0]  # F, A, D, rest
note_velocities = [100, 105, 110, 0]

for note, time, vel in zip(note_pitches, note_times, note_velocities):
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line, D -> C -> Eb -> F
bass_notes = [72, 64, 67, 69]
bass_times = [3.0, 3.375, 3.75, 4.125]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Dm7 on beat 4 (4.125)
piano_notes = [72, 74, 76, 79]
piano_times = [4.125, 4.125, 4.125, 4.125]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# ----------------------------- BAR 4 (4.5 - 6.0s) -----------------------------
# Tenor Sax: End the motif, leave it hanging. No scale runs — just the question.
# Dm7 chord, G (beat 1), F (beat 2), A (beat 3), rest (beat 4)

note_times = [4.5, 4.875, 5.25, 5.625]
note_pitches = [77, 70, 74, 0]  # G, F, A, rest
note_velocities = [110, 100, 105, 0]

for note, time, vel in zip(note_pitches, note_times, note_velocities):
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line, F -> G -> A -> Bb
bass_notes = [67, 69, 71, 70]  # F, G, A, Bb
bass_times = [4.5, 4.875, 5.25, 5.625]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: Dm7 on beat 4 (5.625)
piano_notes = [72, 74, 76, 79]
piano_times = [5.625, 5.625, 5.625, 5.625]
for note, time in zip(piano_notes, piano_times):
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Drums: Same rhythmic pattern as Bar 1
# Kick on 1 and 3
kick_notes = [36, 36]
kick_times = [4.5, 5.25]

# Snare on 2 and 4
snare_notes = [38, 38]
snare_times = [4.875, 5.625]

# Hihat on every eighth
hihat_times = np.arange(4.5, 6.0, 0.125)

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=note, start=time, end=time + 0.05))
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))
for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))

# Add instruments to the MIDI file
for inst in instrument_list:
    pm.instruments.append(inst)

# Save the MIDI
pm.write("dante_russo_4bar_intro.mid")
