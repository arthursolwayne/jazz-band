
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.1875),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=1.6875, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=1.6875, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.375, end=2.5625),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.375, end=2.5625),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.375, end=2.5625),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.375, end=2.5625),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full ensemble
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.1875, end=2.375), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5625), # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.1875),   # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.1875, end=2.375), # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=90, pitch=59, start=2.5625, end=2.75),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=2.1875, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.1875, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.1875, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.1875, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.875, end=3.0625),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.875, end=3.0625),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.875, end=3.0625),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.875, end=3.0625),  # F
]
piano.notes.extend(piano_notes)

# Drums: same pattern as bar 1, repeated
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Full ensemble
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.5625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=2.9375),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.9375, end=3.125),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=2.5625, end=2.75),   # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=2.9375),   # G#
    pretty_midi.Note(velocity=90, pitch=62, start=2.9375, end=3.125),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=3.125, end=3.3125),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=2.9375),   # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=2.9375),   # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=2.9375),   # D
    pretty_midi.Note(velocity=90, pitch=57, start=2.75, end=2.9375),   # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.3125, end=3.5),    # F
    pretty_midi.Note(velocity=90, pitch=53, start=3.3125, end=3.5),    # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.3125, end=3.5),    # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.3125, end=3.5),    # F
]
piano.notes.extend(piano_notes)

# Drums: same pattern as bar 1, repeated
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
