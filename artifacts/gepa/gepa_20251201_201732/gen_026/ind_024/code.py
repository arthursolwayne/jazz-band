
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F# diminished chord over Dm for color)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Bb4
]
# Bar 3: Dm7 -> Gm7 (chromatic passing chord)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
])
# Bar 4: Gm7 (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # F5
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Eb, F, G -> D, G, F, Eb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=63, start=1.6875, end=1.875),  # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.8125, end=3.0),  # G4
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue the same pattern
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (Bb diminished chord over Gm for color)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F5
]
# Bar 4: Gm7 -> Cm7 (chromatic passing chord)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # F5
])
# Bar 4: Cm7 (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A4
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax, continue motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.1875),  # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.5625),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.9375, end=4.125),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.3125),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=4.3125, end=4.5),  # Eb4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums continue the same pattern
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (Bb diminished chord over Cm for color)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, continue motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.6875),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0625),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=5.4375, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.8125),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.8125, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
