
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
for note_time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7 (D, A, F#, C#)
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 41), (2.625, 43),
    (3.0, 38), (3.375, 40), (3.75, 41), (4.125, 43),
    (4.5, 38), (4.875, 40), (5.25, 41), (5.625, 43)
]
for note_time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=note_time, end=note_time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F#, A, C#)
piano_notes = [
    # Bar 2
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 73),
    # Bar 3: G7 (G, B, D, F)
    (3.0, 67), (3.0, 71), (3.0, 76), (3.0, 79),
    # Bar 4: Cmaj7 (C, E, G, B)
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71)
]
for note_time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_time, end=note_time + 0.5)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), E (64), F# (67), D (62)
sax_notes = [
    (1.5, 62), (1.5, 64), (1.5, 67),
    (2.0, 62),
    (3.0, 62), (3.0, 64), (3.0, 67),
    (3.5, 62),
    (4.5, 62), (4.5, 64), (4.5, 67),
    (5.0, 62)
]
for note_time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=note_time, end=note_time + 0.25)
    sax.notes.append(note)

# Drums continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    for i in range(4):
        time = bar_start + i * 0.375
        if i % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
    for i in range(8):
        time = bar_start + i * 0.125
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
