
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
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat == 0 or beat == 2:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    if beat == 1 or beat == 3:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 64), (2.0, 63), (2.25, 65),
    (2.5, 67), (2.75, 65), (3.0, 64), (3.25, 62),
    (3.5, 60), (3.75, 62), (4.0, 61), (4.25, 63),
    (4.5, 65), (4.75, 64), (5.0, 62), (5.25, 60)
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 71), (1.5, 72),
    (2.0, 64), (2.0, 67), (2.0, 71), (2.0, 72),
    (2.5, 64), (2.5, 67), (2.5, 71), (2.5, 72),
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 72),
    (3.5, 64), (3.5, 67), (3.5, 71), (3.5, 72),
    (4.0, 64), (4.0, 67), (4.0, 71), (4.0, 72),
    (4.5, 64), (4.5, 67), (4.5, 71), (4.5, 72),
    (5.0, 64), (5.0, 67), (5.0, 71), (5.0, 72)
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (64), G (65), B (67)
sax_notes = [
    (1.5, 62), (1.625, 64), (1.75, 65), (1.875, 67),
    (2.0, 62), (2.5, 64), (2.75, 65), (3.0, 67),
    (3.5, 62), (3.625, 64), (3.75, 65), (3.875, 67),
    (4.0, 62), (4.125, 64), (4.25, 65), (4.375, 67)
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + (bar - 2) * bar_length + (beat * bar_length / 4)
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
