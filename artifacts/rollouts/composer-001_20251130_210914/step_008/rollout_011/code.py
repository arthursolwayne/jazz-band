
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

# Hihat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches, no repeated notes
# F7 chord: F A C E (F7 is F A C E flat? No, F7 is F A C E flat? Wait, F7 is F A C E flat? No, F7 is F A C E flat? Let's make it F Ab C Eb for F7 flat 9 or something. Let's stick with F7 for now.

# F7 chord: F, A, C, E
# Walking bass line: F -> Eb -> D -> C -> B -> A -> G -> F
# Then repeat the pattern with chromatic passes

# Bar 2 (1.5 - 3.0s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75))  # F (F3)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.5, end=2.75))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0))  # A

# Bar 3 (3.0 - 4.5s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.0))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=4.25, end=4.5))  # Bb

# Bar 4 (4.5 - 6.0s)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.75))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=56, start=5.0, end=5.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.5))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=54, start=5.5, end=5.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=5.75, end=6.0))  # C

# Piano (Diane): 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# F7 = F, A, C, Eb
# Bar 2 (1.5 - 3.0s) on beat 2 (2.25) and 4 (3.0)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.375))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.375))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.375))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.375))  # Eb

piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.125))

# Bar 3 (3.0 - 4.5s) on beat 2 (3.75) and 4 (4.5)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=3.875))

piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.625))

# Bar 4 (4.5 - 6.0s) on beat 2 (5.25) and 4 (6.0)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.375))

piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=6.0, end=6.125))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 scale: F, G, Ab, A, Bb, B, C, Db, D, Eb
# Motif: F, Ab, Bb, F (a small intervallic leap)

# First note: F (F4 = 71)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625))

# Second note: Ab (70)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.625, end=1.75))

# Third note: Bb (69)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875))

# Leave it hanging (no fourth note until bar 4 on beat 1)

# Finish the motif on beat 1 of bar 4 (4.5s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625))

# Drums continue in bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75))

# Hihat on every eighth note
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
