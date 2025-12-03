
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bar 2: Full band enters
# Bass - walking line with chromatic approach to Dm7
bass_notes = [
    # Bar 2: D -> C -> D -> F
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=80, pitch=37, start=1.625, end=1.75),  # C2
    pretty_midi.Note(velocity=80, pitch=38, start=1.75, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano - open voicings, Dm7 (D, F, A, C) with Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # E5
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # F5
]
piano.notes.extend(piano_notes)

# Sax - motif: D4 (quarter), E4 (eighth), F4 (eighth), rest (quarter)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.25),
]
sax.notes.extend(sax_notes)

# Bar 3: Full band
# Bass - F -> E -> F -> A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.375),  # F2
    pretty_midi.Note(velocity=80, pitch=39, start=2.375, end=2.5),  # E2
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.625),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),  # A2
]
bass.notes.extend(bass_notes)

# Piano - Gm7 (G, Bb, D, F) with chromatic passing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # E5
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75),  # Bb5
]
piano.notes.extend(piano_notes)

# Sax - motif variation: G4 (quarter), rest (eighth), A4 (eighth), rest (quarter)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.75),
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875),
]
sax.notes.extend(sax_notes)

# Bar 4: Full band
# Bass - A -> G -> A -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),  # A2
    pretty_midi.Note(velocity=80, pitch=40, start=2.875, end=3.0),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),  # A2
    pretty_midi.Note(velocity=80, pitch=44, start=3.125, end=3.25),  # C3
]
bass.notes.extend(bass_notes)

# Piano - Cm7 (C, Eb, G, Bb) with tension
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.75, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # Ab5
]
piano.notes.extend(piano_notes)

# Sax - motif completion: C5 (quarter), rest (eighth), D5 (eighth), open
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.25),
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.375),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
