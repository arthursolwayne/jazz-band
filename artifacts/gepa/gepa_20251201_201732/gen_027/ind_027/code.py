
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
drums_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),      # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Ab

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: Open voicings, different chord each bar, resolve on the last.
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C

    # Bar 3 (3.0 - 4.5s): Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Ab

    # Bar 4 (4.5 - 6.0s): Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # Bb

    # Bar 3 (3.0 - 4.5s) - leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # Ab

    # Bar 4 (4.5 - 6.0s) - come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
drums_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),      # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),      # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),      # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]

for note in drums_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
