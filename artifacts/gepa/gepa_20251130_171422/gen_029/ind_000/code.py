
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
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody begins with a sparse, emotional motif

# Sax: F (65) -> Bb (62) -> Eb (60) -> B (67)
# Dynamic: soft to medium
sax.notes.append(pretty_midi.Note(velocity=60, pitch=65, start=1.5, end=1.625))  # F
sax.notes.append(pretty_midi.Note(velocity=70, pitch=62, start=1.625, end=1.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=65, pitch=60, start=1.75, end=1.875))  # Eb
sax.notes.append(pretty_midi.Note(velocity=75, pitch=67, start=1.875, end=2.0))  # B

# Bass: walking line, chromatic approaches
# F (65) -> Gb (66) -> G (67) -> A (69)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.625))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=66, start=1.625, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=1.75, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=1.875, end=2.0))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 (F, A, C, Eb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=68, start=1.5, end=1.75))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75))  # C
piano.notes.append(pretty_midi.Note(velocity=75, pitch=62, start=1.5, end=1.75))  # Eb

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif, with a slight variation
# F (65) -> Bb (62) -> Eb (60) -> F (65)
sax.notes.append(pretty_midi.Note(velocity=60, pitch=65, start=3.0, end=3.125))  # F
sax.notes.append(pretty_midi.Note(velocity=70, pitch=62, start=3.125, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=65, pitch=60, start=3.25, end=3.375))  # Eb
sax.notes.append(pretty_midi.Note(velocity=75, pitch=65, start=3.375, end=3.5))   # F

# Bass: walking line, chromatic approaches
# F (65) -> Gb (66) -> G (67) -> A (69)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.125))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=66, start=3.125, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=3.25, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=3.375, end=3.5))

# Piano: 7th chords, comp on 2 and 4
# Bar 3: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25))  # Bb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.25))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25))  # F
piano.notes.append(pretty_midi.Note(velocity=75, pitch=64, start=3.0, end=3.25))  # Ab

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: final variation, leaving it hanging
# F (65) -> Bb (62) -> Eb (60) -> rest
sax.notes.append(pretty_midi.Note(velocity=60, pitch=65, start=4.5, end=4.625))  # F
sax.notes.append(pretty_midi.Note(velocity=70, pitch=62, start=4.625, end=4.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=65, pitch=60, start=4.75, end=4.875))  # Eb

# Bass: walking line, chromatic approaches
# F (65) -> Gb (66) -> G (67) -> A (69)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.625))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=66, start=4.625, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=67, start=4.75, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=4.875, end=5.0))

# Piano: 7th chords, comp on 2 and 4
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75))  # Eb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=4.75))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75))  # Bb
piano.notes.append(pretty_midi.Note(velocity=75, pitch=58, start=4.5, end=4.75))  # Db

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 4):
    kick_start = 4.5 + i * 0.375
    kick_end = kick_start + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))

    snare_start = 4.5 + i * 0.375
    snare_end = snare_start + 0.125
    if i % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))

    hihat_start = 4.5 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
