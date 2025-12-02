
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 50, 100), (1.875, 48, 100), (2.25, 49, 100), (2.625, 51, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 50, 100), (3.375, 48, 100), (3.75, 49, 100), (4.125, 51, 100),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 50, 100), (4.875, 48, 100), (5.25, 49, 100), (5.625, 51, 100)
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (1.5, 53, 100), (1.5, 60, 100), (1.5, 64, 100), (1.5, 62, 100),
    # Bar 3: Gm7 (G, Bb, D, F)
    (3.0, 62, 100), (3.0, 66, 100), (3.0, 67, 100), (3.0, 53, 100),
    # Bar 4: Am7 (A, C, E, G)
    (4.5, 65, 100), (4.5, 64, 100), (4.5, 69, 100), (4.5, 67, 100)
]
for time, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: same pattern for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Ab (60), C (64), rest on 3rd beat, then F again
sax_notes = [
    (1.5, 53, 110), (1.875, 60, 110), (2.25, 64, 110),
    (3.375, 53, 110), (3.75, 60, 110), (4.125, 64, 110),
    (5.25, 53, 110), (5.625, 60, 110), (6.0, 64, 110)
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
