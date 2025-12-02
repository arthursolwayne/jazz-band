
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125), # G#
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.875),  # F7 - A
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # F7 - Bb
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F7 - D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # F7 - F
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625), # F7 - A
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # F7 - Bb
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625), # F7 - D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # F7 - A
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # F7 - Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F7 - D
]
piano.notes.extend(piano_notes)

# Sax: Motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.6875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.6875, end=2.875), # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.9375), # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.9375, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.4375), # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.4375, end=4.625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=4.9375), # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.9375, end=5.125), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.4375, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),    # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),   # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 2
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
