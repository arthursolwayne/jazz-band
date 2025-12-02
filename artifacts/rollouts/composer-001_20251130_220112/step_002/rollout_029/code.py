
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
    start = bar * 1.5
    # Kick on beat 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on beat 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Kick on beat 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick)
    # Snare on beat 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
# In F, a walking bass line with chromatic approaches
# F - G - Ab - A - Bb - B - C - Db - D - Eb - E - F - G - Ab - A - Bb

bass_notes = [
    (1.5, 45, 100),   # F
    (1.875, 46, 100), # G
    (2.25, 47, 100),  # Ab
    (2.625, 48, 100), # A
    (3.0, 49, 100),   # Bb
    (3.375, 50, 100), # B
    (3.75, 51, 100),  # C
    (4.125, 52, 100), # Db
    (4.5, 53, 100),   # D
    (4.875, 54, 100), # Eb
    (5.25, 55, 100),  # E
    (5.625, 51, 100), # C (chromatic approach)
    (6.0, 52, 100),   # Db (chromatic approach)
    (6.375, 53, 100), # D (chromatic approach)
]

for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
# F7 (F, A, C, Eb), Bb7 (Bb, D, F, Ab), F7 again, Bb7 again

piano_notes = [
    # Bar 2, beat 2: F7
    (2.25, 69, 100), # F
    (2.25, 71, 100), # A
    (2.25, 73, 100), # C
    (2.25, 75, 100), # Eb
    # Bar 2, beat 4: Bb7
    (3.0, 76, 100), # Bb
    (3.0, 78, 100), # D
    (3.0, 73, 100), # F
    (3.0, 77, 100), # Ab
    # Bar 3, beat 2: F7
    (4.125, 69, 100), # F
    (4.125, 71, 100), # A
    (4.125, 73, 100), # C
    (4.125, 75, 100), # Eb
    # Bar 3, beat 4: Bb7
    (4.875, 76, 100), # Bb
    (4.875, 78, 100), # D
    (4.875, 73, 100), # F
    (4.875, 77, 100), # Ab
    # Bar 4, beat 2: F7
    (5.625, 69, 100), # F
    (5.625, 71, 100), # A
    (5.625, 73, 100), # C
    (5.625, 75, 100), # Eb
    # Bar 4, beat 4: Bb7
    (6.375, 76, 100), # Bb
    (6.375, 78, 100), # D
    (6.375, 73, 100), # F
    (6.375, 77, 100), # Ab
]

for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# motif: F - G - Ab - A (4 notes)
# Bar 2: F (start at 1.5)
# Bar 2: G (start at 1.875)
# Bar 2: Ab (start at 2.25)
# Bar 2: A (start at 2.625) - leave it hanging

# Bar 3: F (start at 4.5) - come back and finish it

sax_notes = [
    (1.5, 69, 110),  # F
    (1.875, 71, 110), # G
    (2.25, 72, 110),  # Ab
    (2.625, 73, 110), # A
    (4.5, 69, 110),   # F (return)
]

for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on beat 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    drums.notes.append(snare)
    # Kick on beat 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick)
    # Snare on beat 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.875)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
