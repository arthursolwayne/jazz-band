
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

# Bass line (Marcus): walking line, roots and fifths with chromatic approaches
# Fm7: F, C, Ab, Db
# Bar 2: F, Gb, C, B
# Bar 3: Ab, A, Db, C
# Bar 4: F, Gb, C, B
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=46, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano (Diane): open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Db)
# Bar 3: Ab7 (Ab, C, Eb, Gb)
# Bar 4: Fm7 (F, Ab, C, Db)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=85, pitch=43, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=85, pitch=45, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=47, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=85, pitch=42, start=1.5, end=2.0),  # Db
    # Bar 3
    pretty_midi.Note(velocity=85, pitch=45, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=85, pitch=47, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=85, pitch=49, start=2.0, end=2.5),  # Eb
    pretty_midi.Note(velocity=85, pitch=42, start=2.0, end=2.5),  # Gb
    # Bar 4
    pretty_midi.Note(velocity=85, pitch=43, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=85, pitch=45, start=2.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=85, pitch=47, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=85, pitch=42, start=2.5, end=3.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C (Fm7), start on 1.5s, end on 2.0s, then repeat on 4.5s-5.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.0),  # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875),
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
