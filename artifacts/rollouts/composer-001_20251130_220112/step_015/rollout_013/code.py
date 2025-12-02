
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 42), (0.375, 36), (0.75, 42), (1.125, 36), (1.5, 42),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36), (1.875, 37), (2.25, 35), (2.625, 34), (3.0, 36),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 37), (3.375, 38), (3.75, 36), (4.125, 35), (4.5, 37),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 38), (4.875, 39), (5.25, 37), (5.625, 36), (6.0, 38),
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 45), (1.75, 48), (1.75, 50), (1.75, 55), (2.25, 45), (2.25, 48), (2.25, 50), (2.25, 55),
    # Bar 3 (3.0 - 4.5s)
    (3.25, 43), (3.25, 47), (3.25, 49), (3.25, 53), (3.75, 43), (3.75, 47), (3.75, 49), (3.75, 53),
    # Bar 4 (4.5 - 6.0s)
    (4.75, 45), (4.75, 48), (4.75, 50), (4.75, 55), (5.25, 45), (5.25, 48), (5.25, 50), (5.25, 55),
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64), (1.75, 62), (2.0, 60), (2.25, 62), (2.5, 64),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62), (3.25, 60), (3.5, 62), (3.75, 64), (4.0, 62),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 60), (4.75, 62), (5.0, 64), (5.25, 62), (5.5, 60),
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Drums: Fill the bar
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36), (1.875, 38), (2.25, 36), (2.625, 38), (3.0, 42),
    (1.5, 42), (1.875, 36), (2.25, 42), (2.625, 36), (3.0, 42),
    (1.5, 42), (1.875, 42), (2.25, 42), (2.625, 42), (3.0, 42),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 36), (3.375, 38), (3.75, 36), (4.125, 38), (4.5, 42),
    (3.0, 42), (3.375, 36), (3.75, 42), (4.125, 36), (4.5, 42),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42), (4.5, 42),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 36), (4.875, 38), (5.25, 36), (5.625, 38), (6.0, 42),
    (4.5, 42), (4.875, 36), (5.25, 42), (5.625, 36), (6.0, 42),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42), (6.0, 42),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
