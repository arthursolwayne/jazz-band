
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
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice. D minor key.
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875)),   # D
    (pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25)),  # C
    (pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625)),  # D#
    (pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0)),   # E
    (pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375)),   # D
    (pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75)),  # C
    (pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125)),  # B
    (pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5)),   # D
    (pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875)),   # E
    (pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25)),  # F
    (pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625)),  # D
    (pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0)),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. D minor 7, F minor 7, B diminished 7, G minor 7
# Bar 2: D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875))

# Bar 3: F7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625))

# Bar 4: Bdim7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375))

# Bar 4: G7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875))

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: D minor motif (start)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))

# Bar 3: Rest (leave it hanging)
# Bar 4: Come back and finish it
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
