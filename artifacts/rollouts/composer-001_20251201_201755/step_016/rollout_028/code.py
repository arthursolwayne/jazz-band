
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

# Bass: Walking line in Fm (F2 - Ab2 - D2 - G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=54, start=1.875, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=3.0),  # D2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75), # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),  # Ab2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=2.0),  # Db4 (Ab3)
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.5),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F (Ab) (Bb) -> leave it hanging on Bb
# Repeat with a variation
sax_notes = [
    # First motif (Bar 2)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=2.0),   # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),   # Bb4
    # Second motif (Bar 3)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),   # Eb4 (chromatic)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),   # Bb4
    # Final motif (Bar 4)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=61, start=4.75, end=5.0),   # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),   # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),   # Bb4 (hold)
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),   # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
