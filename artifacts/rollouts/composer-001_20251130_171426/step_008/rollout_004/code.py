
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # B#
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D7 - F#
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75),  # D7 - D
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # D7 - F#
]
piano.notes.extend(piano_notes)

# Sax: motif with a question and a hook
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
