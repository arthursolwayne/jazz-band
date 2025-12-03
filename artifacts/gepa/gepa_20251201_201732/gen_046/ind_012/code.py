
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

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0)

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 4):
    for j in range(0, 4):
        start = i * 0.375 + j * 0.375
        end = start + 0.125
        hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 -> Bbm7 -> Ebm7 -> Abm7
# Walking line with chromatic approaches, not scales
# Roots and fifths with chromatic approaches

# Bar 2 (1.5 - 3.0s): Fm7 (F, C, Ab, Db)
# Bass notes: F (D3), Ab (E3), G (F3), Eb (D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F (D3)
    pretty_midi.Note(velocity=85, pitch=55, start=1.75, end=2.0),  # Ab (E3)
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.25),  # G (F3)
    pretty_midi.Note(velocity=85, pitch=52, start=2.25, end=2.5),  # Eb (D3)
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # F (D3)
    pretty_midi.Note(velocity=85, pitch=55, start=2.75, end=3.0),  # Ab (E3)
]

# Bar 3 (3.0 - 4.5s): Bbm7 (Bb, F, Db, Ab)
# Bass notes: Bb (D#3), Db (F3), C (E3), Ab (G3)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=56, start=3.0, end=3.25),  # Bb (D#3)
    pretty_midi.Note(velocity=85, pitch=57, start=3.25, end=3.5),  # Db (F3)
    pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75),  # C (E3)
    pretty_midi.Note(velocity=85, pitch=60, start=3.75, end=4.0),  # Ab (G3)
    pretty_midi.Note(velocity=80, pitch=56, start=4.0, end=4.25),  # Bb (D#3)
    pretty_midi.Note(velocity=85, pitch=57, start=4.25, end=4.5),  # Db (F3)
])

# Bar 4 (4.5 - 6.0s): Ebm7 (Eb, Bb, Gb, Db)
# Bass notes: Eb (D3), Gb (F3), F (E3), Db (D3)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.75),  # Eb (D3)
    pretty_midi.Note(velocity=85, pitch=55, start=4.75, end=5.0),  # Gb (F3)
    pretty_midi.Note(velocity=80, pitch=57, start=5.0, end=5.25),  # F (E3)
    pretty_midi.Note(velocity=85, pitch=52, start=5.25, end=5.5),  # Db (D3)
    pretty_midi.Note(velocity=80, pitch=52, start=5.5, end=5.75),  # Eb (D3)
    pretty_midi.Note(velocity=85, pitch=55, start=5.75, end=6.0),  # Gb (F3)
])

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Db) - open voicing: F, Ab, C, Db
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),  # F (D3)
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0),  # Ab (E3)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=2.0),  # C (F3)
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=2.0),  # Db (D3)
]

# Bar 3: Bbm7 (Bb, Db, F, Ab) - open voicing: Bb, F, Ab, Db
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.5),  # Bb (D#3)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.5),  # F (E3)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.5),  # Ab (E2)
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.5),  # Db (D2)
])

# Bar 4: Ebm7 (Eb, Gb, Bb, Db) - open voicing: Eb, Bb, Gb, Db
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=5.0),  # Eb (D3)
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=5.0),  # Bb (D#3)
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=5.0),  # Gb (F3)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=5.0),  # Db (D2)
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5 - 3.0s): Motif starting on F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=1.9),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.15),  # C
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.4),  # Db
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=2.9),  # F (repeat)
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.15),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=3.25, end=3.4),  # C
    pretty_midi.Note(velocity=110, pitch=52, start=3.5, end=3.65),  # Db
    pretty_midi.Note(velocity=110, pitch=53, start=3.75, end=3.9),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=4.0, end=4.15),  # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=4.25, end=4.4),  # C
    pretty_midi.Note(velocity=110, pitch=52, start=4.5, end=4.65),  # Db
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
