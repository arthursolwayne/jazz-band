
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),    # Hi-hat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),   # Hi-hat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),    # Hi-hat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),    # Hi-hat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line (roots and fifths with chromatic approaches)
# F7 (F, C, Bb, E) -> Bb7 (Bb, F, Eb, Ab) -> Eb7 (Eb, Bb, Ab, Db) -> Ab7 (Ab, Eb, Db, Gb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),    # F (root)
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),   # C (fifth)
    pretty_midi.Note(velocity=80, pitch=75, start=2.25, end=2.625),   # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),    # E (3rd)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),    # Bb (root)
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),   # F (fifth)
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),   # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5),    # Ab (3rd)
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),    # Eb (root)
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),   # Bb (fifth)
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),   # Ab (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),    # Db (3rd)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),    # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),    # E
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.25),    # A
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=2.25),    # F

    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),    # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),    # Ab
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=3.0),    # D
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=3.0),    # Bb

    # Bar 4: Eb7
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),    # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),    # Db
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.75),    # G
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75),    # Eb

    # Bar 4 resolve: F7
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),    # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.5),    # E
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.5),    # A
    pretty_midi.Note(velocity=100, pitch=87, start=3.75, end=4.5),    # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (first two bars), then resolution in the last bar
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=87, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=110, pitch=84, start=1.875, end=2.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=89, start=2.25, end=2.625),   # C
    pretty_midi.Note(velocity=110, pitch=87, start=2.625, end=3.0),    # F

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=87, start=3.0, end=3.375),    # F
    pretty_midi.Note(velocity=110, pitch=84, start=3.375, end=3.75),   # Bb
    pretty_midi.Note(velocity=110, pitch=89, start=3.75, end=4.125),   # C

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=87, start=4.125, end=4.5),    # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hi-hat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hi-hat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hi-hat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
