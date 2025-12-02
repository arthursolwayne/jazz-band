
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    dr_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 45), (1.875, 46), (2.25, 47), (2.625, 49),
    (3.0, 50), (3.375, 51), (3.75, 52), (4.125, 53),
    (4.5, 55), (4.875, 56), (5.25, 57), (5.625, 59)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 64), (2.0, 69), (2.0, 71), (2.0, 76),  # F7 on beat 2
    (3.5, 64), (3.5, 69), (3.5, 71), (3.5, 76),  # F7 on beat 4
    (5.0, 64), (5.0, 69), (5.0, 71), (5.0, 76)   # F7 on beat 4
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66), (1.875, 69), (2.25, 71), (2.625, 69),  # motif
    (3.0, 66), (3.375, 69), (3.75, 71), (4.125, 69),  # repeat
    (4.5, 66), (4.875, 69), (5.25, 71), (5.625, 69)   # repeat
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
