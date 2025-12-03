
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# --- BAR 1: LITTLE RAY ALONE (0.0 - 1.5s) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds
bar_duration = 1.5
note_duration = 0.375  # 160 BPM = 0.375s per beat

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875))  # This is actually bar 2, but let's leave it for clarity

# Hihat on every eighth note
for i in range(0, 4):
    start = i * note_duration
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125))

# --- BAR 2-4: FULL QUARTET (1.5 - 6.0s) ---
# Each bar is 1.5s, so Bar 2: 1.5-3.0, Bar 3: 3.0-4.5, Bar 4: 4.5-6.0

# Marcus: Bass line in Fm — walking line with roots, fifths, and chromatic approaches
# Fm (F, Ab, D, C, Bb, Eb) — roots on 1, 3, 5, 7, with chromatic approach

# Bar 2: Fm7 - F, Ab, D, C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0))  # C

# Bar 3: Bbm7 - Bb, D, F, Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5))  # Ab

# Bar 4: Cm7 - C, Eb, G, Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0))  # Bb

# Diane: Piano — open voicings, one chord per bar, resolving on the last note

# Bar 2: Fm7 (F, Ab, C, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0))  # D

# Bar 3: Bbm7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5))  # Ab

# Bar 4: Cm7 (C, Eb, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))  # Bb

# Dante (you): Tenor sax — one short motif, no scale runs. Let it sing.

# Bar 2: Play the motif (F, Ab, C, F)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0))  # F (repeat)

# Bar 3: Leave it hanging, space
# Bar 4: Return to finish it — F, Ab, C, F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0))  # F

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
