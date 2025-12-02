
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
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.75)),    # Fm7: F, Ab, D, Eb
    (pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0)),   # Bb
    (pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25)),   # Ab
    (pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5)),   # G
    (pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75)),   # F
    (pretty_midi.Note(velocity=90, pitch=46, start=2.75, end=3.0)),   # Bb
    (pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.25)),   # B
    (pretty_midi.Note(velocity=90, pitch=45, start=3.25, end=3.5)),   # Ab
    (pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.75)),   # G
    (pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.0)),   # F
    (pretty_midi.Note(velocity=90, pitch=46, start=4.0, end=4.25)),   # Bb
    (pretty_midi.Note(velocity=90, pitch=47, start=4.25, end=4.5)),   # B
    (pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.75)),   # Ab
    (pretty_midi.Note(velocity=90, pitch=43, start=4.75, end=5.0)),   # G
    (pretty_midi.Note(velocity=90, pitch=44, start=5.0, end=5.25)),   # F
    (pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.5)),   # Bb
    (pretty_midi.Note(velocity=90, pitch=45, start=5.5, end=5.75)),   # Ab
    (pretty_midi.Note(velocity=90, pitch=43, start=5.75, end=6.0)),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Fm7 (F, Ab, D, Eb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.75))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75))  # Eb

# Bar 3: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.5))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5))  # Ab

# Bar 4: Fm7 again
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0))  # Eb

# Sax: Motif
# Bar 2: F (71) -> Ab (68) -> G (67) -> F (71)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=1.625, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0))  # Hang on the last note

# Bar 3: Let it rest
# Bar 4: Repeat the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=4.625, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0))

# Drums: Bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25))

# Hihat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
