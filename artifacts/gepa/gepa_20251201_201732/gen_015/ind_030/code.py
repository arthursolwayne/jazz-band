
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar duration in seconds = 1.5s (160 BPM, 4/4 time)
bar_duration = 1.5

# -----------------------------
# Bar 1: Only drums (0.0 - 1.5s)
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# -----------------------------
for bar in range(1):
    start = bar * bar_duration
    # Kick on beat 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + 1.125, end=start + 1.5))
    # Hi-hat on every eighth
    for i in range(8):
        start_time = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start_time, end=start_time + 0.1875))

# -----------------------------
# Bar 2: Full quartet (1.5 - 3.0s)
# -----------------------------
start = 1.5

# Bass: Walking line in F (root, fifth, chromatic approach)
# F2 (D2 in MIDI is 38, F2 is 42) -> F2 (42), C3 (48), Bb2 (41), F2 (42)
bass_notes = [
    (42, start, start + 0.375),
    (48, start + 0.375, start + 0.75),
    (41, start + 0.75, start + 1.125),
    (42, start + 1.125, start + 1.5)
]
for pitch, start_t, end_t in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=end_t))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    (42, start, start + 0.1875),  # F
    (46, start, start + 0.1875),  # A
    (48, start, start + 0.1875),  # C
    (52, start, start + 0.1875),  # E
]
for pitch, start_t in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=start + 0.375))

# Sax: Melody starts here (first bar of the motif)
# F to Bb (42 to 45), triplet feel
sax_notes = [
    (42, start, start + 0.25),   # F
    (45, start + 0.25, start + 0.5),  # Bb
    (42, start + 0.5, start + 0.75),   # F
    (45, start + 0.75, start + 1.0),   # Bb
]
for pitch, start_t, end_t in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=end_t))

# -----------------------------
# Bar 3: Full quartet (3.0 - 4.5s)
# -----------------------------
start = 3.0

# Bass: Walking line in F7 (F A C Eb)
# F2 (42), A2 (46), G#2 (43), F2 (42)
bass_notes = [
    (42, start, start + 0.375),
    (46, start + 0.375, start + 0.75),
    (43, start + 0.75, start + 1.125),
    (42, start + 1.125, start + 1.5)
]
for pitch, start_t, end_t in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=end_t))

# Piano: F7 (F A C Eb)
piano_notes = [
    (42, start, start + 0.1875),  # F
    (46, start, start + 0.1875),  # A
    (48, start, start + 0.1875),  # C
    (44, start, start + 0.1875),  # Eb
]
for pitch, start_t in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=start + 0.375))

# Drums: same pattern as bar 1
for bar in range(1):
    start = 3.0
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start + 0.75, end=start + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + 1.125, end=start + 1.5))
    for i in range(8):
        start_time = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start_time, end=start_time + 0.1875))

# Sax: Continue the motif
sax_notes = [
    (42, start, start + 0.25),   # F
    (45, start + 0.25, start + 0.5),  # Bb
    (42, start + 0.5, start + 0.75),   # F
    (45, start + 0.75, start + 1.0),   # Bb
]
for pitch, start_t, end_t in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=end_t))

# -----------------------------
# Bar 4: Full quartet (4.5 - 6.0s)
# -----------------------------
start = 4.5

# Bass: Walking line in Fmaj7 (F A C E)
# F2 (42), A2 (46), G#2 (43), F2 (42)
bass_notes = [
    (42, start, start + 0.375),
    (46, start + 0.375, start + 0.75),
    (43, start + 0.75, start + 1.125),
    (42, start + 1.125, start + 1.5)
]
for pitch, start_t, end_t in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=end_t))

# Piano: Fmaj7 (F A C E)
piano_notes = [
    (42, start, start + 0.1875),  # F
    (46, start, start + 0.1875),  # A
    (48, start, start + 0.1875),  # C
    (52, start, start + 0.1875),  # E
]
for pitch, start_t in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=start + 0.375))

# Drums: same pattern as bar 1
for bar in range(1):
    start = 4.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start + 0.75, end=start + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + 1.125, end=start + 1.5))
    for i in range(8):
        start_time = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start_time, end=start_time + 0.1875))

# Sax: Finish the motif
# F to Bb to F (glissando)
sax_notes = [
    (42, start, start + 0.25),   # F
    (45, start + 0.25, start + 0.5),  # Bb
    (42, start + 0.5, start + 0.75),   # F
    (45, start + 0.75, start + 1.0),   # Bb
]
for pitch, start_t, end_t in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start_t, end=end_t))

# -----------------------------
# Final setup
# -----------------------------
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
