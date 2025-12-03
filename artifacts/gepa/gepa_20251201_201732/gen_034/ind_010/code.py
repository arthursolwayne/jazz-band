
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum Note Numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time variables (4/4 at 160 BPM: 1 bar = 1.5s)
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0

# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar1_start + 0.0, end=bar1_start + 0.0 + 0.05))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar1_start + BEAT_DURATION * 2, end=bar1_start + BEAT_DURATION * 2 + 0.05))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar1_start + BEAT_DURATION, end=bar1_start + BEAT_DURATION + 0.05))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar1_start + BEAT_DURATION * 3, end=bar1_start + BEAT_DURATION * 3 + 0.05))

# Hi-hat on every eighth note
for i in range(8):
    start = bar1_start + i * BEAT_DURATION / 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=start + 0.05))

# Bar 2: Start of the quartet (1.5 - 3.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bar2_start = 1.5
for i in range(4):  # 4 beats in a bar
    beat_start = bar2_start + i * BEAT_DURATION
    # Root on beat 1, 3
    if i % 2 == 0:
        pitch = 38  # D2
    else:
        pitch = 43  # G2
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=beat_start, end=beat_start + 0.05))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Open voicing: F, A, C, E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 0.05))  # F (C4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=bar2_start, end=bar2_start + 0.05))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar2_start, end=bar2_start + 0.05))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=bar2_start, end=bar2_start + 0.05))  # E

# Bar 3: Bbmaj7 (Bb, D, F, Ab)
# Open voicing: Bb, D, F, Ab
bar3_start = 3.0
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar3_start, end=bar3_start + 0.05))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=bar3_start, end=bar3_start + 0.05))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=bar3_start, end=bar3_start + 0.05))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=75, start=bar3_start, end=bar3_start + 0.05))  # Ab

# Bar 4: D7 (D, F#, A, C)
# Open voicing: D, F#, A, C
bar4_start = 4.5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar4_start, end=bar4_start + 0.05))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar4_start, end=bar4_start + 0.05))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=bar4_start, end=bar4_start + 0.05))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar4_start, end=bar4_start + 0.05))  # C

# You: Tenor sax — the motif
# Bar 2: Start the motif (F, G, A, Bb)
# Bar 3: Leave it hanging (Bb)
# Bar 4: Return and finish it (F, G, A, Bb)

# Bar 2: F, G, A, Bb
note_lengths = [0.25, 0.25, 0.25, 0.25]  # Each note is 1/4 note
bar2_notes = [71, 72, 74, 76]  # F, G, A, Bb

for i, pitch in enumerate(bar2_notes):
    start = bar2_start + i * BEAT_DURATION
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + note_lengths[i]))

# Bar 3: Bb (left hanging)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=bar3_start, end=bar3_start + 0.25))

# Bar 4: F, G, A, Bb (resolve the motif)
bar4_notes = [71, 72, 74, 76]
for i, pitch in enumerate(bar4_notes):
    start = bar4_start + i * BEAT_DURATION
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + note_lengths[i]))

# Repeat the drums for bars 2-4
# Bar 2
bar2_start = 1.5
for i in range(4):  # 4 beats in a bar
    beat_start = bar2_start + i * BEAT_DURATION
    # Kick on beat 1 and 3
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=beat_start, end=beat_start + 0.05))
    # Snare on beat 2 and 4
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=beat_start, end=beat_start + 0.05))
    # Hi-hat on every eighth note
    for j in range(2):
        hihat_start = beat_start + j * BEAT_DURATION / 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_start + 0.05))

# Bar 3
bar3_start = 3.0
for i in range(4):  # 4 beats in a bar
    beat_start = bar3_start + i * BEAT_DURATION
    # Kick on beat 1 and 3
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=beat_start, end=beat_start + 0.05))
    # Snare on beat 2 and 4
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=beat_start, end=beat_start + 0.05))
    # Hi-hat on every eighth note
    for j in range(2):
        hihat_start = beat_start + j * BEAT_DURATION / 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_start + 0.05))

# Bar 4
bar4_start = 4.5
for i in range(4):  # 4 beats in a bar
    beat_start = bar4_start + i * BEAT_DURATION
    # Kick on beat 1 and 3
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=beat_start, end=beat_start + 0.05))
    # Snare on beat 2 and 4
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=beat_start, end=beat_start + 0.05))
    # Hi-hat on every eighth note
    for j in range(2):
        hihat_start = beat_start + j * BEAT_DURATION / 2
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_start + 0.05))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
print("MIDI file created: 'dantes_introduction.mid'")
