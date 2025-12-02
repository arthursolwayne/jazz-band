
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray (drums) alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0
bar_1_end = 1.5

# Kick on beat 1 and 3
kick_times = [bar_1_start + 0.0, bar_1_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on beat 2 and 4
snare_times = [bar_1_start + 0.375, bar_1_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hi-hat on every eighth note
hihat_times = [bar_1_start + t * 0.375 for t in range(8)]
for time in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet comes in (1.5 - 3.0s)
bar_2_start = 1.5
bar_2_end = 3.0

# Bass line: Marcus playing walking line in F
# F7 chord: F, A, C, E
# Walking line in F: F, G#, A, Bb, B, C#, D, Eb
bass_notes = [77, 79, 80, 79, 81, 83, 84, 82]  # F, G#, A, G#, B, C#, D, Eb
bass_times = [bar_2_start + t * 0.375 for t in range(8)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Piano: Diane plays 7th chords on 2 and 4
# F7: F, A, C, E
# F7 = 77, 80, 79, 82
piano_notes = [77, 80, 79, 82]
piano_times = [bar_2_start + 0.375, bar_2_start + 1.125]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Sax: Dante's motif — one short phrase, singable, leaving it hanging
# F, G#, A, Bb (F7 arpeggio, ascending)
sax_notes = [77, 79, 80, 79]
sax_times = [bar_2_start + 0.0, bar_2_start + 0.375, bar_2_start + 0.75, bar_2_start + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Bar 3: Full quartet continues (3.0 - 4.5s)
bar_3_start = 3.0
bar_3_end = 4.5

# Bass continues walking
bass_notes = [77, 79, 80, 79, 81, 83, 84, 82]
bass_times = [bar_3_start + t * 0.375 for t in range(8)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Piano: Diane plays 7th chords again
piano_notes = [77, 80, 79, 82]
piano_times = [bar_3_start + 0.375, bar_3_start + 1.125]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Drums continue kick, snare, hihat
kick_times = [bar_3_start + 0.0, bar_3_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times = [bar_3_start + 0.375, bar_3_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times = [bar_3_start + t * 0.375 for t in range(8)]
for time in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar_4_start = 4.5
bar_4_end = 6.0

# Bass continues walking
bass_notes = [77, 79, 80, 79, 81, 83, 84, 82]
bass_times = [bar_4_start + t * 0.375 for t in range(8)]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Piano: Diane plays 7th chords again
piano_notes = [77, 80, 79, 82]
piano_times = [bar_4_start + 0.375, bar_4_start + 1.125]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Drums continue kick, snare, hihat
kick_times = [bar_4_start + 0.0, bar_4_start + 0.75]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
    drums.notes.append(note)

snare_times = [bar_4_start + 0.375, bar_4_start + 1.125]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1)
    drums.notes.append(note)

hihat_times = [bar_4_start + t * 0.375 for t in range(8)]
for time in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.1)
    drums.notes.append(note)

# Sax: Finish the motif — return to F and land on the 4th beat
sax_notes = [77, 79, 80, 77]  # F, G#, A, F
sax_times = [bar_4_start + 0.0, bar_4_start + 0.375, bar_4_start + 0.75, bar_4_start + 1.125]
for note, time in zip(sax_notes, sax_times):
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
