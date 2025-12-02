
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
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 57), (1.75, 58), (2.0, 59), (2.25, 60),  # Dm walk
    (2.5, 59), (2.75, 58), (3.0, 57), (3.25, 55),  # chromatic approach to Dm7
    (3.5, 55), (3.75, 57), (4.0, 59), (4.25, 60),  # Dm walk
    (4.5, 59), (4.75, 58), (5.0, 57), (5.25, 55),  # chromatic approach to Dm7
    (5.5, 55), (5.75, 57)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (1.75, 62), (1.75, 65), (1.75, 67), (1.75, 69),
    # Bar 3: G7 (G B D F)
    (3.25, 71), (3.25, 76), (3.25, 74), (3.25, 72),
    # Bar 4: Cm7 (C Eb G Bb)
    (4.75, 60), (4.75, 63), (4.75, 67), (4.75, 62)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875)
    drums.notes.append(drum_note)

# Dante: Tenor sax motif
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start on D (62), go up to F (65), back to D (62)
    (1.5, 62), (1.75, 65), (2.0, 62),
    # Leave it hanging on D (62) for 1 beat
    # Then resolve with a melodic line: D (62), A (67), C (67)
    (3.0, 62), (3.25, 67), (3.5, 67)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
