
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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in F, roots and fifths with chromatic approaches
# Bass line: F -> E -> F -> G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625))  # F2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.75))  # E2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875))  # F2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0))   # G2

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb) with root in the left hand
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=2.0))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.0))  # C5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=2.0))  # Eb4

# Bar 3: Bb7 (Bb D F Ab)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.5))  # F5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=75, start=2.0, end=2.5))  # Ab4

# Bar 4: Eb7 (Eb G Bb Db)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=3.0))  # Db4

# Dante: Saxophone (tenor) - one short motif, make it sing
# Start with a Bb (Bb4) on beat 1, rest on beat 2, wrap around to F (F4) on beat 3, rest on beat 4

sax.notes.append(pretty_midi.Note(velocity=110, pitch=81, start=1.5, end=1.625))  # Bb4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.375))  # F4

# Drums for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=1.875 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=2.875 + 0.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=3.875 + 0.125))

# Hi-hat on every eighth
for i in range(6):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Add more hi-hats in bar 4
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
