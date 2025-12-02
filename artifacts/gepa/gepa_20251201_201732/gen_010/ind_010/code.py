
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # F#2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0)   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # D5

    # Bar 3 (3.0 - 4.5s) - G7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # F5

    # Bar 4 (4.5 - 6.0s) - Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F4 (65) -> D4 (62) -> F4 (65), then resolve to G4 (67) on the last bar
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25),

    # Bar 3 (3.0 - 4.5s) - leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75),

    # Bar 4 (4.5 - 6.0s) - resolve to G4 (67)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25)
]

# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
])

# Hihat on every eighth
for start in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
