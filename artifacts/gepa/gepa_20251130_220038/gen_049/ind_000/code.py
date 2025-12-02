
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # D7 (B)
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # D7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # D7 (C)
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),  # D7 (A)
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # D7 (B)
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # D7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # D7 (C)
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),  # D7 (A)
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
])

# Sax (Dante): Melody that feels like a whisper and a cry
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
