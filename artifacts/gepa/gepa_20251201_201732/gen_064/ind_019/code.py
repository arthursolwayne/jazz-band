
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2 - C3, MIDI 53 - 60), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on 1
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    # G2 (fifth) on 2
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),
    # E2 (chromatic approach) on 3
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),
    # F2 (root) on 4
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # E
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Bb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - G (67) - E (64) - F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75),  # F
]
sax.notes.extend(sax_notes)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
# midi.write disabled
