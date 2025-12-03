
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
    # Bar 1 - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), chromatic approach to G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0), # G2
    # Bar 3: G2 (root), chromatic approach to B2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375), # G2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # B2
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5), # B2
    # Bar 4: B2 (root), chromatic approach to D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875), # B2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25), # C3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.625), # D3
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=6.0), # D3
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # C4
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # F4
])
# Bar 4: B7 (B D# F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # B4
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875), # D#4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # F#4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # A4
])
piano.notes.extend(piano_notes)

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - E4 - F#4 - G4 (up a half step)
# First phrase: D4 - E4 - F#4 (Bar 2, first three eighth notes)
# Second phrase: G4 (Bar 3, first eighth note), then repeat motif in Bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # E4
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # E4
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0), # G4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
])
# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
