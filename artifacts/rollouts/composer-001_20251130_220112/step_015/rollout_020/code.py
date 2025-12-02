
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # D#
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # B7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # A7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D7
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # G7
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # B7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # B7
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # D7
]
piano.notes.extend(piano_notes)

# Sax: Dante
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),   # B
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.6875),  # Hihat on 4

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
