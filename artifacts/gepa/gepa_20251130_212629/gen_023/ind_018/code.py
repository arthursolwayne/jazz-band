
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax melody starts
# Sax: 8th notes, one motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # F
]

sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=39, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=37, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=35, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=37, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=39, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # E
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # Bb

    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75), # C

    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=78, start=4.875, end=5.25), # F

    # Bar 4: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=80, pitch=79, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=80, pitch=80, start=5.625, end=6.0), # G
]

piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=80, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=80, pitch=38, start=start + 0.375, end=start + 0.75),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=start, end=start + 1.5),
    # Kick on 3
    pretty_midi.Note(velocity=80, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 4
    pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.5),

drums.notes.extend([
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
