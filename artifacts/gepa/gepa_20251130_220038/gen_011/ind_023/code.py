
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
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 45), (1.875, 46), (2.25, 47), (2.625, 48), (3.0, 48), (3.375, 47), (3.75, 46), (4.125, 45),
    # Bar 3
    (4.5, 45), (4.875, 46), (5.25, 47), (5.625, 48), (6.0, 48), (6.375, 47), (6.75, 46), (7.125, 45),
    # Bar 4
    (7.5, 45), (7.875, 46), (8.25, 47), (8.625, 48), (9.0, 48), (9.375, 47), (9.75, 46), (10.125, 45),
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 50), (1.5, 53), (1.5, 57), (1.5, 60),  # F7
    # Bar 3
    (3.0, 50), (3.0, 53), (3.0, 57), (3.0, 60),  # F7
    # Bar 4
    (4.5, 50), (4.5, 53), (4.5, 57), (4.5, 60),  # F7
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax (Dante): Motif in F
sax_notes = [
    # Bar 2
    (1.5, 66), (1.875, 69), (2.25, 67), (2.625, 69),  # F, A, G, A
    # Bar 3
    (3.0, 66), (3.375, 69), (3.75, 67), (4.125, 69),  # F, A, G, A (reprise)
    # Bar 4
    (4.5, 66), (4.875, 69), (5.25, 67), (5.625, 71),  # F, A, G, Bb (new note)
    (6.0, 71), (6.375, 69), (6.75, 67), (7.125, 66)   # Bb, A, G, F
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Drums: continued with same pattern
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (1.5, 42), (1.875, 42), (2.25, 42), (2.625, 42), (3.0, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42), (4.5, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42), (6.0, 42),
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
