
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
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=1.625, end=1.75))  # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=1.875))  # G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0))  # G#

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.75))

# Sax: Motif - start it, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75))  # B
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875))  # C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0))  # D

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.125))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=3.125, end=3.25))  # A#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.375))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5))  # C

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.25))

# Sax: Continue motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=73, start=3.0, end=3.125))  # D#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=75, start=3.125, end=3.25))  # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.375))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.5))  # G

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.625))  # C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.625, end=4.75))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=4.875))  # D#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.0))  # E

# Piano: 7th chords, comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75))  # F7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.75))

# Sax: Finish the motif with a question
sax.notes.append(pretty_midi.Note(velocity=110, pitch=79, start=4.5, end=4.625))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=81, start=4.625, end=4.75))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=83, start=4.75, end=4.875))  # B
sax.notes.append(pretty_midi.Note(velocity=110, pitch=85, start=4.875, end=5.0))  # C

# Drums: Kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125))

# Hi-hat on every eighth
for i in range(10, 14):
    start = i * 0.375 + 4.5
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
