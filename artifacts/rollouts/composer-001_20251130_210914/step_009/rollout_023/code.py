
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
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Fm7 -> Ab -> Bb -> Eb (ascending minor 3rd, then whole step, then minor 3rd)

# Fm7 (F, Ab, Bb, Db) -> Ab -> Bb -> Eb (F, Ab, Bb, Eb)
note1 = pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875)  # F
note2 = pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25) # Ab
note3 = pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625) # Bb
note4 = pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0) # Eb

sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in Fm
# F -> Gb -> Ab -> A -> Bb -> C -> Db -> D -> Eb -> F
bass_notes = [
    (1.5, 72),  # F
    (1.625, 71), # Gb
    (1.75, 68),  # Ab
    (1.875, 69), # A
    (2.0, 70),   # Bb
    (2.125, 72), # C
    (2.25, 67),  # Db
    (2.375, 69), # D
    (2.5, 64),   # Eb
    (2.625, 72), # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.125)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 on 2 (1.875), Ab7 on 4 (2.625)

# Fm7 (F, Ab, Bb, Db)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.125)
note2 = pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.125)
note3 = pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.125)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.125)
piano.notes.extend([note1, note2, note3, note4])

# Ab7 (Ab, C, Db, F)
note1 = pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.875)
note2 = pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.875)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875)
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with chromatic passing tone on 3

note5 = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375)  # F
note6 = pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75) # Ab
note7 = pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125) # Bb (passing)
note8 = pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5) # Eb

sax.notes.extend([note5, note6, note7, note8])

# Bass: Walking line in Fm
bass_notes2 = [
    (3.0, 72),  # F
    (3.125, 71), # Gb
    (3.25, 68),  # Ab
    (3.375, 69), # A
    (3.5, 70),   # Bb
    (3.625, 72), # C
    (3.75, 67),  # Db
    (3.875, 69), # D
    (4.0, 64),   # Eb
    (4.125, 72), # F
]

for t, pitch in bass_notes2:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.125)
    bass.notes.append(note)

# Piano: comp on 2 and 4 (3.375 and 4.125)
# Fm7 on 2 (3.375), Ab7 on 4 (4.125)

# Fm7 (F, Ab, Bb, Db)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.625)
note2 = pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.625)
note3 = pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.625)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.625)
piano.notes.extend([note1, note2, note3, note4])

# Ab7 (Ab, C, Db, F)
note1 = pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.375)
note2 = pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.375)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.375)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.375)
piano.notes.extend([note1, note2, note3, note4])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End on F, with a slight lift
note9 = pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875)  # F
note10 = pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.25) # Gb (chromatic lift)
note11 = pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625) # F (resolution)
note12 = pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0) # F

sax.notes.extend([note9, note10, note11, note12])

# Bass: Walking line in Fm
bass_notes3 = [
    (4.5, 72),  # F
    (4.625, 71), # Gb
    (4.75, 68),  # Ab
    (4.875, 69), # A
    (5.0, 70),   # Bb
    (5.125, 72), # C
    (5.25, 67),  # Db
    (5.375, 69), # D
    (5.5, 64),   # Eb
    (5.625, 72), # F
]

for t, pitch in bass_notes3:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.125)
    bass.notes.append(note)

# Piano: comp on 2 and 4 (4.875 and 5.625)
# Fm7 on 2 (4.875), Ab7 on 4 (5.625)

# Fm7 (F, Ab, Bb, Db)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.125)
note2 = pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.125)
note3 = pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.125)
note4 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.125)
piano.notes.extend([note1, note2, note3, note4])

# Ab7 (Ab, C, Db, F)
note1 = pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=5.875)
note2 = pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.875)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.875)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.875)
piano.notes.extend([note1, note2, note3, note4])

# Add drum fill for the last bar
kick_times2 = [4.5, 5.25]
snare_times2 = [4.875, 5.625]
hihat_times2 = [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times2:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times2:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times2:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
