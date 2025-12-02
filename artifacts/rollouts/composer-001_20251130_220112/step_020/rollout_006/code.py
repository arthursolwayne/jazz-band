
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

# Bass line - Marcus, walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Fm7 -> Bb7 -> Eb7 -> Ab7
    # Bass line: F, Gb, G, Ab, Bb, B, C, Db
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),   # Gb
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),   # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=3.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),    # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),   # B
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),   # C
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),    # Db
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),    # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25),    # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),    # B
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),     # C
]
bass.notes.extend(bass_notes)

# Piano - Diane, 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, Db), Bb7 (Bb, D, F, Ab), Eb7 (Eb, G, Bb, Db), Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),    # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),    # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),    # Db
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),    # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),    # D
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),    # F
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),    # Ab
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),    # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),    # G
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),    # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),    # Db
]
piano.notes.extend(piano_notes)

# Saxophone - Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, Db -> F, Ab, Bb, Db (octave up)
sax_notes = [
    # First motif
    pretty_midi.Note(velocity=110, pitch=45, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=2.0625, end=2.25), # Db
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=52, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.5625, end=3.75), # Db (octave up)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
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
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
