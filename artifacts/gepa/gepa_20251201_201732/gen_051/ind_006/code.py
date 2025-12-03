
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2 chord: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Gm7 (Bb, D, G, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),   # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (Bb, D, G, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Motif continues, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Cm7 (Eb, G, C, E)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # Db2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # C2
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (Eb, G, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # E5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),  # Snare on 2
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
