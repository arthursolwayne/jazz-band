
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F minor, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 45), (1.875, 46), (2.25, 47), (2.625, 45),
    # Bar 3
    (3.0, 45), (3.375, 46), (3.75, 47), (4.125, 45),
    # Bar 4
    (4.5, 45), (4.875, 46), (5.25, 47), (5.625, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on 2 and 4
    (1.875, 59), (1.875, 57), (2.625, 59), (2.625, 57),
    # Bar 3 - 7th chord on 2 and 4
    (3.375, 59), (3.375, 57), (4.125, 59), (4.125, 57),
    # Bar 4 - 7th chord on 2 and 4
    (4.875, 59), (4.875, 57), (5.625, 59), (5.625, 57)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: continue pattern
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    # Bar 3
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif starts here, short, melodic, leaves a question
# F7 -> G7 -> A7 -> F7 (minor 3rd interval)
sax_notes = [
    # Bar 2
    (1.5, 87), (1.625, 89), (1.75, 91), (1.875, 87),
    # Bar 3
    (2.25, 87), (2.375, 89), (2.5, 91), (2.625, 87),
    # Bar 4
    (3.0, 87), (3.125, 89), (3.25, 91), (3.375, 87),
    (3.5, 87), (3.625, 89), (3.75, 91), (3.875, 87)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
