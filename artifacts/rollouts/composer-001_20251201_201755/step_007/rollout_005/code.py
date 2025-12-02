
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches and roots/fifths
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25))  # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0))  # G#

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0))  # E

# Sax: Start of motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0))  # F

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches and roots/fifths
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75))  # G#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5))  # A#

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B, D, F#, A)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=4.5))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5))  # A

# Sax: Continue motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5))  # F

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches and roots/fifths
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25))  # A#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0))  # B#

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Em7 (E, G, B, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0))  # D

# Sax: Finish motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0))  # F

# Drums: Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
