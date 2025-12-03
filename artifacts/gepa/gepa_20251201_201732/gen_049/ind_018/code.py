
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
    # Bar 1: 0.0 - 1.5s
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: 1.5 - 3.0s
# Bass: F2 (MIDI 53) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=2.25, end=2.625),  # chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chords each bar
# Bar 2: F7sus4 (F, Bb, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: C7sus4 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: G7sus4 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Bar 2: 1.5 - 3.0s - short motif, incomplete
# F (53), Bb (60), G (67), rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
]
sax.notes.extend(sax_notes)

# Bar 3: 3.0 - 4.5s - drum fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s - sax returns with motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

# Bar 4: 4.5 - 6.0s - bass resolves
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=6.0),
]
bass.notes.extend(bass_notes)

# Bar 4: 4.5 - 6.0s - piano resolves on F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Bar 4: 4.5 - 6.0s - drum fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
