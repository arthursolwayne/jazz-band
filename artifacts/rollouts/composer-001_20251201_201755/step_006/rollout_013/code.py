
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),  # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0),  # Gb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # Ab
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb
])

# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
])

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Ab
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # Bb
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F (G#) -> Ab -> C -> Bb -> F (G#) -> Ab -> C -> F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.6875),  # F (G#)
    pretty_midi.Note(velocity=110, pitch=50, start=1.6875, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0625),  # C
    pretty_midi.Note(velocity=110, pitch=57, start=2.0625, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.4375),  # F (G#)
    pretty_midi.Note(velocity=110, pitch=50, start=2.4375, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=110, pitch=53, start=2.8125, end=3.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
