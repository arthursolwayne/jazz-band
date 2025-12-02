
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

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=39, start=1.5, end=1.875),  # Fm7 - F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Gb - chromatic
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # G - up a half step
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # E - root movement
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F (root)
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),  # Bb (7th)
    pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=2.25),  # Eb (3rd)
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),  # Ab (5th)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.0),  # Ab
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=85, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=85, pitch=69, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=85, pitch=64, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.5),  # Ab
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=64, start=5.625, end=6.0),  # Eb
    pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=6.0),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm (F, Ab, Bb, Db) — motif: F -> Ab -> Bb -> F

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F (Fm7)
    pretty_midi.Note(velocity=105, pitch=68, start=1.75, end=2.0),  # Ab (Ab9)
    pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.25),  # Bb (Bb7)
    pretty_midi.Note(velocity=105, pitch=67, start=2.25, end=2.5),  # Db (Db7)
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=105, pitch=67, start=3.75, end=4.0),  # Db
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=105, pitch=67, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=6.0),  # F (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
