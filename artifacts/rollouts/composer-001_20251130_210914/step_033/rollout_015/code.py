
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

# Bass: Walking line, chromatic approaches, no repeated notes
# Fm key: F, Gb, Ab, Bb, C, Db, Eb
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75), # Db
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, Db, F, Ab
# Ab7 = Ab, B, Eb, Gb
# Db7 = Db, F, Ab, Bb
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=85, pitch=61, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=85, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=85, pitch=57, start=1.5, end=1.875),  # Eb
    # Bar 3
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=59, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=85, pitch=61, start=3.0, end=3.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=85, pitch=61, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=85, pitch=63, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=85, pitch=57, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=85, pitch=63, start=4.5, end=4.875),  # Gb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, Bb, C, Db, Eb
# Motif: F - Gb - Ab - Bb (staccato) -> F - Ab - Bb - C (legato)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=63, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=110, pitch=61, start=2.5, end=2.75),   # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.5),    # C
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
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        start_time = start + (i * 0.1875)
        pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.1875)

drums.notes.extend([n for n in drums.notes if n.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
