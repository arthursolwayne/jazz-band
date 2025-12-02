
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
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 45), (1.75, 46), (2.0, 47), (2.25, 49),
    (2.5, 50), (2.75, 51), (3.0, 52), (3.25, 53),
    (3.5, 55), (3.75, 57), (4.0, 59), (4.25, 60),
    (4.5, 62), (4.75, 63), (5.0, 64), (5.25, 65)
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.75, 62), (1.75, 67), (1.75, 71), (1.75, 72),
    # Bar 3 (2.5 - 3.25s)
    (2.75, 62), (2.75, 67), (2.75, 71), (2.75, 72),
    # Bar 4 (3.5 - 4.25s)
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 72)
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25))

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.5, 62), (1.65, 65), (1.8, 69),
    # Bar 3 (2.5 - 3.25s)
    (2.5, 66), (2.65, 69), (2.8, 72),
    # Bar 4 (3.5 - 4.25s)
    (3.5, 62), (3.65, 65), (3.8, 69), (4.0, 66), (4.15, 69), (4.3, 72)
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.15))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
