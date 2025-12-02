
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note numbers for F minor scale
Fm_scale = [65, 67, 69, 70, 72, 74, 76]  # F, Gb, G, Ab, A, Bb, Bb (octave 4)

# Define drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth with small variations
bar1_start = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=bar1_start + 1.125, end=bar1_start + 1.5))

# Snare on 2 and 4 with subtle syncopation
drums.notes.append(pretty_midi.Note(velocity=110, pitch=snare, start=bar1_start + 0.75, end=bar1_start + 0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=snare, start=bar1_start + 1.875, end=bar1_start + 2.0))

# Hi-hat on every eighth with slight timing variations
hihat_notes = [
    bar1_start + 0.0,
    bar1_start + 0.375,
    bar1_start + 0.75,
    bar1_start + 1.125,
    bar1_start + 1.5,
    bar1_start + 1.875,
    bar1_start + 2.25,
    bar1_start + 2.625
]

for note_start in hihat_notes:
    # Vary velocity slightly to add human feel
    velocity = 90 + (note_start % 0.5) * 10
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=hihat, start=note_start, end=note_start + 0.125))

# Bar 2: Full quartet starts (1.5s - 3.0s)
bar2_start = 1.5

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (bar2_start, 65),  # F
    (bar2_start + 0.375, 64),  # Eb
    (bar2_start + 0.75, 65),  # F
    (bar2_start + 1.125, 66),  # G
    (bar2_start + 1.5, 67),  # Gb
    (bar2_start + 1.875, 66),  # G
    (bar2_start + 2.25, 65),  # F
    (bar2_start + 2.625, 64),  # Eb
]

for note_start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=note_start, end=note_start + 0.25))

# Piano: 7th chords, comp on 2 and 4
# F7 (F, A, C, Eb), Bb7 (Bb, D, F, Ab), etc.
piano_notes = [
    # Bar 2, beat 1: F7 (F, A, C, Eb)
    (bar2_start, 65, 70, 69, 67),
    # Bar 2, beat 2: Bb7 (Bb, D, F, Ab)
    (bar2_start + 0.75, 71, 74, 65, 69),
    # Bar 2, beat 3: F7 again
    (bar2_start + 1.5, 65, 70, 69, 67),
    # Bar 2, beat 4: Bb7 again
    (bar2_start + 2.25, 71, 74, 65, 69),
]

for note_start, *pitches in piano_notes:
    for pitch in pitches:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=note_start, end=note_start + 0.25))

# Sax: Melody - short, singing motif. Start it, leave it hanging
# F - Ab - Bb - A (F, Ab, Bb, A)
sax_notes = [
    (bar2_start, 65),  # F
    (bar2_start + 0.375, 69),  # Ab
    (bar2_start + 0.75, 71),  # Bb
    (bar2_start + 1.125, 72),  # A
]

for note_start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.125))

# Bar 3: Continue the pattern
bar3_start = 3.0

# Bass: Continue walking line
bass_notes = [
    (bar3_start, 71),  # Bb
    (bar3_start + 0.375, 69),  # Ab
    (bar3_start + 0.75, 71),  # Bb
    (bar3_start + 1.125, 67),  # Gb
    (bar3_start + 1.5, 69),  # Ab
    (bar3_start + 1.875, 71),  # Bb
    (bar3_start + 2.25, 65),  # F
    (bar3_start + 2.625, 67),  # Gb
]

for note_start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=note_start, end=note_start + 0.25))

# Piano: Continue comping
piano_notes = [
    (bar3_start, 65, 70, 69, 67),  # F7
    (bar3_start + 0.75, 71, 74, 65, 69),  # Bb7
    (bar3_start + 1.5, 65, 70, 69, 67),  # F7
    (bar3_start + 2.25, 71, 74, 65, 69),  # Bb7
]

for note_start, *pitches in piano_notes:
    for pitch in pitches:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=note_start, end=note_start + 0.25))

# Sax: Repeat the motif, then leave it hanging
sax_notes = [
    (bar3_start, 65),  # F
    (bar3_start + 0.375, 69),  # Ab
    (bar3_start + 0.75, 71),  # Bb
    (bar3_start + 1.125, 72),  # A
]

for note_start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_start + 0.125))

# Bar 4: Build toward resolution, leave it open
bar4_start = 4.5

# Bass: Continue walking line
bass_notes = [
    (bar4_start, 67),  # Gb
    (bar4_start + 0.375, 69),  # Ab
    (bar4_start + 0.75, 71),  # Bb
    (bar4_start + 1.125, 65),  # F
    (bar4_start + 1.5, 67),  # Gb
    (bar4_start + 1.875, 69),  # Ab
    (bar4_start + 2.25, 71),  # Bb
    (bar4_start + 2.625, 65),  # F
]

for note_start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=note_start, end=note_start + 0.25))

# Piano: Continue comping
piano_notes = [
    (bar4_start, 65, 70, 69, 67),  # F7
    (bar4_start + 0.75, 71, 74, 65, 69),  # Bb7
    (bar4_start + 1.5, 65, 70, 69, 67),  # F7
    (bar4_start + 2.25, 71, 74, 65, 69),  # Bb7
]

for note_start, *pitches in piano_notes:
    for pitch in pitches:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=note_start, end=note_start + 0.25))

# Sax: End on the last note of the motif (A), leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=bar4_start + 1.5, end=bar4_start + 1.75))

# Add instruments to MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("intro_in_fm.mid")
