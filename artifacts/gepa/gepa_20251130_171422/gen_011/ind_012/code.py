
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 39), (1.875, 40), (2.25, 38), (2.625, 37),
    (3.0, 39), (3.375, 40), (3.75, 38), (4.125, 37),
    (4.5, 39), (4.875, 40), (5.25, 38), (5.625, 37)
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4, Fm7, Bbm7, Eb7, Ab7
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 67), (1.875, 71), (1.875, 76),
    # Bar 3
    (3.375, 64), (3.375, 67), (3.375, 71), (3.375, 76),
    # Bar 4
    (4.875, 64), (4.875, 67), (4.875, 71), (4.875, 76)
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm (F, Ab, Bb, D)
sax_notes = [
    (1.5, 77), (1.625, 80), (1.75, 79), (1.875, 82),
    (3.0, 77), (3.125, 80), (3.25, 79), (3.375, 82),
    (4.5, 77), (4.625, 80), (4.75, 79), (4.875, 82)
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125))

# Drums: 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
