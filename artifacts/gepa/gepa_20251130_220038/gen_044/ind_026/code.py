
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
# Dm7 chord: D F A C
# Walking bass line: D, F#, E, F, G, Ab, G, A, Bb, B, C, Db, C, D

bass_notes = [
    (1.5, 50),  # D
    (1.875, 62),  # F#
    (2.25, 59),  # E
    (2.625, 60),  # F
    (3.0, 62),  # G
    (3.375, 60),  # Ab
    (3.75, 62),  # G
    (4.125, 65),  # A
    (4.5, 61),  # Bb
    (4.875, 63),  # B
    (5.25, 64),  # C
    (5.625, 61),  # Db
    (6.0, 64)   # C
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
# Dm7 chord: D F A C
# Comp on 2 and 4

# Bar 2: 2nd beat
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375))  # D

# Bar 3: 2nd beat
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875))  # D

# Bar 4: 2nd beat
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375))  # D

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.

# Melody in Dm: D, F, G, A, Bb, C, D

# Bar 2: Start with a whisper
sax.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=1.75, end=2.0))  # F
sax.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=2.0, end=2.25))  # G
sax.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5))  # A

# Bar 3: Build tension
sax.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.5))  # C
sax.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75))  # Bb

# Bar 4: Resolution
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0))  # C

# Drums: Bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625))

# Hi-hat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
