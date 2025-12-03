
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2, MIDI 53 - 57), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    # F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),
    # Bb2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=56, start=2.5, end=2.75),
    # Bar 3 (3.0 - 4.5s)
    # F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.0),
    # Bb2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=56, start=4.0, end=4.25),
    # Bar 4 (4.5 - 6.0s)
    # F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.5),
    # Bb2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=56, start=5.5, end=5.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Eb5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Ab5
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # Bb5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - G4 - Ab4 - Bb4 (F, G, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=110, pitch=72, start=1.625, end=1.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # Bb4
    # Leave it hanging (rest)
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.125),  # F4 (repeat)
    pretty_midi.Note(velocity=110, pitch=72, start=2.125, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.375),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=2.375, end=2.5),  # Bb4
]
sax.notes.extend(sax_notes)

# Add more sax notes to finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.625),  # F4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Add more sax notes for the rest of the bars
# Bar 2: F - G - Ab - Bb (0.5 note each)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125),  # F4
    pretty_midi.Note(velocity=110, pitch=72, start=3.125, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 3: F - Bb - G - Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.625),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=3.625, end=3.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=3.875),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.875, end=4.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: F - G - Ab - Bb (repeat motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.125),  # F4
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.375),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=4.375, end=4.5),  # Bb4
]
sax.notes.extend(sax_notes)

# Add more sax notes for the rest of the bar
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625),  # F4
    pretty_midi.Note(velocity=110, pitch=72, start=4.625, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),  # Bb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
