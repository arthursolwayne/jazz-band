
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (Walking line, D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # E2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # E2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C4

    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4

    # Bar 4: C7 (C-E-G-B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # B4
]
piano.notes.extend(piano_notes)

# Drums: Little Ray (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Motif: D4 - F#4 - D5 - C5 (Motif starts at 1.5s, ends at 2.25s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # C5

    # Repeat motif with slight variation (resolve on D4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D4

    # Final resolution
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
