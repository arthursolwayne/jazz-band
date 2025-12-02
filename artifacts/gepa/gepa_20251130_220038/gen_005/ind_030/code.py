
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line in Fm (F, Gb, Ab, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords on 2 and 4
# Fm7 = F, Ab, Bb, Db
# Bbm7 = Bb, Db, F, Ab
# Fm7 on beat 2 (1.875-2.25)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Db
    # Bbm7 on beat 4 (3.0-3.375)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),   # Db
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # Ab
    # Fm7 again on beat 2 (4.875-5.25)
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Db
]
piano.notes.extend(piano_notes)

# Little Ray on drums - continue from bar 1
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    start_time = 1.5 + i * 0.375
    end_time = start_time + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=end_time))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start_time, end=end_time))  # Snare
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=end_time))  # Hihat

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    start_time = 3.0 + i * 0.375
    end_time = start_time + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=end_time))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start_time, end=end_time))  # Snare
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=end_time))  # Hihat

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    start_time = 4.5 + i * 0.375
    end_time = start_time + 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=end_time))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start_time, end=end_time))  # Snare
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=end_time))  # Hihat

# Dante on sax - short motif that sings, starts on bar 2
# Fm scale: F, Gb, Ab, Bb, C, Db, Eb
# Motif: F, Ab, Bb, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
