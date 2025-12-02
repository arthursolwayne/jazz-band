
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
]
piano.notes.extend(piano_notes)

# Sax: motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),  # D
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=56, start=4.125, end=4.5),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Sax: continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375),
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax: resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
