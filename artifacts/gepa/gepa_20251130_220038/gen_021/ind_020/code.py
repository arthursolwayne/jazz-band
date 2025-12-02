
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
# F7 chord: F, A, C, E
# Walking bass line: F, G, Ab, A, Bb, B, C, Db, D, Eb, E, F#, G, Ab, A, Bb
bass_notes = [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]
bass_time = 1.5
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bass_time, end=bass_time + 0.25))
    bass_time += 0.25

# Piano: 7th chords, comp on 2 and 4
# F7: F, A, C, E
# Bb7: Bb, D, F, Ab
# C7: C, E, G, B
# E7: E, G#, B, D
piano_notes = [
    # Bar 2
    (1, 77, 1.5, 1.75), (1, 82, 1.5, 1.75), (1, 87, 1.5, 1.75), (1, 89, 1.5, 1.75),
    # Bar 3
    (1, 80, 2.25, 2.5), (1, 84, 2.25, 2.5), (1, 87, 2.25, 2.5), (1, 90, 2.25, 2.5),
    # Bar 4
    (1, 79, 3.0, 3.25), (1, 84, 3.0, 3.25), (1, 89, 3.0, 3.25), (1, 91, 3.0, 3.25)
]
for vel, pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, C
sax_notes = [
    (100, 77, 1.5, 1.75),
    (100, 80, 1.75, 2.0),
    (100, 81, 2.0, 2.25),
    (100, 83, 2.25, 2.5),
    (100, 77, 3.0, 3.25),
    (100, 80, 3.25, 3.5),
    (100, 81, 3.5, 3.75),
    (100, 83, 3.75, 4.0)
]
for vel, pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# Drums: Bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
