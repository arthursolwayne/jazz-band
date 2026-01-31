
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # E2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # F2 (chromatic)

    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # G2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # G#2 (chromatic)

    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # G#2 (root)
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25), # A#2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625), # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # B2 (chromatic)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25), # C5
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=2.25), # E5
]

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0), # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0), # F5
])

# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75), # B4
])

# Add Diane's resolving chord on the last beat of bar 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # B4
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 (71), A4 (74), F4 (71), rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
