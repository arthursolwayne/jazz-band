
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.0),  # F7
    # Bar 3 - 2nd beat
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=2.875, end=3.0),  # F7
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 - first motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # C
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),    # D
    # Bar 4 - return and finish
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.5625, end=3.75), # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

# Bar 3: Bass (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
piano_notes = [
    # Bar 3 - 2nd beat
    pretty_midi.Note(velocity=80, pitch=64, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=3.875, end=4.0),  # F7
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # A
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes = [
    # Bar 4 - 2nd beat
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),  # F7
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.0625, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.4375), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.8125, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
