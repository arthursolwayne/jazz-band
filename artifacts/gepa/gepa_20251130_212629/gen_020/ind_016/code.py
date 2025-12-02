
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]

for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 50),
    # Bar 3
    (3.0, 48), (3.375, 47), (3.75, 49), (4.125, 48),
    # Bar 4
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 50)
]

for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (1.875, 62), (1.875, 67), (1.875, 70), (1.875, 74),
    # Bar 3: G7
    (3.375, 67), (3.375, 71), (3.375, 74), (3.375, 77),
    # Bar 4: Cm7
    (4.875, 60), (4.875, 65), (4.875, 68), (4.875, 72)
]

for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    # Bar 2: Start motif
    (1.5, 62), (1.75, 64), (2.0, 67), (2.25, 62),
    # Bar 3: Leave it hanging
    (3.0, 62),
    # Bar 4: Come back and finish it
    (4.5, 62), (4.75, 64), (5.0, 67), (5.25, 69)
]

for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=note_number, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
