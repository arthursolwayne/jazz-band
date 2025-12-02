
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeating notes
bass_notes = [
    (1.5, 48),  # F
    (1.875, 47),  # Eb
    (2.25, 49),  # Gb
    (2.625, 50),  # Ab
    (3.0, 48),  # F
    (3.375, 47),  # Eb
    (3.75, 49),  # Gb
    (4.125, 50),  # Ab
    (4.5, 48),  # F
    (4.875, 47),  # Eb
    (5.25, 49),  # Gb
    (5.625, 50)   # Ab
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
# Ebm7 = Eb, Gb, Bb, Db
# Abm7 = Ab, B, Eb, Gb
piano_notes = [
    (1.5, 53),  # F
    (1.5, 60),  # Ab
    (1.5, 64),  # C
    (1.5, 65),  # Eb
    (2.25, 57),  # Bb
    (2.25, 62),  # Db
    (2.25, 64),  # F
    (2.25, 65),  # Ab
    (3.0, 60),  # Eb
    (3.0, 66),  # Gb
    (3.0, 67),  # Bb
    (3.0, 69),  # Db
    (3.75, 64),  # Ab
    (3.75, 67),  # B
    (3.75, 69),  # Eb
    (3.75, 71),  # Gb
    (4.5, 53),  # F
    (4.5, 60),  # Ab
    (4.5, 64),  # C
    (4.5, 65)   # Eb
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: short motif, start it, leave it hanging, come back and finish it
# F (60), Ab (65), C (64), Bb (62)
sax_notes = [
    (1.5, 60),  # F
    (1.625, 65),  # Ab
    (1.75, 64),  # C
    (2.0, 60),  # F
    (2.125, 62),  # Bb
    (2.25, 65),  # Ab
    (2.375, 64),  # C
    (2.5, 60),  # F
    (2.625, 62),  # Bb
    (2.75, 65),  # Ab
    (2.875, 64),  # C
    (3.0, 60)   # F
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
