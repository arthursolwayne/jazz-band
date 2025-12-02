
import pretty_midi

# Setup the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar at 160 BPM is 1.5 seconds
bar_duration = 1.5
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, with a slight syncopation

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4 (slightly off-beat for tension)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.45, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.2, end=1.5))

# Hi-hat on every eighth note, with a slight variation in timing for space
for i in range(8):
    time = i * 0.1875  # 0.1875s per eighth note
    if i % 2 == 0:
        # Slightly ahead on even eighth notes
        time += 0.02
    else:
        # Slightly behind on odd eighth notes
        time -= 0.02
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.1875))

# Bar 2: Full ensemble enters
# Start with a short, singing motif on sax
# Fmaj7 chord: F, A, C, E (piano comp on 2 and 4)
# Bass walks with chromatic approach
# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Piano comp: F7 on beat 2, F7 on beat 4
# F7: F, A, C, E♭
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=1.5, end=1.875))  # E♭

piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375))

# Bass line: Chromatic walk from F to A
# F (77) -> F# (78) -> G (79) -> A (81)
# (full 4-bar walk, but we're only showing the first bar)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=77, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=70, pitch=78, start=1.875, end=2.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=70, pitch=79, start=2.25, end=2.625))  # G
bass.notes.append(pretty_midi.Note(velocity=70, pitch=81, start=2.625, end=3.0))   # A

# Saxophone: Short motif, starts on beat 1, leaves it hanging
# F (77) -> G (79) -> E (74) -> F (77)
# Start at bar 2 (1.5s), play the first three notes, leave the last note to come back later
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.6875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.6875, end=1.875)) # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0625)) # E
# The F (77) is left hanging, to be resolved in bar 4

# Drums continue the same pattern
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=2.25, end=2.625))

# Snare on 2 and 4 (slightly off-beat)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.95, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=2.8, end=3.0))

# Hi-hat on every eighth note
for i in range(8):
    time = 1.5 + i * 0.1875
    if i % 2 == 0:
        time += 0.02
    else:
        time -= 0.02
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.1875))

# Bar 3: Continue the same pattern
# Piano comp again on beat 2 and 4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75))

piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25))

# Bass line: continue the chromatic walk
bass.notes.append(pretty_midi.Note(velocity=70, pitch=83, start=3.0, end=3.375))  # B♭
bass.notes.append(pretty_midi.Note(velocity=70, pitch=84, start=3.375, end=3.75))  # B
bass.notes.append(pretty_midi.Note(velocity=70, pitch=86, start=3.75, end=4.125))  # C
bass.notes.append(pretty_midi.Note(velocity=70, pitch=88, start=4.125, end=4.5))   # D

bass.notes.append(pretty_midi.Note(velocity=70, pitch=90, start=4.5, end=4.875))  # E
bass.notes.append(pretty_midi.Note(velocity=70, pitch=92, start=4.875, end=5.25))  # F
bass.notes.append(pretty_midi.Note(velocity=70, pitch=93, start=5.25, end=5.625))  # F#
bass.notes.append(pretty_midi.Note(velocity=70, pitch=95, start=5.625, end=6.0))   # G

# Drums continue the same pattern
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=3.75, end=4.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=3.45, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=4.2, end=4.5))

# Hi-hat on every eighth note
for i in range(8):
    time = 3.0 + i * 0.1875
    if i % 2 == 0:
        time += 0.02
    else:
        time -= 0.02
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.1875))

# Bar 4: Sax returns to finish the motif, resolve the F
# Play the last note of the motif (F) on beat 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.0625))  # F

# Add the final resolution to A (79) to complete the idea
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=5.0625, end=5.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.4375))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=5.4375, end=5.625))  # F

# Add the final resolution to A (81)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=5.8125))  # A

# Add the final sustained note to let it hang
sax.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=5.8125, end=6.0))  # F

# Append instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_introduction.mid")
