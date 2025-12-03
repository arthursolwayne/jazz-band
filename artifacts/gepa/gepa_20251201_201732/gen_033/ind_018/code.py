
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

# Bass line (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F, G, E, D
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2

    # Bar 3: Bb, A, G, F
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # F2

    # Bar 4: F, G, E, D
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # E2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    # Fm7: F, Ab, C, D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C2
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # D2

    # Bar 3: Bbmaj7
    # Bb, D, F, Ab
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # Ab2

    # Bar 4: Fm7
    # F, Ab, C, D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # D2
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante): One short motif, start it, leave it hanging, come back and finish it
# Motif: F, Ab, G, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F2
    pretty_midi.Note(velocity=110, pitch=55, start=1.625, end=1.75),  # Ab2
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=1.875),  # G2
    pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.0),  # F2

    # Let it hang
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.375),  # F2

    # Come back in bar 4
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.625),  # F2
    pretty_midi.Note(velocity=110, pitch=55, start=4.625, end=4.75),  # Ab2
    pretty_midi.Note(velocity=110, pitch=55, start=4.75, end=4.875),  # G2
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.0),  # F2
]

for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),

    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),

    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
