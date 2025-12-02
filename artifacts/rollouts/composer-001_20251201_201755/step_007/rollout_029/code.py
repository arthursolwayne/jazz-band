
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),  # 1st bar
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),  # 2nd bar
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),  # 3rd bar
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)   # 4th bar
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 43), (2.625, 42),
    (3.0, 43), (3.375, 45), (3.75, 48), (4.125, 47),
    (4.5, 48), (4.875, 50), (5.25, 53), (5.625, 52)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 66),
    # Bar 3: Bm7 (B, D, F#, A)
    (3.0, 69), (3.0, 64), (3.0, 67), (3.0, 71),
    # Bar 4: G7 (G, B, D, F)
    (4.5, 71), (4.5, 76), (4.5, 72), (4.5, 74)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note_obj)

# Sax: Short motif, begin, leave it hanging, come back and finish
sax_notes = [
    (1.5, 65), (1.6, 67), (1.7, 65), (1.8, 67),
    (3.0, 65), (3.1, 67), (3.2, 65), (3.3, 67),
    (4.5, 65), (4.6, 67), (4.7, 65), (4.8, 67)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
