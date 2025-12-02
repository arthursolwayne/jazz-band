
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
    (0.0, 36), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 36),  # Bar 1
    (1.875, 38), (2.25, 42), (2.625, 42), (3.0, 42), (3.375, 36), # Bar 2
    (3.75, 38), (4.125, 42), (4.5, 42), (4.875, 42), (5.25, 36),  # Bar 3
    (5.625, 38), (6.0, 42)                                       # Bar 4
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 57), (1.875, 58), (2.25, 59), (2.625, 60),  # Bar 2
    (3.0, 62), (3.375, 61), (3.75, 60), (4.125, 59),  # Bar 3
    (4.5, 58), (4.875, 57), (5.25, 56), (5.625, 55)   # Bar 4
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),  # D7
    (3.75, 64), (3.75, 69), (3.75, 71), (3.75, 74),  # F7
    (5.25, 65), (5.25, 70), (5.25, 72), (5.25, 76)   # G7
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: Motif, start it, leave it hanging, come back to finish
sax_notes = [
    (1.5, 62), (1.875, 65), (2.25, 67),  # First 3 notes of motif
    (2.625, 69), (3.0, 67), (3.375, 65), (3.75, 62),  # Repetition
    (4.125, 62), (4.5, 65), (4.875, 67),  # Repeat motif
    (5.25, 69), (5.625, 67), (6.0, 65)   # End on D
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
