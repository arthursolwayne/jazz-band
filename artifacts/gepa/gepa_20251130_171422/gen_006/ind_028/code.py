
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
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    (1.5, 50), (1.875, 49), (2.25, 50), (2.625, 51),
    # Bar 3 (Dm7)
    (3.0, 51), (3.375, 50), (3.75, 49), (4.125, 50),
    # Bar 4 (Dm7)
    (4.5, 50), (4.875, 51), (5.25, 50), (5.625, 49)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
piano_notes = []

# Bar 2: Dm7 (F, A, C, D)
piano_notes.extend([
    (1.875, 62), (1.875, 65), (1.875, 67), (1.875, 69)
])
# Bar 3: Dm7
piano_notes.extend([
    (3.375, 62), (3.375, 65), (3.375, 67), (3.375, 69)
])
# Bar 4: Dm7
piano_notes.extend([
    (4.875, 62), (4.875, 65), (4.875, 67), (4.875, 69)
])

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax (Dante) - melody, one short motif, make it sing
sax_notes = [
    # Bar 2: Start motif
    (1.5, 62), (1.75, 67), (2.0, 62),
    # Bar 3: Leave it hanging
    (3.0, 67), (3.25, 64), (3.5, 67),
    # Bar 4: Finish it
    (4.5, 62), (4.75, 67), (5.0, 64)
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
