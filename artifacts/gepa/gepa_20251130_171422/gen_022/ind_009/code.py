
import pretty_midi

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature to F minor
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F minor is key number 5

# Define note durations (in seconds)
beat = 0.375  # 160 BPM = 60 / 160 = 0.375 sec per beat
bar = 1.5  # 4 beats per bar

# ---------------------------- DRUMS ----------------------------
drum_program = pretty_midi.Instrument(program=128)
pm.instruments.append(drum_program)

# Bar 1: Drums alone
# Kick on 1 and 3
kick_notes = [36, 36]  # MIDI note for kick
kick_times = [0.0, beat*2]  # at beat 0 and 2 (1 & 3)
for note, time in zip(kick_notes, kick_times):
    drum_program.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Snare on 2 and 4 (first bar only)
snare_notes = [38, 38]  # MIDI note for snare
snare_times = [beat, beat*3]
for note, time in zip(snare_notes, snare_times):
    drum_program.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.1))

# Hi-hat on every eighth note
hihat_notes = [42] * 8
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]
for note, time in zip(hihat_notes, hihat_times):
    drum_program.notes.append(pretty_midi.Note(velocity=60, pitch=note, start=time, end=time + 0.05))

# Bar 2: Drums continue with more energy
# Kick on 1 and 3
kick_notes = [36, 36]
kick_times = [bar, bar + beat*2]
for note, time in zip(kick_notes, kick_times):
    drum_program.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Snare on 2 and 4
snare_notes = [38, 38]
snare_times = [bar + beat, bar + beat*3]
for note, time in zip(snare_notes, snare_times):
    drum_program.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))

# Hi-hat with some space
hihat_notes = [42] * 8
hihat_times = [bar, bar + 0.1875, bar + 0.375, bar + 0.5625, bar + 0.75, bar + 0.9375, bar + 1.125, bar + 1.3125]
for note, time in zip(hihat_notes, hihat_times):
    drum_program.notes.append(pretty_midi.Note(velocity=65, pitch=note, start=time, end=time + 0.05))

# ---------------------------- BASS ----------------------------
bass_program = pretty_midi.Instrument(program=33)  # Acoustic Bass
pm.instruments.append(bass_program)

# Bar 1: Walking line with chromatic approaches
bass_notes = [59, 60, 61, 59, 60, 61, 60, 59]  # F natural, Gb, G, F, Gb, G, Gb, F
bass_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for note, time in zip(bass_notes, bass_times):
    bass_program.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Bar 2: Chromatic line in Fm
bass_notes = [59, 60, 61, 59, 60, 58, 59, 58]
bass_times = [bar, bar + 0.375, bar + 0.75, bar + 1.125, bar + 1.5, bar + 1.875, bar + 2.25, bar + 2.625]
for note, time in zip(bass_notes, bass_times):
    bass_program.notes.append(pretty_midi.Note(velocity=82, pitch=note, start=time, end=time + 0.25))

# Bar 3: More tension
bass_notes = [59, 60, 61, 59, 60, 58, 60, 59]
bass_times = [bar*2, bar*2 + 0.375, bar*2 + 0.75, bar*2 + 1.125, bar*2 + 1.5, bar*2 + 1.875, bar*2 + 2.25, bar*2 + 2.625]
for note, time in zip(bass_notes, bass_times):
    bass_program.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Bar 4: Resolving tension
bass_notes = [60, 61, 59, 60, 58, 59, 58, 59]
bass_times = [bar*3, bar*3 + 0.375, bar*3 + 0.75, bar*3 + 1.125, bar*3 + 1.5, bar*3 + 1.875, bar*3 + 2.25, bar*3 + 2.625]
for note, time in zip(bass_notes, bass_times):
    bass_program.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# ---------------------------- PIANO ----------------------------
piano_program = pretty_midi.Instrument(program=0)  # Acoustic Piano
pm.instruments.append(piano_program)

# Bar 1: Rest
# Bar 2: Comp on 2 & 4
# F7 (F A C Eb) = [59, 64, 60, 62]
comp_notes = [59, 64, 60, 62]
comp_times = [bar + beat, bar + beat*3]
for note, time in zip(comp_notes, comp_times):
    piano_program.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 3: Comp on 2 & 4
comp_notes = [59, 62, 60, 62]  # F7 altered
comp_times = [bar*2 + beat, bar*2 + beat*3]
for note, time in zip(comp_notes, comp_times):
    piano_program.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Bar 4: Comp on 2 & 4
comp_notes = [59, 62, 60, 62]  # F7
comp_times = [bar*3 + beat, bar*3 + beat*3]
for note, time in zip(comp_notes, comp_times):
    piano_program.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# ---------------------------- SAX (Tenor) ----------------------------
sax_program = pretty_midi.Instrument(program=64)  # Tenor Sax
pm.instruments.append(sax_program)

# Bar 2: Motif starts
# F - Gb - F - Gb - E - D - C - Bb
# Notes in MIDI: 59, 60, 59, 60, 57, 55, 52, 50
# Timing: bar + 0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625
sax_notes = [59, 60, 59, 60, 57, 55, 52, 50]
sax_times = [bar, bar + 0.375, bar + 0.75, bar + 1.125, bar + 1.5, bar + 1.875, bar + 2.25, bar + 2.625]
for note, time in zip(sax_notes, sax_times):
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Repeat the motif with slight variation
# F - Gb - F - Gb - D - C - Bb - B
# Notes: 59, 60, 59, 60, 55, 52, 50, 51
sax_notes = [59, 60, 59, 60, 55, 52, 50, 51]
sax_times = [bar*2, bar*2 + 0.375, bar*2 + 0.75, bar*2 + 1.125, bar*2 + 1.5, bar*2 + 1.875, bar*2 + 2.25, bar*2 + 2.625]
for note, time in zip(sax_notes, sax_times):
    sax_program.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Bar 4: Motif ends with a question
# F - Gb - E - D
sax_notes = [59, 60, 57, 55]
sax_times = [bar*3, bar*3 + 0.375, bar*3 + 0.75, bar*3 + 1.125]
for note, time in zip(sax_notes, sax_times):
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Save the MIDI file
pm.write("Cellar_4_bar_intro.mid")
