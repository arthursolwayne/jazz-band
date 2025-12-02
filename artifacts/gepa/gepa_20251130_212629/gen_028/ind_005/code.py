
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# --- Bar 1: Drums only (0.0 - 1.5 seconds) ---
# Tension, space, anticipation

# Kick on beat 1 and 3 (approx 0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.75, end=1.125))

# Snare on beat 2 and 4 (approx 0.375 and 1.125s)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=0.375, end=0.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=1.125, end=1.375))

# Hi-hat on every eighth note (approx 0.0, 0.375, 0.75, 1.125)
# But leave the space between the 2nd and 3rd eighth (0.375 to 0.75)
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.125, end=1.3125))

# --- Bar 2-4: Full quartet (1.5 - 6.0 seconds) ---

# Key: F major
# Mode: A Mixolydian (F major but with a bent, suspended feeling)
# Your motif: F - G - Bb - D - rest (a question, not a statement)

# Saxophone — your melody
# Start at 1.5s, each note lasts 0.375s (1/4 note)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25)) # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0))  # D
# Then a rest for the rest of the bar, but with a slight syncopation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.1875))  # F (early entrance)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.1875, end=3.375)) # D (followed by rest)

# Bass line (Marcus) — walking line with chromatic approach
# F - Gb - G - A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875))   # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25))  # Gb (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0))   # A
# Then back to F, with a subtle chromatic step
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375))    # F

# Piano (Diane) — 7th chords, comp on 2 and 4
# F7 on beat 2 and 4
# F7 = F, A, C, Eb
# A7 = A, C#, E, G (but we'll use a 7th chord on D for contrast)

# Bar 2: F7 on 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25))  # Eb

# Bar 3: D7 on 2 (subtle harmonic twist)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0))   # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.625, end=3.0))   # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0))   # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0))   # C

# Bar 4: F7 on 4 — ends the intro with a question
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75))  # Eb

# Drums — Bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=3.0, end=3.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=1.875, end=2.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=3.375, end=3.625))

# Hi-hat on every eighth
# But with a slight space between the second and third eighth notes (1.875-2.25)
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.5, end=1.6875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.875, end=2.0625))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=2.25, end=2.4375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=2.625, end=2.8125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=3.0, end=3.1875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=3.375, end=3.5625))

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
