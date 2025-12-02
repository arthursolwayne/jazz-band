
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=45, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=5.75, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2 - comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),

    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # F7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),

    # Bar 3 - comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),

    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # F7
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),

    # Bar 4 - comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),

    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # F7
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, make it sing
# Bar 2: F, Ab, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=73, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=1.875, end=2.0),  # D
]
# Bar 3: Repeat motif starting on 2
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.375))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=73, start=2.375, end=2.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=2.625))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=77, start=2.625, end=2.75))
# Bar 4: Repeat motif starting on 2
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=3.875))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=73, start=3.875, end=4.0))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=77, start=4.125, end=4.25))

sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
]
# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
])
# Hihat on every eighth
for t in [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]:
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1875))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
