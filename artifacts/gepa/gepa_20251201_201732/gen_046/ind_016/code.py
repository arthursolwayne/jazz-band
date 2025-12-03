
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F root
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # D chromatic
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # C (fifth of Fm)
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),  # Gb (root + 3)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Melody - short motif, haunting, incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: Continuation of the motif, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Completes the motif, resolves with a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
]
drums.notes.extend(drum_notes)

# Hihat on every eighth
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.1875
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
