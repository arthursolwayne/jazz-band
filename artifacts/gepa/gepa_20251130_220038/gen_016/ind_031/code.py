
import pretty_midi

# Create the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define drum notes
kick = 36  # Kick drum on beat 1 and 3
snare = 38  # Snare on beat 2 and 4
hihat = 42  # Hi-hat on every eighth note

# Bar 1: Little Ray (drums only) - 0.0s to 1.5s
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Define the time for each bar (6 seconds total, 1.5s per bar)
bar_length = 1.5
note_duration = bar_length / 16  # 16 notes per bar at 160 BPM

# Fill the drum pattern for bar 1
for i in range(16):
    time = i * note_duration
    if i % 8 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + note_duration)
        drums.notes.append(note)
    if i % 8 == 4:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + note_duration)
        drums.notes.append(note)
    if i % 8 == 2:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + note_duration)
        drums.notes.append(note)
    if i % 8 == 6:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + note_duration)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + note_duration)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5s to 6.0s)

# BASS LINE: Marcus (walking line in Fm)
# Fm: F, Ab, Bb, C, Eb, F, G, Ab
# Walking line in 4/4: 1 & 2 & 3 & 4 &

# Melody: Dante (Tenor Sax) — short motif, start it, leave it hanging, come back
# Motif: F, Ab, Bb, C (start), then rest on the 2nd and 3rd bar, then resolve on the 4th bar

# Piano: Diane — 7th chords, comp on 2 and 4

def play_piano_on_beat(note, time):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + note_duration)
    piano.notes.append(note)

# Bar 2: 1.5s to 3.0s
# Bass
bass_notes = [77, 75, 74, 72]  # F, Eb, D, C
for i, pitch in enumerate(bass_notes):
    time = 1.5 + i * note_duration
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + note_duration)
    bass.notes.append(note)

# Piano — 7th chords on 2 and 4 (Ab7 on 2, Cm7 on 4)
play_piano_on_beat(83, 1.5 + 2 * note_duration)  # Ab7 (Ab, C, Eb, G)
play_piano_on_beat(72, 1.5 + 4 * note_duration)  # Cm7 (C, Eb, G, Bb)

# Sax — Start the motif
note = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.5 + note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=75, start=1.5 + note_duration, end=1.5 + 2 * note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 2 * note_duration, end=1.5 + 3 * note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 3 * note_duration, end=1.5 + 4 * note_duration)
sax.notes.append(note)

# Bar 3: 3.0s to 4.5s
# Bass
bass_notes = [71, 69, 68, 66]  # Bb, G, F, Eb (walking line)
for i, pitch in enumerate(bass_notes):
    time = 3.0 + i * note_duration
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + note_duration)
    bass.notes.append(note)

# Piano — 7th chords on 2 and 4 (Bb7 on 2, Eb7 on 4)
play_piano_on_beat(71, 3.0 + 2 * note_duration)  # Bb7 (Bb, D, F, Ab)
play_piano_on_beat(64, 3.0 + 4 * note_duration)  # Eb7 (Eb, G, Bb, D)

# Sax — Rest
# No notes in Bar 3 (wait for resolution)

# Bar 4: 4.5s to 6.0s
# Bass
bass_notes = [65, 64, 66, 68]  # Ab, G, Ab, Bb (resolve to Fm)
for i, pitch in enumerate(bass_notes):
    time = 4.5 + i * note_duration
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + note_duration)
    bass.notes.append(note)

# Piano — 7th chords on 2 and 4 (Fm7 on 2, Cm7 on 4)
play_piano_on_beat(64, 4.5 + 2 * note_duration)  # Fm7 (F, Ab, C, Eb)
play_piano_on_beat(72, 4.5 + 4 * note_duration)  # Cm7 (C, Eb, G, Bb)

# Sax — Return to resolve the motif
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.5 + note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=75, start=4.5 + note_duration, end=4.5 + 2 * note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5 + 2 * note_duration, end=4.5 + 3 * note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=4.5 + 3 * note_duration, end=4.5 + 4 * note_duration)
sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
