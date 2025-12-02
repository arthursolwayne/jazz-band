
import pretty_midi

# Initialize a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar in seconds (160 BPM => 60/160 = 0.375 sec per beat, 1.5 sec per bar)
BAR_DURATION = 1.5

# --- BAR 1 (0.0 - 1.5s): Little Ray on drums only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat on every eighth note (8 notes per bar)
for i in range(8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=start, end=end))

# --- BAR 2 (1.5 - 3.0s): Full band in - sax takes melody ---

# SAX: Melody - short motif starting on Fm7 (F, Ab, Bb, D)
# F (F4), Ab (Ab4), Bb (Bb4), D (D4) -> Fm7 chord
# Motif: F, Ab, Bb, D (create a small phrase, then leave it hanging)

# Note durations: 0.375s per beat, half-note = 0.75s, quarter = 0.375s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875))     # F4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25))    # Ab4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))    # Bb4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0))     # D4

# BASS: Walking line - chromatic approach on Fm7
# F, Gb (F#, chromatic), G, F (resolve to F)
# This is a descending chromatic line with a resolution
bass_notes = [
    (65, 1.5, 1.875),     # F3
    (66, 1.875, 2.25),    # F#
    (67, 2.25, 2.625),    # G3
    (65, 2.625, 3.0)      # F3
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# PIANO: Comp on 2 and 4 (7th chords)
# Fm7 on beat 2, Fm7 on beat 4

# Fm7 = F, Ab, Bb, D (chord tones)
# Comp: play the chord on beat 2 and 4

# Fm7 on beat 2 (1.875 - 2.25)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25))  # D4

# Fm7 on beat 4 (2.625 - 3.0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0))   # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0))   # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0))   # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0))   # D4

# --- BAR 3 (3.0 - 4.5s): Full band in, sax continues motif (unfinished) ---

# SAX: repeat the same motif (unfinished), same as bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375))     # F4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75))    # Ab4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))    # Bb4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5))     # D4

# BASS: Walking line, same as bar 2 but shifted
bass_notes = [
    (65, 3.0, 3.375),     # F3
    (66, 3.375, 3.75),    # F#
    (67, 3.75, 4.125),    # G3
    (65, 4.125, 4.5)      # F3
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# PIANO: same comp on 2 and 4
# Fm7 at beat 2 (3.375 - 3.75)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75))  # D4

# Fm7 at beat 4 (4.125 - 4.5)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5))   # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5))   # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5))   # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5))   # D4

# --- BAR 4 (4.5 - 6.0s): Full band in, sax finishes the motif ---

# SAX: finish the motif with a resolution (F minor)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875))     # F4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25))    # Ab4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625))    # Bb4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0))     # D4

# BASS: Walking line, same as before
bass_notes = [
    (65, 4.5, 4.875),     # F3
    (66, 4.875, 5.25),    # F#
    (67, 5.25, 5.625),    # G3
    (65, 5.625, 6.0)      # F3
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# PIANO: same comp on 2 and 4
# Fm7 at beat 2 (4.875 - 5.25)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25))  # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # D4

# Fm7 at beat 4 (5.625 - 6.0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0))   # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0))   # Ab4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0))   # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0))   # D4

# Add the instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_introduction.mid")
