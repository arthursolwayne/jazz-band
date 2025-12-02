
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
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 53),
    (3.0, 55), (3.375, 53), (3.75, 51), (4.125, 49),
    (4.5, 50), (4.875, 52), (5.25, 54), (5.625, 55)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),
    # Bar 3
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),
    # Bar 4
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing
sax_notes = [
    (2.0, 62), (2.25, 67), (2.5, 64), (2.75, 62),  # first motif
    (3.0, 67), (3.25, 64), (3.5, 62), (3.75, 64),  # second motif
    (4.0, 67), (4.25, 64), (4.5, 62), (4.75, 64),  # third motif
    (5.0, 67), (5.25, 64), (5.5, 62), (5.75, 64)   # fourth motif
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
