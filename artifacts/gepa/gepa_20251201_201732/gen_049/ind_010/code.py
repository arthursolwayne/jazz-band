
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),   # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)     # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),     # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),    # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),    # G2
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),     # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # E4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),    # F2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),   # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),   # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),    # F2
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (B D# F# A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D#4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # A4
]
piano.notes.extend(piano_notes)

# Sax: continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # F4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),   # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)     # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),    # G2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),   # F2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),   # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),    # Eb2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # F4
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # C4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),    # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),   # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),   # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)     # hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
