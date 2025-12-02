
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

# Bars 2-4: Full quartet
# Time starts at 1.5s

# Marcus: Walking line, chromatic approaches, never the same note twice. Fm7 -> Bb7 -> Eb7 -> Ab7
# Bar 2: Fm7 - root motion F -> Bb
# Bar 3: Bb7 - root motion Bb -> Eb
# Bar 4: Eb7 - root motion Eb -> Ab

# Bass line
bass_notes = [
    # Bar 2
    (1.5, 53), # F
    (1.875, 51), # Eb
    (2.25, 50), # D
    (2.625, 49), # C

    # Bar 3
    (2.875, 57), # Bb
    (3.25, 55), # Ab
    (3.625, 54), # G
    (4.0, 53), # F

    # Bar 4
    (4.25, 61), # Eb
    (4.625, 59), # Db
    (5.0, 58), # C
    (5.375, 57), # Bb
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4. Fm7, Bb7, Eb7, Ab7
# Bar 2: Fm7 (F, Ab, Bb, Db) - comp on 2 and 4
# Bar 3: Bb7 (Bb, Db, Eb, F) - comp on 2 and 4
# Bar 4: Eb7 (Eb, G, Ab, Bb) - comp on 2 and 4

# Bar 2: Fm7
diane_notes = [
    # Bar 2
    (1.875, 53), # F
    (1.875, 51), # Ab
    (1.875, 50), # Bb
    (1.875, 49), # Db

    # Bar 3
    (3.25, 57), # Bb
    (3.25, 55), # Db
    (3.25, 54), # Eb
    (3.25, 53), # F

    # Bar 4
    (4.625, 61), # Eb
    (4.625, 58), # G
    (4.625, 57), # Ab
    (4.625, 54), # Bb
]
for start, pitch in diane_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, Db (Fm7) - start on 1.5, end on 2.0
# Then repeat on 3.0, end on 3.5
# Then resolve on 4.0, end on 4.5

sax_notes = [
    # Bar 2
    (1.5, 66), # F
    (1.875, 64), # Ab
    (2.25, 63), # Bb
    (2.625, 61), # Db

    # Bar 3
    (3.0, 66), # F
    (3.375, 64), # Ab
    (3.75, 63), # Bb
    (4.125, 61), # Db

    # Bar 4
    (4.5, 66), # F
    (4.875, 68), # G
    (5.25, 66), # F
    (5.625, 64), # Ab
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
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

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
