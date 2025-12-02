
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

# Hihat on every eighth
for i in range(0, 4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
# Bar 2: F -> Bb -> C -> Eb (Roots and fifths)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0))  # Eb

# Bar 3: Bb -> D -> Eb -> G (Roots and fifths)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.125))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=4.125, end=4.5))  # G

# Bar 4: C -> F -> G -> Bb (Roots and fifths)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=5.25, end=5.625))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0))  # Bb

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fmaj7 (F, A, C, E)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # E

# Bar 3: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375))  # Ab

# Bar 4: C7 (C, E, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875))  # Bb

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - E - D (with some space)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.6875))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=1.6875, end=1.875))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0625))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=2.0625, end=2.25))  # D

# End of motif, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.4375))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=2.4375, end=2.625))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.8125))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=2.8125, end=3.0))  # G

# Drums: Continue same pattern for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0))

# Hihat on every eighth
for i in range(4, 16):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
