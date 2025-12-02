
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (MIDI note numbers)
kick = 36
snare = 38
hihat = 42

# Bar duration in seconds (160 BPM, 4/4 time)
bar_length = 1.5  # 60/160 * 4 = 1.5 seconds per bar

# -------------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat every 8th note
# Slightly syncopated, with dynamic velocities

# Kick on beats 1 and 3 (0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=kick, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=75, pitch=kick, start=0.75, end=0.8))

# Snare on beats 2 and 4 (0.375 and 1.125s)
drums.notes.append(pretty_midi.Note(velocity=95, pitch=snare, start=0.375, end=0.4))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=1.125, end=1.15))

# Hihat on every eighth note
hihat_notes = [0.0, 0.375, 0.75, 1.125]
for t in hihat_notes:
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=hihat, start=t, end=t + 0.05))

# -------------------
# Bar 2: Full band (1.5 - 3.0s)
# Bass: walking line with chromatic approaches, Dm7 -> G7 -> Cm7 -> F7

# Bass line in D minor (D, F, G, A, Bb, C, Eb)
# Walking bass line: D - F - G - A - Bb - C - Eb - D (chromatic approach to G7)

bass_notes = [
    (1.5, 62),  # D (Dm7)
    (1.625, 64), # F
    (1.75, 67),  # G
    (1.875, 69), # A
    (2.0, 67),   # Bb (chromatic descent to G)
    (2.125, 69), # C
    (2.25, 64),  # Eb
    (2.375, 62), # D
    (2.5, 67),   # G (G7)
    (2.625, 69), # A
    (2.75, 71),  # Bb
    (2.875, 69), # C
    (3.0, 67),   # D (Dm7)
]

for t, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.1))

# Piano: 7th chords on 2 and 4, comping with emotional tension
# Dm7 (D, F, A, C) on beat 2 (1.875s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=1.9))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=1.9))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=1.9))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=1.9))  # C

# G7 (G, B, D, F) on beat 4 (2.625s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.65))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=2.65))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.65))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=2.65))  # F

# Saxophone: Melody - short, haunting motif, with space and silence
# D - F - G - A (Dm7), then resolve to D again with space
# Play on beats 1 and 3 (1.5 and 2.25s)

sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.55))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.675))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.8))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.925))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.3))  # D

# -------------------
# Bar 3: Full band (3.0 - 4.5s)

# Drums: More syncopation, velocity variation
# Kick on 1 and 3 (3.0 and 3.75s)
drums.notes.append(pretty_midi.Note(velocity=75, pitch=kick, start=3.0, end=3.05))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=kick, start=3.75, end=3.8))

# Snare on 2 and 4 (3.375 and 4.125s)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=3.375, end=3.4))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=snare, start=4.125, end=4.15))

# Hihat every eighth note
for t in [3.0, 3.375, 3.75, 4.125]:
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=hihat, start=t, end=t + 0.05))

# Bass: Dm7 -> G7 -> Cm7 -> F7

# Dm7 (D, F, A, C)
bass_notes = [
    (3.0, 62),  # D
    (3.125, 64), # F
    (3.25, 69), # A
    (3.375, 67), # C
    (3.5, 64),   # F (chromatic approach to G)
    (3.625, 67), # G
    (3.75, 69),  # A
    (3.875, 71), # Bb
    (4.0, 69),   # C
    (4.125, 67), # D
    (4.25, 69),  # E
    (4.375, 67), # F
    (4.5, 69),   # G
]

for t, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.1))

# Piano: 7th chords on 2 and 4
# Cm7 (C, Eb, G, Bb) on beat 2 (3.375s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.4))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=3.375, end=3.4))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.4))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=3.375, end=3.4))  # Bb

# F7 (F, A, C, Eb) on beat 4 (4.125s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.15))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.15))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.15))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=4.125, end=4.15))  # Eb

# Saxophone: Echo the motif but with a slight variation
# D - F - G - A (Dm7), then resolve to D again with more space

sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.05))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.175))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.3))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.425))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.8))  # D (with space)

# -------------------
# Bar 4: Full band (4.5 - 6.0s)

# Drums: Slight change in energy, end with a big snare
# Kick on 1 and 3 (4.5 and 5.25s)
drums.notes.append(pretty_midi.Note(velocity=85, pitch=kick, start=4.5, end=4.55))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=5.25, end=5.3))

# Snare on 2 and 4 (4.875 and 5.625s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=4.9))
drums.notes.append(pretty_midi.Note(velocity=105, pitch=snare, start=5.625, end=5.65))

# Hihat every eighth note
for t in [4.5, 4.875, 5.25, 5.625]:
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=hihat, start=t, end=t + 0.05))

# Bass: F7 (F, A, C, Eb) for resolution
bass_notes = [
    (4.5, 65),  # F
    (4.625, 69), # A
    (4.75, 67), # C
    (4.875, 64), # Eb
    (5.0, 69),   # A
    (5.125, 71), # Bb
    (5.25, 69),  # C
    (5.375, 67), # D
    (5.5, 69),   # E
    (5.625, 67), # F
    (5.75, 69),  # G
    (5.875, 67), # A
    (6.0, 69),   # Bb
]

for t, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.1))

# Piano: F7 chord on beat 4 (5.625s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=5.65))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=5.65))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.65))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=5.625, end=5.65))  # Eb

# Saxophone: Final resolution, full motif
# D - F - G - A (Dm7), then D with a breath of silence
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.55))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.675))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.8))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=4.925))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.3))  # D

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("four_bar_intro.mid")
