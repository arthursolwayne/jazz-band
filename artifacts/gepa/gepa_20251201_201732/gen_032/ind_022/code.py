
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> G (43) -> F# (44) -> G (43)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),
    # Bar 3: C (40) -> D (45) -> C# (46) -> D (45)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),
    # Bar 4: G (43) -> A (47) -> G# (48) -> A (47)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # E
    # Bar 3: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (66) -> Bb (62) -> C (67) -> F (66)
# Use 1.5s (start of bar 2) to 2.25s, then leave it hanging, then return at 4.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),
]
for note in sax_notes:
    sax.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),
]

# Bar 3 (3.0 - 4.5)
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
]

# Bar 4 (4.5 - 6.0)
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),
]

for note in drum_notes_bar2 + drum_notes_bar3 + drum_notes_bar4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
