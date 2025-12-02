
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
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875)),  # D
    (pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25)), # Eb
    (pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625)), # E
    (pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0)),  # G
    (pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375)),  # A
    (pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75)), # Bb
    (pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125)), # B
    (pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5)),  # D
    (pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875)),  # Eb
    (pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25)), # E
    (pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625)), # G
    (pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0)),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# Dm7 = D F A C
# Comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),

    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),

    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Little Ray: Full kit for all bars 2-4
# Kick on 1 and 3
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))

# Snare on 2 and 4
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))

# Hi-hat on every eighth
for i in range(2, 4):
    for j in range(0, 4):
        start = i * 1.5 + j * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Dante: Short motif, make it sing.
# Dm scale: D, Eb, E, F, G, A, Bb, B
# D, Eb, E, D

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.0),   # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),   # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.0),   # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.125),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
