
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but bar ends at 1.5s, so skip)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38), F# (42) chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # chromatic
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # chromatic
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # G (43)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # chromatic
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),

    # Bar 3: A (45), C# (49) chromatic approach
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=2.875),  # chromatic
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=45, start=2.875, end=3.125),
    pretty_midi.Note(velocity=80, pitch=47, start=2.875, end=3.125),  # chromatic
    pretty_midi.Note(velocity=80, pitch=50, start=2.875, end=3.125),  # C# (50)
    pretty_midi.Note(velocity=80, pitch=45, start=3.125, end=3.375),
    pretty_midi.Note(velocity=80, pitch=47, start=3.125, end=3.375),  # chromatic
    pretty_midi.Note(velocity=80, pitch=49, start=3.125, end=3.375),

    # Bar 4: B (50), D (52) chromatic approach
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.625),  # chromatic
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=50, start=3.625, end=3.875),
    pretty_midi.Note(velocity=80, pitch=51, start=3.625, end=3.875),  # chromatic
    pretty_midi.Note(velocity=80, pitch=54, start=3.625, end=3.875),  # D (52) + chromatic
    pretty_midi.Note(velocity=80, pitch=50, start=3.875, end=4.125),
    pretty_midi.Note(velocity=80, pitch=51, start=3.875, end=4.125),  # chromatic
    pretty_midi.Note(velocity=80, pitch=52, start=3.875, end=4.125),
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: Open voicings, different chord each bar, resolve on the last
piano_notes = []

# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (62)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F# (67)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A (71)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C# (69)
])

# Bar 3: Am7 (A, C#, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875),  # A (71)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.875),  # C# (69)
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.875),  # E (74)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.875),  # G (72)
])

# Bar 4: Bm7 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.625),  # B (73)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.625),  # D (62)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.625),  # F# (67)
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.625),  # A (71)
])

for note in piano_notes:
    piano.notes.append(note)

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (67) -> A (71) -> D (62) -> F# (67) -> A (71) -> D (62)
# Start on bar 2, end on bar 4

sax_notes = [
    # Bar 2: D (62) on 1, F# (67) on 2, A (71) on 3
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
