
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 40), (1.875, 39), (2.25, 41), (2.625, 42),
    (3.0, 43), (3.375, 42), (3.75, 41), (4.125, 40),
    (4.5, 39), (4.875, 38), (5.25, 40), (5.625, 42)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 71),
    # Bar 3
    (3.75, 60), (3.75, 64), (3.75, 67), (3.75, 71),
    # Bar 4
    (5.25, 60), (5.25, 64), (5.25, 67), (5.25, 71)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(drum_note)

# Dante on sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
sax_notes = [
    (1.5, 64), (1.875, 62), (2.25, 60), (2.625, 60),
    (3.0, 62), (3.375, 64), (3.75, 62), (4.125, 60),
    (4.5, 64), (4.875, 62), (5.25, 60), (5.625, 60)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
