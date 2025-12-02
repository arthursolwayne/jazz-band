
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes (MIDI note numbers)
KICK = 36
SNARE = 38
HIHAT = 42

# Define time in seconds per bar (160 BPM, 4/4 time)
bar_length = 1.5  # 6 seconds for 4 bars
beat_length = 0.375  # 0.375 seconds per beat

# Bar 1 (0.0 - 1.5s): Drums only
# Little Ray sets the mood with a kick on 1 and 3, snare on 2 and 4, and hihat on every eighth
for i in range(0, 4):  # 4 beats per bar
    time = i * beat_length
    if i % 2 == 0:
        # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + beat_length))
    else:
        # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + beat_length))
    # Hi-hat on every eighth note
    for j in range(2):  # 2 eighth notes per beat
        hihat_time = time + j * (beat_length / 2)
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + (beat_length / 2)))

# Bar 2 (1.5 - 3.0s): Everyone in
# Marcus on bass: Walking line with chromatic approaches
# Start on F (MIDI 65) and walk down with chromatic approach to Eb
bass_notes = [
    (1.5, 65),    # F
    (1.875, 64),  # E
    (2.25, 63),   # D
    (2.625, 62),  # C
    (3.0, 61),    # Bb
]

for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + beat_length))

# Diane on piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Minor 7th chord, root position
piano_notes = [
    (1.5, 65),    # F
    (1.5, 76),    # Ab
    (1.5, 79),    # C
    (1.5, 69),    # Eb

    (2.25, 65),   # F again on beat 3 (fill)
    (2.25, 76),   # Ab
    (2.25, 79),   # C
    (2.25, 69),   # Eb
]

for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + beat_length))

# Dante on sax: Short motif, make it sing
# Start with F (65), then Bb (69) with a slight bend, then leave it hanging on Ab (76)
# Return in bar 3 to finish the motif on Eb (69) with a resolution
sax_notes = [
    (1.5, 65),    # F
    (1.875, 69),  # Bb
    (2.25, 76),   # Ab (hanging)
    (3.0, 69),    # Eb (resolution)
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + beat_length))

# Bar 3 (3.0 - 4.5s): Full quartet continues
# Marcus walks again, this time up
bass_notes = [
    (3.0, 61),    # Bb
    (3.375, 62),  # C
    (3.75, 63),   # D
    (4.125, 64),  # E
    (4.5, 65),    # F
]

for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + beat_length))

# Diane comp 7th chords again
piano_notes = [
    (3.0, 65),    # F
    (3.0, 76),    # Ab
    (3.0, 79),    # C
    (3.0, 69),    # Eb

    (3.75, 65),   # F again on beat 3
    (3.75, 76),   # Ab
    (3.75, 79),   # C
    (3.75, 69),   # Eb
]

for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + beat_length))

# Dante continues the motif, now resolving the tension
sax_notes = [
    (3.0, 69),    # Eb (resolving the tension)
    (3.375, 65),  # F (return to home)
    (3.75, 69),   # Eb (reiterate)
    (4.125, 65),  # F
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + beat_length))

# Bar 4 (4.5 - 6.0s): Full quartet
# Marcus walks again
bass_notes = [
    (4.5, 65),    # F
    (4.875, 64),  # E
    (5.25, 63),   # D
    (5.625, 62),  # C
    (6.0, 61),    # Bb
]

for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + beat_length))

# Diane comp 7th chords again
piano_notes = [
    (4.5, 65),    # F
    (4.5, 76),    # Ab
    (4.5, 79),    # C
    (4.5, 69),    # Eb

    (5.25, 65),   # F again on beat 3
    (5.25, 76),   # Ab
    (5.25, 79),   # C
    (5.25, 69),   # Eb
]

for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + beat_length))

# Dante wraps up with a final note, leaving it on the edge of resolution
sax_notes = [
    (4.5, 69),    # Eb (final note, unresolved)
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + beat_length))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
