
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
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 64), (1.875, 65), (2.25, 67), (2.625, 69),
    # Bar 3
    (3.0, 71), (3.375, 72), (3.75, 70), (4.125, 68),
    # Bar 4
    (4.5, 67), (4.875, 65), (5.25, 64), (5.625, 62)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 69), (1.875, 71), (1.875, 74),  # F7
    (2.625, 64), (2.625, 69), (2.625, 71), (2.625, 74),
    # Bar 3
    (3.375, 67), (3.375, 72), (3.375, 74), (3.375, 76),  # Bb7
    (4.125, 67), (4.125, 72), (4.125, 74), (4.125, 76),
    # Bar 4
    (4.875, 69), (4.875, 74), (4.875, 76), (4.875, 79),  # E7
    (5.625, 69), (5.625, 74), (5.625, 76), (5.625, 79)
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66), (1.75, 69), (2.0, 66), (2.25, 67), (2.5, 69), (2.75, 67),
    (3.0, 66), (3.25, 69), (3.5, 66), (3.75, 67), (4.0, 69), (4.25, 67),
    (4.5, 66), (4.75, 69), (5.0, 66), (5.25, 67), (5.5, 69), (5.75, 67)
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
