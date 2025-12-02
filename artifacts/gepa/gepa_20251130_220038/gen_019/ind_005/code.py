
import pretty_midi

# Initialize the MIDI file with tempo and time signature
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time values (seconds per beat = 60 / 160 = 0.375)
BAR = 1.5
BEAT = 0.375
EIGHTH = BEAT / 2
QUARTER = BEAT
HALF = 2 * BEAT

# -------------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0 - 1.5s

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat
for t in range(0, 1500, 375):  # 0, 375, 750, 1125
    start = t / 1000
    end = start + EIGHTH
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# -------------------------
# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
# F minor key (F, Gb, Ab, Bb, B, C, Db)
# Chromatic descent from B to F

# Bar 2 (1.5 - 3.0s)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.875))  # B
bass.notes.append(pretty_midi.Note(velocity=70, pitch=70, start=1.875, end=2.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.625))  # A
bass.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=2.625, end=3.0))  # G

# Bar 3 (3.0 - 4.5s)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.375))  # F#
bass.notes.append(pretty_midi.Note(velocity=70, pitch=64, start=3.375, end=3.75))  # F
bass.notes.append(pretty_midi.Note(velocity=70, pitch=62, start=3.75, end=4.125))  # Eb
bass.notes.append(pretty_midi.Note(velocity=70, pitch=60, start=4.125, end=4.5))  # D

# Bar 4 (4.5 - 6.0s)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=59, start=4.5, end=4.875))  # C#
bass.notes.append(pretty_midi.Note(velocity=70, pitch=57, start=4.875, end=5.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=70, pitch=55, start=5.25, end=5.625))  # A
bass.notes.append(pretty_midi.Note(velocity=70, pitch=53, start=5.625, end=6.0))  # G

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab

# Bar 2 (1.5 - 3.0s)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25))  # B (F7)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25))  # Eb

# Bar 3 (3.0 - 4.5s)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75))  # D (Bb7)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75))  # Ab

# Bar 4 (4.5 - 6.0s)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25))  # B (F7)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25))  # Eb

# Drums (Bars 2-4)
# Same pattern: kick on 1 and 3, snare on 2 and 4, hihat every eighth
# Bar 2 (1.5 - 3.0s)
for t in range(1500, 3000, 375):
    start = t / 1000
    end = start + EIGHTH
    if t == 1500 or t == 2250:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=end))
    elif t == 1875 or t == 2625:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=start, end=end))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 3 (3.0 - 4.5s)
for t in range(3000, 4500, 375):
    start = t / 1000
    end = start + EIGHTH
    if t == 3000 or t == 3750:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=end))
    elif t == 3375 or t == 4125:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=start, end=end))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 4 (4.5 - 6.0s)
for t in range(4500, 6000, 375):
    start = t / 1000
    end = start + EIGHTH
    if t == 4500 or t == 5250:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=end))
    elif t == 4875 or t == 5625:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=start, end=end))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# SAX: Dante's motif — short, low, and memorable
# F minor: F - Ab - Bb - B (F7 voicing)
# Start on F, descend chromatically, then resolve

# Bar 2 (1.5 - 3.0s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0))  # C

# Bar 3 (3.0 - 4.5s)
# Leave it hanging — no notes here. Silence.

# Bar 4 (4.5 - 6.0s)
# Return and finish the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0))  # C

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
