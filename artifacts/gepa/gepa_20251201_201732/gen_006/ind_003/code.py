
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: Fm (F, C, Eb)
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F (1)
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.25), # C (2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # Eb (3)
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # D (approach to F)
    # Bar 3: Bb7 (Bb, F, Ab)
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Bb (1)
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # F (2)
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125), # Ab (3)
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # G (approach to Bb)
    # Bar 4: Ebm7 (Eb, Bb, Db)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # Eb (1)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # Bb (2)
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Db (3)
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # C (approach to Eb)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # Ab
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Ab
    # Bar 4: Ebm7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # Db
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - Eb - F (Fm triad with a twist)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=41, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=43, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.375),  # F (return)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
