
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> D2 chromatic up to E2 (40)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=39, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=40, start=2.0, end=2.25),
    # Bar 3: A2 (45) -> A2 chromatic up to B2 (47)
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),
    # Bar 4: D2 (38) -> D2 chromatic up to E2 (40)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=39, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=40, start=3.5, end=3.75),
]
bass.notes.extend(bass_notes)

# Diane: Piano, open voicings, different chord each bar, resolve on the last
# Bar 2: Gmaj7 (G4, B4, D4, F#4) -> resolve to D
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # F#4
    # Bar 3: D7 (D4, F#4, A4, C#4) -> resolve to G
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # C#4
    # Bar 4: Gmaj7 (G4, B4, D4, F#4) -> resolve to D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # F#4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5-2.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
]
# Bar 3 (2.25-2.75s)
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),
]
# Bar 4 (3.0-3.5s)
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish it
# Motif: D4 (62) -> E4 (64) -> F#4 (67) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
