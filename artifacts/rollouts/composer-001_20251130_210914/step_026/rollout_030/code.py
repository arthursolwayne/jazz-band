
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif starting on F (70)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.1875), # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=2.1875, end=2.375),# F
    pretty_midi.Note(velocity=80, pitch=49, start=2.375, end=2.5625),# G
    pretty_midi.Note(velocity=80, pitch=50, start=2.5625, end=2.75), # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, measure 2 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),
    # Bar 3, measure 4 (4th beat)
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif but end on a different note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=68, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=70, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=70, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=70, start=4.3125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bass: walking line continuation
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.1875, end=3.375),# F
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.5625),# G
    pretty_midi.Note(velocity=80, pitch=50, start=3.5625, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.9375, end=4.125),# F
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.3125),# G
    pretty_midi.Note(velocity=80, pitch=50, start=4.3125, end=4.5),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, measure 2 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),
    # Bar 4, measure 4 (4th beat)
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=4.3125, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),# Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=68, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=68, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=100, pitch=70, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=100, pitch=70, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Bass: walking line continuation
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.6875), # Ab
    pretty_midi.Note(velocity=80, pitch=52, start=4.6875, end=4.875),# Bb
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.0, end=5.1875), # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.1875, end=5.375),# Ab
    pretty_midi.Note(velocity=80, pitch=52, start=5.375, end=5.5625),# Bb
    pretty_midi.Note(velocity=80, pitch=47, start=5.5625, end=5.75), # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.75, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, measure 2 (2nd beat)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),
    # Bar 4, measure 4 (4th beat)
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
