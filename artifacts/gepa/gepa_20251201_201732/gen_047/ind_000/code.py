
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F minor, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # D2
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375), # E2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # D2
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, each bar a different chord
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25), # C4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # E4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0), # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=3.0), # Ab4
])
# Bar 4: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75), # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75), # C4
])
# Bar 4 resolution: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5), # B4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5), # F4
])
piano.notes.extend(piano_notes)

# Saxophone (Dante) - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0), # F4
]
sax.notes.extend(sax_notes)

# Drums: continue for Bars 2-4
# Bar 2: Kick on 1, Snare on 2, Kick on 3, Snare on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    # Bar 3: Kick on 1, Snare on 2, Kick on 3, Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    # Bar 4: Kick on 1, Snare on 2, Kick on 3, Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
# Hihat on every eighth note
for i in range(0, 6):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
