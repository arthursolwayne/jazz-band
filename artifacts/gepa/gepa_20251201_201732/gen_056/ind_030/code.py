
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

# Drums in Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0), # D2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375), # D2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5), # D2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875), # D2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0), # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane)
# Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7b5 (D, F, Ab, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C5
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375), # F5
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # E4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # B4
]
piano.notes.extend(piano_notes)

# Drums in Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375), # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax (Dante) - Melody: haunting, incomplete, one motif that lingers
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # G4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # G4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125), # D4
    pretty_midi.Note(velocity=100, pitch=66, start=5.8125, end=6.0), # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
