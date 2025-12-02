
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    dr_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line with chromatic approaches)
bass_notes = [
    # Bar 2
    (1.5, 48), (1.75, 49), (2.0, 50), (2.25, 51),
    # Bar 3
    (2.5, 50), (2.75, 49), (3.0, 48), (3.25, 47),
    # Bar 4
    (3.5, 47), (3.75, 48), (4.0, 49), (4.25, 50),
    # Bar 4 continuation
    (4.5, 51), (4.75, 50), (5.0, 49), (5.25, 48)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane - Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 2
    (1.75, 57), (1.75, 60), (1.75, 62), (1.75, 64),  # F7
    (2.25, 57), (2.25, 60), (2.25, 62), (2.25, 64),
    # Bar 3
    (2.75, 60), (2.75, 62), (2.75, 64), (2.75, 67),  # Bb7
    (3.25, 60), (3.25, 62), (3.25, 64), (3.25, 67),
    # Bar 4
    (3.75, 62), (3.75, 64), (3.75, 67), (3.75, 70),  # Eb7
    (4.25, 62), (4.25, 64), (4.25, 67), (4.25, 70),
    # Bar 4 continuation
    (4.75, 64), (4.75, 67), (4.75, 70), (4.75, 72),  # G7
    (5.25, 64), (5.25, 67), (5.25, 70), (5.25, 72)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    # Bar 3
    (2.5, 38), (2.875, 42), (3.25, 38), (3.625, 42),
    # Bar 4
    (3.5, 36), (3.875, 42), (4.25, 36), (4.625, 42),
    # Bar 4 continuation
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr_note)

# Dante - Tenor Sax - Motif
# Fm7 -> Bb7 -> Eb7 -> G7
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# G7: G, B, D, F

# Bar 2 - Start motif
sax_notes = [
    (1.5, 71),     # F
    (1.75, 69),    # Ab
    (2.0, 71),     # Bb
    (2.25, 68),    # Db
    # Bar 3 - Bb7
    (2.5, 69),     # Bb
    (2.75, 71),    # D
    (3.0, 69),     # F
    (3.25, 71),    # Ab
    # Bar 4 - Eb7
    (3.5, 67),     # Eb
    (3.75, 70),    # G
    (4.0, 69),     # Bb
    (4.25, 67),    # Db
    # Bar 4 continuation - G7
    (4.5, 71),     # G
    (4.75, 73),    # B
    (5.0, 71),     # D
    (5.25, 71),    # F
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
