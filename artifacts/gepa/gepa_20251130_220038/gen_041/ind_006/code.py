
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Duration of each bar (6 seconds / 4 bars = 1.5 seconds per bar)
bar_duration = 1.5

# --- BAR 1: Little Ray alone (0.0 - 1.5s) ---
# Kicks on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beats 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on beats 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth
for i in range(0, 6, 1):  # 6 eighth notes in a 4/4 bar
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=end))

# --- BAR 2: Full quartet (1.5 - 3.0s) ---

# Saxophone: Dante's motif — short, melodic, with space
sax_notes = [
    (113, 0.0, 0.375),   # D (Dm7) - 1st beat
    (109, 0.75, 1.125)   # F (Dm7) - 3rd beat (leaving it hanging)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + 1.5, end=end + 1.5))

# Bass: Marcus's walking line in Dm7
bass_notes = [
    (62, 1.5, 1.875),     # D (root) on beat 1
    (65, 1.875, 2.25),    # F (3rd) on beat 2
    (67, 2.25, 2.625),    # A (5th) on beat 3
    (64, 2.625, 3.0),     # C (7th) on beat 4
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Diane's comping on 2 and 4 with Dm7 chords
# Dm7 = D, F, A, C
# 2: Dm7 (1.875 - 2.25)
# 4: Dm7 (2.625 - 3.0)

# Dm7 chord on beat 2
for pitch in [62, 65, 67, 64]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=1.875, end=2.25))

# Dm7 chord on beat 4
for pitch in [62, 65, 67, 64]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=2.625, end=3.0))

# --- BAR 3: Full quartet (3.0 - 4.5s) ---

# Saxophone: Repeat the motif, but resolve it
sax_notes = [
    (113, 0.0, 0.375),   # D
    (109, 0.75, 1.125),  # F
    (107, 1.125, 1.5),   # Bb (resolution)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + 3.0, end=end + 3.0))

# Bass: Marcus's walking line (same pattern, one octave up)
bass_notes = [
    (72, 3.0, 3.375),     # D (root) on beat 1
    (75, 3.375, 3.75),    # F (3rd) on beat 2
    (77, 3.75, 4.125),    # A (5th) on beat 3
    (74, 4.125, 4.5),     # C (7th) on beat 4
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Diane's comping on 2 and 4 with Dm7 chords
# 2: Dm7 (3.375 - 3.75)
# 4: Dm7 (4.125 - 4.5)

# Dm7 chord on beat 2
for pitch in [72, 75, 77, 74]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=3.375, end=3.75))

# Dm7 chord on beat 4
for pitch in [72, 75, 77, 74]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=4.125, end=4.5))

# --- BAR 4: Full quartet (4.5 - 6.0s) ---

# Saxophone: Repeat the motif, embellish slightly
sax_notes = [
    (113, 0.0, 0.375),   # D
    (109, 0.75, 1.125),  # F
    (111, 1.125, 1.5),   # Bb
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start + 4.5, end=end + 4.5))

# Bass: Marcus's walking line (same pattern, one octave down)
bass_notes = [
    (52, 4.5, 4.875),     # D (root) on beat 1
    (55, 4.875, 5.25),    # F (3rd) on beat 2
    (57, 5.25, 5.625),    # A (5th) on beat 3
    (54, 5.625, 6.0),     # C (7th) on beat 4
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Diane's comping on 2 and 4 with Dm7 chords
# 2: Dm7 (4.875 - 5.25)
# 4: Dm7 (5.625 - 6.0)

# Dm7 chord on beat 2
for pitch in [52, 55, 57, 54]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=4.875, end=5.25))

# Dm7 chord on beat 4
for pitch in [52, 55, 57, 54]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=5.625, end=6.0))

# Drums: same pattern as bar 1
# Kicks on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.625))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.625, end=6.0))

# Hihat on every eighth
for i in range(0, 6, 1):  # 6 eighth notes in a 4/4 bar
    start = i * 0.375 + 4.5
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
