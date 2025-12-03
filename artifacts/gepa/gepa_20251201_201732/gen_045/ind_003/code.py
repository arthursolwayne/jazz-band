
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

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# Bass: C (Dm7 root) with chromatic approach from Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75))  # C (root)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=60, start=1.75, end=2.0))  # Bb (chromatic approach)

# Piano: Dm7 (D F A C) - open voicing, resolve on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=2.0))  # C

# Sax: start the motif (Dm7 melody, incomplete)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0))  # F

# Bar 3 (3.0 - 4.5s)
# Bass: F (Dm7 3rd) with chromatic approach from E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25))  # F
bass.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=3.25, end=3.5))  # E

# Piano: Gm7 (G Bb D F) - open voicing, resolve on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.5))  # F

# Sax: continuation of the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0))  # F

# Bar 4 (4.5 - 6.0s)
# Bass: A (Dm7 5th) with chromatic approach from G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75))  # A
bass.notes.append(pretty_midi.Note(velocity=70, pitch=72, start=4.75, end=5.0))  # G

# Piano: Cm7 (C Eb G Bb) - open voicing, resolve on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=5.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=5.0))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=5.0))  # Bb

# Sax: finish the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0))  # F

# Drums: continue with kick, snare, hihat
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125))

# Hihat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
