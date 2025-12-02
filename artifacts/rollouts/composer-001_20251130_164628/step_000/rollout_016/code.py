
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

# Bass line: Marcus - walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 52),
    (3.0, 50), (3.375, 49), (3.75, 51), (4.125, 52),
    (4.5, 50), (4.875, 49), (5.25, 51), (5.625, 52)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (2.25, 62), (2.25, 67), (2.25, 70), (2.25, 72),
    (2.625, 62), (2.625, 67), (2.625, 70), (2.625, 72),
    # Bar 3: Gm7 on 2 and 4
    (3.75, 67), (3.75, 72), (3.75, 74), (3.75, 76),
    (4.125, 67), (4.125, 72), (4.125, 74), (4.125, 76),
    # Bar 4: Cm7 on 2 and 4
    (5.25, 60), (5.25, 65), (5.25, 67), (5.25, 69),
    (5.625, 60), (5.625, 65), (5.625, 67), (5.625, 69)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Dante - short motif, make it sing
sax_notes = [
    # Bar 2: Dm - motif starts
    (1.5, 62), (1.875, 67), (2.25, 62), (2.625, 65),
    # Bar 3: Gm - continuation of motif
    (3.0, 67), (3.375, 72), (3.75, 67), (4.125, 70),
    # Bar 4: Cm - complete the motif
    (4.5, 60), (4.875, 65), (5.25, 60), (5.625, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Drums continue for bars 2-4
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
