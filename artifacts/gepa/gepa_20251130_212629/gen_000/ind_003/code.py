
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 52),  # Dm7
    (3.0, 52), (3.375, 51), (3.75, 49), (4.125, 50),  # G7
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 52)   # Dm7
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 72), (1.75, 70), (1.75, 68), (1.75, 67),  # Dm7
    # Bar 3 (3.0 - 4.5s)
    (3.25, 76), (3.25, 74), (3.25, 72), (3.25, 71),  # G7
    # Bar 4 (4.5 - 6.0s)
    (4.75, 72), (4.75, 70), (4.75, 68), (4.75, 67)   # Dm7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.75, 64), (2.0, 62), (2.25, 60),     # Dm
    (3.0, 62), (3.25, 64), (3.5, 62), (3.75, 60),     # Dm
    (4.5, 62), (4.75, 64), (5.0, 62), (5.25, 60)      # Dm
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
