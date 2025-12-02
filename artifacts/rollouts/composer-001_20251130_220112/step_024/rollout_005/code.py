
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
    pretty_midi.Note(velocity=96, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=96, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=96, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=96, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D, F#, A, B (D7 chord)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # B4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=1.625, end=1.75),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=1.875),  # F#3
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # G3
]
bass.notes.extend(bass_notes)

# Piano: D7 chord on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # B4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: D, B, A, F# (chromatic approach to D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5),  # F#4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.125),  # A3
    pretty_midi.Note(velocity=80, pitch=50, start=3.125, end=3.25),  # G3
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.375),  # F#3
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.5),  # E3
]
bass.notes.extend(bass_notes)

# Piano: D7 chord on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.25),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # B4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: D, F#, A, B (D7 chord)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),  # B4
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.625),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=4.625, end=4.75),  # E3
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=4.875),  # F#3
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.0),  # G3
]
bass.notes.extend(bass_notes)

# Piano: D7 chord on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.5),  # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # A4
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # B4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=96, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=96, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=96, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=96, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth starting from 4.5
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
