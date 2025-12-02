
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 60), (2.0, 63), (2.25, 62),
    (2.5, 60), (2.75, 63), (3.0, 62), (3.25, 60),
    (3.5, 63), (3.75, 62), (4.0, 60), (4.25, 63),
    (4.5, 62), (4.75, 60), (5.0, 63), (5.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2
    (2.0, 64), (2.0, 67), (2.0, 71), (2.0, 72),  # G7
    # Bar 3
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 76),  # Bm7
    # Bar 4
    (4.0, 64), (4.0, 67), (4.0, 71), (4.0, 72),  # G7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Sax: One short motif, make it sing
# D - F# - B - D (Dorian mode)
sax_notes = [
    (1.5, 62), (1.5, 66), (1.5, 71), (1.5, 62),
    (2.0, 71), (2.0, 66), (2.0, 62), (2.0, 66),
    (2.5, 62), (2.5, 66), (2.5, 71), (2.5, 62),
    (3.0, 62), (3.0, 65), (3.0, 69), (3.0, 62),
    (3.5, 69), (3.5, 65), (3.5, 62), (3.5, 65),
    (4.0, 62), (4.0, 66), (4.0, 71), (4.0, 62),
    (4.5, 62), (4.5, 66), (4.5, 71), (4.5, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = 1.5 * bar
    for i in range(4):
        time = bar_start + i * 0.375
        if i % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for i in range(8):
        time = bar_start + i * 0.125
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
