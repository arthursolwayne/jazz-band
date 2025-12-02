
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define drum note numbers
DRUM_KICK = 36
DRUM_SNARE = 38
DRUM_HI_HAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # in seconds (160 BPM = 1.5s per bar)

# Drums in Bar 1
# Kick on beat 1 and 3 (0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=0.0, end=0.0 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=0.75, end=0.75 + 0.375))

# Snare on beat 2 and 4 (0.375 and 1.125s)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=DRUM_SNARE, start=0.375, end=0.375 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=DRUM_SNARE, start=1.125, end=1.125 + 0.375))

# Hihat on every eighth note
for i in range(0, 8):
    start = i * 0.375
    end = start + 0.1875  # 1/8 note
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=DRUM_HI_HAT, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# --- BASS: Marcus ---
# Walking line in Fm. Chromatic approaches. No repeating notes.
# Fm scale: F, Ab, Bb, C, Db, Eb, F
# Walking bass line (compound time, 4/4)

# Bar 2 (1.5 - 3.0s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.5 + 0.25))  # F (Ab)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.75 + 0.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.0, end=2.0 + 0.25))  # Db
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.25 + 0.25))  # Bb

# Bar 3 (3.0 - 4.5s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.0 + 0.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.25 + 0.25))  # G (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.5 + 0.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.75 + 0.25))  # Bb

# Bar 4 (4.5 - 6.0s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.5 + 0.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.75 + 0.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.0 + 0.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.25 + 0.25))  # Eb

# --- PIANO: Diane ---
# 7th chords, comp on 2 and 4. Dynamic, angry, emotional.

# Bar 2 (1.5 - 3.0s)
# Fm7 on beat 2 (1.75 - 2.0s)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=1.75, end=2.0))  # Bb

# Bar 3 (3.0 - 4.5s)
# Fm7 on beat 2 (3.25 - 3.5s)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=3.25, end=3.5))

# Bar 4 (4.5 - 6.0s)
# Fm7 on beat 2 (4.75 - 5.0s)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=4.75, end=5.0))

# --- SAX: Dante ---
# Original motif. Short, singable, leaves it hanging, then finishes it.

# Bar 2 (1.5 - 3.0s)
# Start of motif: F (69), Bb (62), Ab (60), Bb (62) — a question

sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6))  # F
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=1.75, end=1.85))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1))  # Ab
sax.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.35))  # Bb

# Bar 3 (3.0 - 4.5s)
# Let it hang, then come back with resolution

sax.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1))  # Bb
sax.notes.append(pretty_midi.Note(velocity=85, pitch=60, start=3.25, end=3.35))  # Ab

# Bar 4 (4.5 - 6.0s)
# Finish the motif with a resolution or twist

sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.6))  # F
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=4.75, end=4.85))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.1))  # Ab
sax.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.35))  # Bb

# --- DRUMS: Bars 2-4 (1.5 - 6.0s) ---
# Same pattern as bar 1, but with more energy

# Bar 2 (1.5-3.0s)
for i in range(0, 8):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    if i % 2 == 0:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=start, end=end))
    elif i == 1 or i == 3 or i == 5 or i == 7:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=DRUM_SNARE, start=start, end=end))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=DRUM_HI_HAT, start=start, end=end))

# Bar 3 (3.0-4.5s)
for i in range(0, 8):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=start, end=end))
    elif i == 1 or i == 3 or i == 5 or i == 7:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=DRUM_SNARE, start=start, end=end))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=DRUM_HI_HAT, start=start, end=end))

# Bar 4 (4.5-6.0s)
for i in range(0, 8):
    start = 4.5 + i * 0.375
    end = start + 0.1875
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=DRUM_KICK, start=start, end=end))
    elif i == 1 or i == 3 or i == 5 or i == 7:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=DRUM_SNARE, start=start, end=end))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=DRUM_HI_HAT, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
