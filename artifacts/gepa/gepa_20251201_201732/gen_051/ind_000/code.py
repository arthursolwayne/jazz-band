
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

# Marcus: Walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),   # E

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=37, start=4.125, end=4.5),   # E

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last.
# Fm7, Bbmaj7, Eb7, Am7
piano_notes = []
# Bar 2 (1.5 - 3.0s) - Fm7 (F, Ab, C, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=3.0),  # D
])

# Bar 3 (3.0 - 4.5s) - Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # Ab
])

# Bar 4 (4.5 - 6.0s) - Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),  # D
])

for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, G, D (MIDI 53, 51, 55, 56)
# Start on bar 2 (1.5s)
# First phrase: 1.5 - 2.125 (4 eighth notes)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=56, start=2.625, end=3.0),   # D

    # Second phrase: 4.5 - 5.125 (4 eighth notes)
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=51, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=56, start=5.625, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
