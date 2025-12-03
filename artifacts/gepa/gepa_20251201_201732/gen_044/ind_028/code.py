
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (D), chromatic approach to G2 (G)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    # Bar 3: G2 (G), chromatic approach to A2 (A)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=2.875), # G2
    pretty_midi.Note(velocity=90, pitch=44, start=2.875, end=3.125), # Ab2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=45, start=3.125, end=3.5),  # A2
    # Bar 4: A2 (A), chromatic approach to D3 (D)
    pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.875),  # A2
    pretty_midi.Note(velocity=90, pitch=46, start=3.875, end=4.125), # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # C4
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F4
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=3.125, end=3.5),  # C#5
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.5),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.5),  # G4
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, G4, A4 -> D4, F4, G4, A4
# First pass: D4 (start), F4, G4, A4 (end)
# Second pass: D4, F4 (hanging), then back to D4, F4, G4, A4
sax_notes = [
    # First pass (bar 2)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75), # F4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=1.875), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),  # A4

    # Second pass (bar 4)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625), # D4
    pretty_midi.Note(velocity=110, pitch=64, start=3.625, end=3.75), # F4
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=3.875), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
