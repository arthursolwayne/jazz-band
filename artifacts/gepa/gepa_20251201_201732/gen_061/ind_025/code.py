
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
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, C, Ab, D) -> chromatic approach to F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75))  # Eb (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=1.75, end=2.0))  # F (root)

# Bar 3: Bb7 (Bb, F, D, Ab) -> chromatic approach to Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25))  # A (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5))  # Bb (root)

# Bar 4: Eb7 (Eb, Bb, G, Db) -> chromatic approach to Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=2.5, end=2.75))  # D (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0))  # Eb (root)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0))  # D

# Bar 3: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5))  # Ab

# Bar 4: Eb7 (Eb, G, Bb, Db)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=3.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0))  # Db

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (sax in Bb instrument, so F is D, Ab is F, Bb is G, F is D again)
# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))  # D (F in Fm)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=2.0))  # F (Ab)

# Bar 3: Leave it hanging — don't resolve yet
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25))  # G (Bb)

# Bar 4: Finish it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75))  # D (F)

# Drums: Bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25))

# Hi-hat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
