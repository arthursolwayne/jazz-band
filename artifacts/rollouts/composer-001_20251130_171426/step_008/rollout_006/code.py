
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
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Dm7 -> Gm7 -> Cm7 -> F7
bass_notes = [
    (1.5, 62), (1.75, 60), (2.0, 62), (2.25, 64),
    (2.5, 64), (2.75, 62), (3.0, 60), (3.25, 62),
    (3.5, 64), (3.75, 62), (4.0, 60), (4.25, 62),
    (4.5, 64), (4.75, 62), (5.0, 60), (5.25, 62)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (2.0, 62), (2.0, 67), (2.0, 72), (2.0, 74),
    (2.25, 62), (2.25, 67), (2.25, 72), (2.25, 74),
    # Bar 3: Gm7 on 2 and 4
    (3.5, 67), (3.5, 72), (3.5, 76), (3.5, 79),
    (3.75, 67), (3.75, 72), (3.75, 76), (3.75, 79),
    # Bar 4: Cm7 on 2 and 4
    (5.0, 60), (5.0, 65), (5.0, 70), (5.0, 72),
    (5.25, 60), (5.25, 65), (5.25, 70), (5.25, 72)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, G, Bb (Dm7 arpeggio)
sax_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 74),  # Motif start
    (1.625, 62), (1.625, 67), (1.625, 72), (1.625, 74),  # Repeat
    (1.75, 62), (1.75, 67), (1.75, 72), (1.75, 74)   # Finish
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Continue for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (start, 36), (start + 0.375, 42), (start + 0.75, 38), (start + 1.125, 42),
        (start + 1.5, 36), (start + 1.875, 42), (start + 2.25, 38), (start + 2.625, 42)
    ]
    for time, note_number in drum_notes:
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
