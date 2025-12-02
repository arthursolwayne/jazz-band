
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
for bar in range(1):
    time = bar * 1.5
    # Kick on beat 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on beat 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on beat 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on beat 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, Db, Eb, Gb, G, A
# Bass line: F -> G -> Ab -> Bb -> Bb -> C -> Db -> Eb
bass_notes = [
    (1.5, 71),   # F
    (1.875, 72), # G
    (2.25, 70),  # Ab
    (2.625, 69), # Bb
    (3.0, 69),   # Bb
    (3.375, 71), # C
    (3.75, 68),  # Db
    (4.125, 67), # Eb
    (4.5, 69),   # Bb
    (4.875, 71), # C
    (5.25, 68),  # Db
    (5.625, 67), # Eb
    (6.0, 69)    # Bb
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7, Bb7, Eb7, Ab7
chords = [
    (1.5, 65, 69, 72, 71),   # F7 (F, A, C, Eb)
    (2.25, 69, 72, 76, 74),  # Bb7 (Bb, D, F, Ab)
    (3.0, 67, 71, 74, 72),   # Eb7 (Eb, G, Bb, Db)
    (3.75, 70, 74, 77, 75),  # Ab7 (Ab, C, Eb, Gb)
    (4.5, 67, 71, 74, 72),   # Eb7
    (5.25, 70, 74, 77, 75)   # Ab7
]
for start, root, third, fifth, seventh in chords:
    note1 = pretty_midi.Note(velocity=90, pitch=root, start=start, end=start + 0.375)
    note2 = pretty_midi.Note(velocity=90, pitch=third, start=start, end=start + 0.375)
    note3 = pretty_midi.Note(velocity=90, pitch=fifth, start=start, end=start + 0.375)
    note4 = pretty_midi.Note(velocity=90, pitch=seventh, start=start, end=start + 0.375)
    piano.notes.append(note1)
    piano.notes.append(note2)
    piano.notes.append(note3)
    piano.notes.append(note4)

# Sax: Melody, one short motif, make it sing
# Motif: F (Ab) - Bb - Eb - D
# Start at bar 2
# D is a passing tone, resolve to Eb
motif = [
    (1.5, 71),   # F
    (1.875, 70), # Ab
    (2.25, 69),  # Bb
    (2.625, 67), # Eb
    (3.0, 66),   # D
    (3.375, 67), # Eb
    (3.75, 69),  # Bb
    (4.125, 71), # F
    (4.5, 70),   # Ab
    (4.875, 69), # Bb
    (5.25, 67),  # Eb
    (5.625, 66), # D
    (6.0, 67)    # Eb
]
for start, pitch in motif:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
