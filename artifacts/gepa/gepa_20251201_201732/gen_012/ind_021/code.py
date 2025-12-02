
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
    # Hihats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: All instruments enter
# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # F#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (open voicing)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=2.0),  # D5
]
# Bar 3: Bm7 (open voicing)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.5),  # B3
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.5),  # E4
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.5),  # A4
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.5),  # C5
])
# Bar 4: G7 (open voicing)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=3.0),  # C5
    pretty_midi.Note(velocity=80, pitch=74, start=2.5, end=3.0),  # D5
    pretty_midi.Note(velocity=80, pitch=79, start=2.5, end=3.0),  # F#5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, sing it, leave it hanging
# Motif: D4 - F#4 - G4 - E4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),   # E4
    # Repeat the motif again, ending with a resolution on D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),
    # Hihats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=5.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),
    # Hihats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.8125, end=5.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Bass line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),   # G2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # F2
]
bass.notes.extend(bass_notes)

# Bar 4: Piano resolves on D7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=4.0),  # D4
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=4.0),  # C5
    pretty_midi.Note(velocity=80, pitch=74, start=3.5, end=4.0),  # D5
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_moment.mid")
