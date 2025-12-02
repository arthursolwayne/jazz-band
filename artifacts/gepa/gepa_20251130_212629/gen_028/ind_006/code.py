
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1, snare on 2, hihat on every eighth, but with subtle space

# Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
# Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
# Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5))

# BAR 2: Everyone in (1.5 - 3.0s)
# Sax: Start of the motif - a short, searching phrase

# Dm7 chord: D F A C
# Motif: D -> F -> A -> rest
# Rhythmic placement: D on beat 1, F on & of 1, A on 2, rest on & of 2

sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0))   # A
# Diane: Dm7 on beat 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0))  # F
# Marcus: walking line in Dm
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0))  # Eb
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875))  # Hihat
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0))

# BAR 3: Continue the motif, but with variation (3.0 - 4.5s)
# Sax: Repeat the motif but start on A, shift the rhythm

sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.125, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5))   # D
# Diane: Dm7 on beat 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5))  # F
# Marcus: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5))  # F
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375))  # Hihat
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5))

# BAR 4: End with a question (4.5 - 6.0s)
# Sax: End the motif with a rest on beat 2, leave it hanging

# Diane: Dm7 on beat 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75))  # F
# Marcus: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0))  # G
# Drums
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875))  # Hihat
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
