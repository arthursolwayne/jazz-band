
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F7 - C7 - Bb7 - E7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.25),  # C7
    pretty_midi.Note(velocity=100, pitch=83, start=2.25, end=2.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0)   # E7
]
sax.notes.extend(sax_notes)

# Bass: walking line in F (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F root
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with open voicings
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0),  # Ab
])
piano.notes.extend(piano_notes)

# Bar 3: Little Ray alone (3.0 - 4.5s)
# Repeat the same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif with a variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25),  # C7
    pretty_midi.Note(velocity=100, pitch=83, start=5.25, end=5.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0)   # E7
]
sax.notes.extend(sax_notes)

# Bass: Walking line again
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F root
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with open voicings
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # E
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
