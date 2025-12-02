
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2, F (root) -> E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),
    # Bar 2, C (fifth) -> D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=54, start=2.625, end=3.0),
    # Bar 3, F (root) -> E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75),
    # Bar 3, C (fifth) -> D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=54, start=4.125, end=4.5),
    # Bar 4, F (root) -> E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25),
    # Bar 4, C (fifth) -> D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=54, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # E
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Ab
])

# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # B
])

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2, 1st note: F (60)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),
    # Bar 2, 2nd note: A (65)
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),
    # Bar 3, 1st note: F (60)
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),
    # Bar 3, 2nd note: A (65)
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),
    # Bar 4, 1st note: F (60)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),
    # Bar 4, 2nd note: A (65)
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),
    # Bar 4, 3rd note: G (67)
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
