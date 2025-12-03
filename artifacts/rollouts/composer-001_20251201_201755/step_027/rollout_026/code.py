
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

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 to F#2 (root to fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # F#2
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2

    # Bar 3: A2 to C#2 (root to fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75), # B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # C#2
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # A2

    # Bar 4: B2 to D2 (root to fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25), # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # B2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, A, C#) -> D7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # F#4

    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # C#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # C#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # C#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # C#4

    # Bar 4: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # A4
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing
# Bar 2: Start with a motif (D4, F#4, A4, D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0),  # F#4
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
