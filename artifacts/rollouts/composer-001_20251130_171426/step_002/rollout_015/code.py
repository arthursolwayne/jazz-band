
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [50, 51, 53, 55, 57, 59, 60, 62, 64, 66, 67, 69, 71, 72, 74, 76]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        index = (bar - 2) * 4 + beat
        note = pretty_midi.Note(velocity=80, pitch=bass_notes[index % len(bass_notes)], start=time, end=time + 0.25)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    [64, 67, 71, 72],  # D7
    [64, 67, 71, 72],  # D7
    [62, 65, 69, 71],  # Bm7
    [64, 67, 71, 72],  # D7
    [64, 67, 71, 72],  # D7
    [62, 65, 69, 71],  # Bm7
    [64, 67, 71, 72],  # D7
    [64, 67, 71, 72],  # D7
]
for i, chord in enumerate(piano_notes):
    time = i * 0.75
    for note in chord:
        pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D D# F A (D7 arpeggio with a twist)
sax_notes = [
    (64, 0.0),    # D
    (66, 0.375),  # D#
    (67, 0.75),   # F
    (72, 1.125),  # A
    (64, 1.5),    # D
    (66, 1.875),  # D#
    (67, 2.25),   # F
    (72, 2.625),  # A
    (64, 3.0),    # D
    (66, 3.375),  # D#
    (67, 3.75),   # F
    (72, 4.125),  # A
    (64, 4.5),    # D
    (66, 4.875),  # D#
    (67, 5.25),   # F
    (72, 5.625),  # A
]
for note, time in sax_notes:
    pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
