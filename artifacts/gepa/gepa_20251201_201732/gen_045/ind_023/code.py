
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2-G2, MIDI 38-43) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # B2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Cm7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # Eb4
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F4
    # Bar 4: Cm7 (F, A, C, Eb) again, resolving back
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # Eb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),   # F#2
]
bass.notes.extend(bass_notes)

# Piano: Continue open voicings
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F4
    # Bar 4: Cm7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # Eb4
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif in Bar 3 with slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),   # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums continue
# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # B2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0),   # F#2
]
bass.notes.extend(bass_notes)

# Piano: Continue open voicings
piano_notes = [
    # Bar 4: Cm7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),   # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # Eb4
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif in Bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),   # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
