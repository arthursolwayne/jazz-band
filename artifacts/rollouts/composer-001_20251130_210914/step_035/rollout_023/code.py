
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Fm7 bass
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    # Fm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=47, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=52, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=95, pitch=47, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=52, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # Db
    # Bar 3
    # Comp on 2 and 4
    pretty_midi.Note(velocity=85, pitch=46, start=2.625, end=2.8125),  # E
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=2.8125),  # Ab
    pretty_midi.Note(velocity=75, pitch=52, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=70, pitch=53, start=2.625, end=2.8125),  # Db
    pretty_midi.Note(velocity=85, pitch=44, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=75, pitch=50, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=70, pitch=52, start=3.375, end=3.5625),  # C
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=47, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=85, pitch=52, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=95, pitch=47, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=52, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),  # C
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # Bb
    # Bar 3 - come back and finish
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # Bb
    # Bar 4 - resolve
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.6875, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.4375, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
