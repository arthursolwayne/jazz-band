
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    "kick": 36,
    "snare": 38,
    "hihat": 42
}

# Bar duration at 160 BPM, 4/4 time
bar_length = 1.5  # seconds per bar
beat_length = 0.375  # seconds per beat

# ---------------------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray sets the mood, hihat on every 8th
# Kick on 1 and 3, snare on 2 and 4
# ---------------------------

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["kick"], start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["kick"], start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["snare"], start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["snare"], start=1.125, end=1.5))

# Hihat on every 8th
for i in range(0, 4):  # 4 eighths per bar
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes["hihat"], start=start, end=end))

# ---------------------------
# Bar 2: Full quartet (1.5 - 3.0s)
# Diane (piano) plays D7 chord on beat 2 and 4
# Marcus (bass) walks with chromatic motion
# Dante (sax) plays the motif
# ---------------------------

# Piano: D7 on 2 and 4 (D F# A C)
diane_notes = [
    (1.875, 65),  # D (D4)
    (1.875, 67),  # F#
    (1.875, 69),  # A
    (1.875, 62),  # C
    (3.0, 65),  # D
    (3.0, 67),  # F#
    (3.0, 69),  # A
    (3.0, 62)   # C
]

for start, pitch in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Bass: D (65) -> D# (66) -> E (67) -> F (68) chromatic walk
bass_notes = [
    (1.5, 65),  # D
    (1.875, 66),  # D#
    (2.25, 67),  # E
    (2.625, 68),  # F
    (3.0, 65)   # D again
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.375))

# Sax: Motif
# D (65) -> E (67) -> D (65) -> E (67) -> F# (69) -> B (71) -> A (69)
# Start at 1.5, then leave it hanging, return at 3.0
sax_notes = [
    (1.5, 65),  # D
    (1.625, 67),  # E
    (1.75, 65),  # D
    (1.875, 67),  # E
    (2.0, 69),  # F#
    (2.125, 71),  # B
    (2.25, 69),  # A
    (3.0, 65),  # D
    (3.125, 67),  # E
    (3.25, 65),  # D
    (3.375, 67)   # E
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# ---------------------------
# Bar 3: Full quartet (3.0 - 4.5s)
# Repeat motif with variation
# ---------------------------

# Piano: D7 again on 2 and 4
diane_notes = [
    (3.875, 65),  # D
    (3.875, 67),  # F#
    (3.875, 69),  # A
    (3.875, 62),  # C
    (4.5, 65),  # D
    (4.5, 67),  # F#
    (4.5, 69),  # A
    (4.5, 62)   # C
]

for start, pitch in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Bass: Chromatic walk again
bass_notes = [
    (3.0, 65),  # D
    (3.375, 66),  # D#
    (3.75, 67),  # E
    (4.125, 68),  # F
    (4.5, 65)   # D again
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.375))

# Sax: Motif again, but with a slight variation
sax_notes = [
    (3.0, 65),  # D
    (3.125, 67),  # E
    (3.25, 65),  # D
    (3.375, 67),  # E
    (3.5, 69),  # F#
    (3.625, 71),  # B
    (3.75, 69),  # A
    (4.5, 65),  # D
    (4.625, 67),  # E
    (4.75, 65),  # D
    (4.875, 67)   # E
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# ---------------------------
# Bar 4: Full quartet (4.5 - 6.0s)
# Resolve the motif, bring it back in
# ---------------------------

# Piano: D7 again on 2 and 4
diane_notes = [
    (5.25, 65),  # D
    (5.25, 67),  # F#
    (5.25, 69),  # A
    (5.25, 62),  # C
    (6.0, 65),  # D
    (6.0, 67),  # F#
    (6.0, 69),  # A
    (6.0, 62)   # C
]

for start, pitch in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Bass: Chromatic walk
bass_notes = [
    (4.5, 65),  # D
    (4.875, 66),  # D#
    (5.25, 67),  # E
    (5.625, 68),  # F
    (6.0, 65)   # D again
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.375))

# Sax: Finale variation of the motif
sax_notes = [
    (4.5, 65),  # D
    (4.625, 67),  # E
    (4.75, 65),  # D
    (4.875, 67),  # E
    (5.0, 69),  # F#
    (5.125, 71),  # B
    (5.25, 69),  # A
    (6.0, 65),  # D
    (6.125, 67),  # E
    (6.25, 65),  # D
    (6.375, 67)   # E
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125))

# ---------------------------
# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# ---------------------------

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["kick"], start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["snare"], start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["kick"], start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["snare"], start=4.125, end=4.5))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["kick"], start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["snare"], start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["kick"], start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes["snare"], start=5.625, end=6.0))

# Hihat on every 8th
for i in range(3, 6):  # 6 eighths in 2 bars
    for j in range(0, 4):  # 4 eighths per bar
        start = (i * 1.5) + (j * 0.375)
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes["hihat"], start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
