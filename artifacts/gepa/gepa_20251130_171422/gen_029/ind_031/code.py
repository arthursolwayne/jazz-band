
import pretty_midi

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=160)]

# BAR 1: Little Ray (0.0 - 1.5s) — rhythmic tension, subtle dynamics
# Drums: build anticipation with space and energy

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=70, pitch=KICK, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=SNARE, start=1.875, end=2.0))  # Wait, this is outside bar 1, we'll fix it

# Hi-hats on every eighth
for i in range(0, 4):  # 4 eighth notes in a bar
    start = i * 0.375
    end = start + 0.125
    velocity = 90 if i % 2 == 0 else 85  # slight variation
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=HIHAT, start=start, end=end))

# Remove the snare note that's outside of bar 1
drums.notes = [note for note in drums.notes if note.start < 1.5]

# BAR 2-4: Full quartet (1.5 - 6.0s) — sax melody, chromatic bass, emotional piano

# Key: D minor (to give it a darker, moody vibe for emotional weight)
# Scale: D Dorian (D, E, F, G, A, B, C)

# SAX: Melodic motif — concise, emotional, memorable
# Start with a simple phrase: D - F - A - C (melodic minor feel)
# Phrase: D (0.0), F (0.375), A (0.75), C (1.125), then rest (1.5 to 2.0), resolve on G (2.0)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D (62)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25))  # F (64)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # A (67)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0))   # C (69)

# Then resolve on G (67)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))

# BASS: Chromatic walking line, active and melodic
# Bass line over D minor: D - C - B - A - G - F - E - D (chromatic descent)
# Start at 1.5s
notes = [62, 60, 59, 57, 55, 53, 52, 62]
for i, pitch in enumerate(notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end))

# PIANO: 7th chords, comp on 2 and 4 — emotional, not just rhythm
# Chords in D minor: Dm7 (D F A C), G7 (G B D F), Cm7 (C Eb G Bb), F7 (F A C E)
# Comp on 2 and 4 of each bar, with dynamic variation

# Bar 2: Dm7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.375))  # D
piano.notes.append(pretty_midi.Note(velocity=75, pitch=64, start=2.25, end=2.375))  # F
piano.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=65, pitch=69, start=2.25, end=2.375))  # C

# Bar 3: G7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125))  # G
piano.notes.append(pretty_midi.Note(velocity=75, pitch=71, start=3.0, end=3.125))  # B
piano.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.125))  # D
piano.notes.append(pretty_midi.Note(velocity=65, pitch=69, start=3.0, end=3.125))  # F

# Bar 4: Cm7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.875))  # C
piano.notes.append(pretty_midi.Note(velocity=75, pitch=64, start=3.75, end=3.875))  # Eb
piano.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=3.875))  # G
piano.notes.append(pretty_midi.Note(velocity=65, pitch=71, start=3.75, end=3.875))  # Bb

# Add a final chord on beat 4 (F7) to close the intro
piano.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.625))  # F
piano.notes.append(pretty_midi.Note(velocity=75, pitch=62, start=4.5, end=4.625))  # A
piano.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.625))  # C
piano.notes.append(pretty_midi.Note(velocity=65, pitch=69, start=4.5, end=4.625))  # E

# Add the instruments to the MIDI file
midi.instruments = [drums, sax, bass, piano]

# Save the MIDI file
midi.write("dante_russo_intro.mid")
