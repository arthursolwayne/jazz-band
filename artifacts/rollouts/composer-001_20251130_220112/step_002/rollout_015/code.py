
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

# Drums in bar 1 (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))

# Bars 2-4 (1.5 - 6.0s)
# Start with the bass line (Marcus)
# Walking line in Fm, chromatic approaches

# Fm: F, Ab, Bb, Db
# Walking bass line: F -> Gb -> Ab -> A -> Bb -> B -> Db -> D

bass_notes = [
    (1.5, 71),  # F
    (1.875, 69), # Gb
    (2.25, 70),  # Ab
    (2.625, 71), # A
    (3.0, 69),   # Bb
    (3.375, 71), # B
    (3.75, 68),  # Db
    (4.125, 70), # D
    (4.5, 71),   # F
    (4.875, 69), # Gb
    (5.25, 70),  # Ab
    (5.625, 71), # A
]

for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375))

# Diane on piano - 7th chords on 2 and 4
# F7 on 2, Bb7 on 4

# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab

piano_notes = [
    # Bar 2, beat 2: F7
    (2.25, 65),  # F
    (2.25, 68),  # A
    (2.25, 72),  # C
    (2.25, 67),  # Eb
    # Bar 2, beat 4: F7
    (3.0, 65),   # F
    (3.0, 68),   # A
    (3.0, 72),   # C
    (3.0, 67),   # Eb
    # Bar 3, beat 2: Bb7
    (4.125, 62), # Bb
    (4.125, 66), # D
    (4.125, 65), # F
    (4.125, 69), # Ab
    # Bar 3, beat 4: Bb7
    (4.875, 62), # Bb
    (4.875, 66), # D
    (4.875, 65), # F
    (4.875, 69), # Ab
]

for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.375))

# Little Ray in bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for i in range(6):
    time = 1.5 + i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))

# Dante on tenor sax - bars 2-4: short motif, make it sing
# Fm - F, Ab, Bb, Db

# Motif: F (1.5s) -> Ab (1.875s) -> Bb (2.25s) -> Db (2.625s), then leave it hanging

sax_notes = [
    (1.5, 66),  # F
    (1.875, 64), # Ab
    (2.25, 62),  # Bb
    (2.625, 60), # Db
    # End of motif at 3.0s
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375))

# Add the second pass of the motif at 4.5s
sax_notes = [
    (4.5, 66),  # F
    (4.875, 64), # Ab
    (5.25, 62),  # Bb
    (5.625, 60), # Db
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
