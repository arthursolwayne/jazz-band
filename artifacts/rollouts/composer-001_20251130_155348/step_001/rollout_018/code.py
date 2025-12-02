
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=35, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=36, start=2.25, end=2.5),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=34, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=90, pitch=35, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=33, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=34, start=3.75, end=4.0),  # Db
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=32, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=33, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=31, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=32, start=5.25, end=5.5),  # Bb
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Eb
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.25),  # Ab
    # Bar 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Eb
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + (i * 0.1875)
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
drums.notes.extend(drum_notes[0:8] * 3)

# Dante on tenor sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # Ab
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
