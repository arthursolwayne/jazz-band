
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line in Fm (F - Ab - D - C), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=70, pitch=44, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=70, pitch=50, start=1.875, end=2.25), # Ab2 (b3)
    pretty_midi.Note(velocity=70, pitch=51, start=2.25, end=2.625), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=52, start=2.625, end=3.0),  # D2 (5th)

    # Bar 3
    pretty_midi.Note(velocity=70, pitch=51, start=3.0, end=3.375),  # C2 (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=48, start=3.375, end=3.75), # F2 (root)
    pretty_midi.Note(velocity=70, pitch=53, start=3.75, end=4.125), # Eb2 (b7)
    pretty_midi.Note(velocity=70, pitch=53, start=4.125, end=4.5),  # Eb2 (b7)

    # Bar 4
    pretty_midi.Note(velocity=70, pitch=52, start=4.5, end=4.875),  # D2 (5th)
    pretty_midi.Note(velocity=70, pitch=51, start=4.875, end=5.25), # C2 (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=50, start=5.25, end=5.625), # Ab2 (b3)
    pretty_midi.Note(velocity=70, pitch=44, start=5.625, end=6.0),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Eb4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=75, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # Ab4
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=75, start=4.5, end=4.875),  # D5
])
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: G7 (G, B, D, F) -> Fm (F, Ab, C, Eb)
# Bar 2: Start with G in 3rd position (G4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=1.625, end=1.75), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=1.875), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F4 (sustain)
]
# Bar 3: Leave it hanging, no notes
# Bar 4: Finish the motif with a descending line F - Eb - D - C
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),   # C4
])
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
