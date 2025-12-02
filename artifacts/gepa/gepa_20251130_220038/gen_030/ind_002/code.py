
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

# Bars 2-4: Full quartet

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 42), (1.875, 41), (2.25, 43), (2.625, 44),
    # Bar 3
    (3.0, 43), (3.375, 42), (3.75, 40), (4.125, 41),
    # Bar 4
    (4.5, 41), (4.875, 40), (5.25, 42), (5.625, 44)
]

for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 69), (1.875, 71), (1.875, 76),
    # Bar 3
    (3.375, 64), (3.375, 69), (3.375, 71), (3.375, 76),
    # Bar 4
    (4.875, 64), (4.875, 69), (4.875, 71), (4.875, 76)
]

for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: Motif in Fm, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (1.5, 64), (1.75, 67), (2.0, 64), (2.25, 67),
    # Bar 3
    (3.0, 64), (3.25, 67), (3.5, 64), (3.75, 67),
    # Bar 4
    (4.5, 64), (4.75, 67), (5.0, 64), (5.25, 67)
]

for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Add drums for bars 2-4
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
