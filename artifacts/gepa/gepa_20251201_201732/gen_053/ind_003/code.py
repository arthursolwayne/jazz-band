
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
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i*0.375, end=i*0.375 + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, C, Ab, D)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75))  # F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=1.75, end=2.0))  # Ab2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=2.0, end=2.25))  # Bb2 (chromatic)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5))  # C2

# Bar 3: Bb7 (Bb, F, D, Ab)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75))  # Bb2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0))  # D2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25))  # Eb2 (chromatic)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5))  # F2

# Bar 4: Eb7 (Eb, Bb, G, D)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75))  # Eb2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=4.0, end=4.25))  # A2 (chromatic)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5))  # Bb2

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75))  # F2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75))  # C2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75))  # D2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.5, end=1.75))  # Eb2

# Bar 3: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75))  # Bb2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75))  # D2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75))  # F2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.75))  # Ab2

# Bar 4: Eb7 (Eb, G, Bb, D)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75))  # Eb2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75))  # G2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75))  # Bb2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75))  # D2

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))  # D3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))   # Eb3

# Bar 3: Leave it hanging
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75))  # Bb2

# Bar 4: Come back and finish it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75))  # D3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0))   # Eb3

# Drums: Bar 2-4
# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))   # Snare
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.1875))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875))  # Kick
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0))   # Snare
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=2.5 + i*0.375, end=2.5 + i*0.375 + 0.1875))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))  # Kick
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0))   # Snare
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.5 + i*0.375, end=3.5 + i*0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
