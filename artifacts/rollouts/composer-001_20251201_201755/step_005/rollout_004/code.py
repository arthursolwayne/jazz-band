
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 (F, C, Ab, D)
# Bar 3: Bb7 (Bb, F, D, Ab)
# Bar 4: Eb7 (Eb, Bb, G, Db)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Ab

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Db
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # D

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Ab

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (60), C (62), F (65)
# Play first two notes on bar 2, then pause, then play last two notes on bar 4
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # Ab

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
