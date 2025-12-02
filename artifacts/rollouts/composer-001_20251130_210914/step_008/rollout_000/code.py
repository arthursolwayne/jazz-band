
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 65), (1.75, 67), (2.0, 69), (2.25, 67),
    (2.5, 65), (2.75, 64), (3.0, 62), (3.25, 60),
    (3.5, 62), (3.75, 64), (4.0, 65), (4.25, 67),
    (4.5, 69), (4.75, 67), (5.0, 65), (5.25, 64),
    (5.5, 62), (5.75, 60)
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 72), (1.5, 76), (1.5, 69), (1.5, 67),
    (2.0, 72), (2.0, 76), (2.0, 69), (2.0, 67),
    (2.5, 72), (2.5, 76), (2.5, 69), (2.5, 67),
    (3.0, 72), (3.0, 76), (3.0, 69), (3.0, 67),
    (3.5, 72), (3.5, 76), (3.5, 69), (3.5, 67),
    (4.0, 72), (4.0, 76), (4.0, 69), (4.0, 67),
    (4.5, 72), (4.5, 76), (4.5, 69), (4.5, 67),
    (5.0, 72), (5.0, 76), (5.0, 69), (5.0, 67)
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), (1.75, 67), (2.0, 69), (2.25, 67),
    (2.5, 65), (2.75, 67), (3.0, 69), (3.25, 67),
    (3.5, 65), (3.75, 67), (4.0, 69), (4.25, 67),
    (4.5, 65), (4.75, 67), (5.0, 69), (5.25, 67)
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25))

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
