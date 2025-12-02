
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
# Fm = F, Ab, C, D (lower root)
bass_notes = [
    # Bar 2: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    # Bar 2: Ab (fifth) with chromatic approach from G
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),
    # Bar 3: C (root) with chromatic approach from Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625),
    # Bar 3: Ab (fifth) with chromatic approach from G
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=3.0),
    # Bar 4: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    # Bar 4: C (root) with chromatic approach from Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),
    # Bar 4: F (root) again
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    # Bar 4: Ab (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),
]

bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, one chord per bar, resolve on last
# Fm: F, Ab, C, D (lower root)
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=2.25),
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=3.0),
    # Bar 4: Cm7
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),
]

piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F - Gb - Ab - A (ascending with tension)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
]

sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('f_minor_intro.mid')
