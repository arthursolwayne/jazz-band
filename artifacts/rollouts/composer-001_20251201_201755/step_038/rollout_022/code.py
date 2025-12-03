
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # G#2 (chromatic approach to A2) on & of 1
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.0625),
    # A2 (fifth) on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.375),
    # Bb2 (chromatic approach to Bb2) on & of 2
    pretty_midi.Note(velocity=80, pitch=58, start=2.375, end=2.5625),
    # F2 (root) on beat 3
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.875),
    # G#2 (chromatic approach to A2) on & of 3
    pretty_midi.Note(velocity=80, pitch=55, start=2.875, end=3.0625),
    # A2 (fifth) on beat 4
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),
    # Bb2 (chromatic approach to Bb2) on & of 4
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.5625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.375),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.375),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.375),  # Ab4
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.875),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.875),  # G5
    pretty_midi.Note(velocity=100, pitch=83, start=2.5, end=2.875),  # B5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - Bb (68) - C (72) - F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=2.5, end=2.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.0),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (4.5 - 6.0s)
# Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),
    # G#2 (chromatic approach to A2) on & of 1
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.0625),
    # A2 (fifth) on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.375),
    # Bb2 (chromatic approach to Bb2) on & of 2
    pretty_midi.Note(velocity=80, pitch=58, start=5.375, end=5.5625),
    # F2 (root) on beat 3
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.875),
    # G#2 (chromatic approach to A2) on & of 3
    pretty_midi.Note(velocity=80, pitch=55, start=5.875, end=6.0625),
    # A2 (fifth) on beat 4
    pretty_midi.Note(velocity=90, pitch=57, start=6.0, end=6.375),
    # Bb2 (chromatic approach to Bb2) on & of 4
    pretty_midi.Note(velocity=80, pitch=58, start=6.375, end=6.5625),
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
# Resolve on the last chord
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E5
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
# Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
