
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax: short motif, D - F# - G - B (D7 chord)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F#
    # Bar 3: D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F#
    # Bar 4: D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F#
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, but end on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 3: D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F#
    # Bar 4: D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # F#
]
piano.notes.extend(piano_notes)

# Drums: continue kick, snare, hihat
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve motif, end on B
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # B
]
sax.notes.extend(sax_notes)

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 4: D7 on 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F#
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
