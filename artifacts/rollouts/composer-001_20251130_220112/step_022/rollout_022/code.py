
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody
bar_length = 1.5

# Sax melody (Fm scale: F, Gb, Ab, A, Bb, C, Db)
# Motif: F (Ab) - Gb (Bb) - Ab (C) - A (Db) - Bb (F) - C (Gb) - Db (Ab)
# Start on F, end on Ab, leave it hanging

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375), # Db
    pretty_midi.Note(velocity=100, pitch=68, start=2.375, end=2.5),  # Ab (leave it hanging)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875), # Db
    pretty_midi.Note(velocity=100, pitch=68, start=3.875, end=4.0),  # Ab (leave it hanging)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.125, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375), # Db
    pretty_midi.Note(velocity=100, pitch=68, start=5.375, end=5.5),  # Ab (finish it)
]

sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice
# Fm7: F, Ab, Bb, Db
# Walking line: F, Gb, Ab, A, Bb, B, C, Db, D, Eb, F, Gb, Ab, A, Bb, B
# Bar 2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.125, end=2.25), # B
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5),  # Db
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),   # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.625, end=3.75), # Db
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=3.875, end=4.0),   # A
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.625, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),   # Db
    pretty_midi.Note(velocity=80, pitch=68, start=5.0, end=5.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=5.125, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.375, end=5.5),   # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, Db
# Bar 2
piano_notes = [
    # 2nd beat: Fm7
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),   # Db
    # 4th beat: Fm7
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # Db
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),   # Db
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.25),  # Db
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),   # Db
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=5.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.75),  # Db
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
