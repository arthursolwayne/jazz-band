
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Saxophone: short motif starting on D (D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor (D, Eb, F, G)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=63, start=2.75, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (D7 on 2, G7 on 4)
piano_notes = [
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0)
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the motif and develop it (3.0 - 4.5s)
# Saxophone: repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5)
]
sax.notes.extend(sax_notes)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (D7 on 2, G7 on 4)
piano_notes = [
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=68, start=4.25, end=4.5)
]
piano.notes.extend(piano_notes)

# Bar 4: Final bar, resolve the motif (4.5 - 6.0s)
# Saxophone: resolve the motif on D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Bass: Finish walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=63, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Final 7th chord (D7 on 2)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0)
]
piano.notes.extend(piano_notes)

# Drums: Continue the pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
