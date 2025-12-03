
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2: F (D2) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=60, pitch=37, start=1.5, end=1.6875),  # chromatic approach
    # Bar 3: C (D2) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=60, pitch=44, start=2.25, end=2.4375),  # chromatic approach
    # Bar 4: G (D2) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=60, pitch=39, start=3.0, end=3.1875),  # chromatic approach
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E♭)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # E♭
]
# Bar 3: B♭7 (B♭, D, F, A♭)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.75),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.75),  # A♭
]
# Bar 4: C7 (C, E, G, B♭)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # B♭
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax (Dante) - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (G4), B♭ (A4), C (B4), F (G4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # B♭
    pretty_midi.Note(velocity=110, pitch=79, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # F
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),  # F
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=76, start=2.75, end=3.0),  # B♭
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75)
]
# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes_bar2 + drum_notes_bar3 + drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
