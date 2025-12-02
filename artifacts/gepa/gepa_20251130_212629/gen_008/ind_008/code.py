
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 52),
    # Bar 3
    (3.0, 52), (3.375, 51), (3.75, 49), (4.125, 50),
    # Bar 4
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1875))

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62), (2.0, 67), (2.0, 69), (2.0, 71),
    (2.5, 62), (2.5, 67), (2.5, 69), (2.5, 71),
    # Bar 3
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71),
    (3.5, 62), (3.5, 67), (3.5, 69), (3.5, 71),
    # Bar 4
    (4.0, 62), (4.0, 67), (4.0, 69), (4.0, 71),
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1875))

# Sax: Dante - motif, one short phrase, starts on beat 1 of bar 2
sax_notes = [
    (1.5, 62), (1.875, 66), (2.25, 65), (2.625, 62),
    (3.0, 62), (3.375, 66), (3.75, 67), (4.125, 62),
    (4.5, 62), (4.875, 66), (5.25, 65), (5.625, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Drums: continue pattern through bars 2-4
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
