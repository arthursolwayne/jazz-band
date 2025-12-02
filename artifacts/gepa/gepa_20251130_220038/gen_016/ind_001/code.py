
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Time in seconds per bar (160 BPM, 4/4 time)
bar_length = 1.5
time = 0.0

# -----------------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only, building tension

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hi-hat on every eighth note
for i in range(8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=end))

# -----------------------------
# Bar 2 (1.5 - 3.0s): Full quartet begins

# Bass line - Marcus (walking line in F minor)
# F - Gb - G - Ab
# 1: F (piano key 65)
# 2: Gb (66)
# 3: G (67)
# 4: Ab (68)
# Repeat for all bars

# Bar 2
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25))  # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0))  # Ab

# Piano - Diane (7th chords on 2 and 4, F7 and Bb7)
# Bar 2: F7 on beat 2 (1.875 - 2.25)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25))  # D

# Bar 2: Bb7 on beat 4 (2.625 - 3.0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0))  # G

# Sax - Dante (melody: F - Ab - G - F)
# F (65), Ab (68), G (67), F (65)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))  # F

# -----------------------------
# Bar 3 (3.0 - 4.5s)

# Drums: same pattern
for i in range(8):
    start = 3.0 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375))  # Kick 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.75, end=4.125))  # Kick 3

drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=3.375, end=3.75))  # Snare 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.125, end=4.5))  # Snare 4

# Bass line (F - Gb - G - Ab)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75))  # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5))  # Ab

# Piano: 7th chords on 2 and 4
# Bar 3: F7 on beat 2 (3.375 - 3.75)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75))  # D

# Bar 3: Bb7 on beat 4 (4.125 - 4.5)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5))  # G

# Sax melody (F - Ab - G - F, same as Bar 2, but with a slight variation in phrasing)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5))  # F

# -----------------------------
# Bar 4 (4.5 - 6.0s)

# Drums
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))  # Kick 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.625))  # Kick 3

drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25))  # Snare 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.625, end=6.0))  # Snare 4

# Bass line (F - Gb - G - Ab)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25))  # Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0))  # Ab

# Piano: 7th chords on 2 and 4
# Bar 4: F7 on beat 2 (4.875 - 5.25)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25))  # D

# Bar 4: Bb7 on beat 4 (5.625 - 6.0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0))  # G

# Sax: Same motif, but now resolves back to F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0))  # F

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file written to 'dante_intro.mid'")
