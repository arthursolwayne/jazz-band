
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # B2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # F3
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Ab5
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, G4, A4, C5 (F, G, A, C)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0),   # C5
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.5),   # C5
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 and 3
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
