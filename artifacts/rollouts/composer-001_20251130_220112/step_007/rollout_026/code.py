
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62), (1.875, 63), (2.25, 64), (2.625, 66),
    (3.0, 67), (3.375, 65), (3.75, 64), (4.125, 62),
    (4.5, 60), (4.875, 59), (5.25, 57), (5.625, 55)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (1.5, 65), (1.625, 69), (1.75, 72), (1.875, 67),
    # Bar 3
    (3.0, 65), (3.125, 69), (3.25, 72), (3.375, 67),
    # Bar 4
    (4.5, 65), (4.625, 69), (4.75, 72), (4.875, 67)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: Motif in D, one short phrase, leave it hanging
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 67), (2.25, 69),  # Start motif
    (2.5, 67), (2.75, 65), (3.0, 62), (3.25, 60),  # Answer with chromatic
    (3.5, 62), (3.75, 65), (4.0, 67), (4.25, 69),  # Repeat motif
    (4.5, 67), (4.75, 65), (5.0, 62), (5.25, 60)   # Resolve and leave it hanging
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums continue in bars 2-4
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne_intro.mid')
