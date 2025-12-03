
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> C#2 (chromatic approach) -> F2 (fifth) -> E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25), # C#2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # E2

    # Bar 3: A2 (root) -> G#2 (chromatic approach) -> D3 (fifth) -> C#3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # G#2
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # D3
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # C#3

    # Bar 4: G2 (root) -> F#2 (chromatic approach) -> C3 (fifth) -> B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # F#2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),  # B2
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, A, D (octave up)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),  # D5
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
