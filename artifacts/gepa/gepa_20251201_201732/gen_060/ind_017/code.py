
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
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))  # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25)) # E2 (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625)) # A2 (fifth of D)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0))  # G2

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0))  # F#4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0))  # C#5

# Bar 3: Gm7 (G-Bb-D-F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5))  # F5

# Bar 4: C7 (C-E-G-B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0))  # B4

# Dante: Tenor sax motif
# Short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif - D4 (D)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875))

# Bar 3: Continue motif - F#4 (F#), G4 (G)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625))

# Bar 4: Resolve back to D - D4 (D)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875))

# Bar 4: Add a chromatic lead-in to the final note
sax.notes.append(pretty_midi.Note(velocity=110, pitch=61, start=4.375, end=4.5))

# Drums continue in bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0))

# Hi-hat on every eighth
for i in range(4, 8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Add the final hi-hat on beat 4 of bar 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
