
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking line in F minor, chromatic approach to Bb
bass_notes = [
    (1.5, 65), (1.875, 66), (2.25, 64), (2.625, 62), # F -> Gb -> E -> D
    (3.0, 65), (3.375, 66), (3.75, 64), (4.125, 62)
]

for time, note in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano - 7th chords on 2 and 4, comping in F minor
piano_notes = [
    # Bar 2
    (1.5, 38), (1.5, 42), (1.5, 46), (1.5, 50), # F7
    (1.875, 46), (1.875, 50), (1.875, 53), (1.875, 57), # Bb7
    (2.25, 38), (2.25, 42), (2.25, 46), (2.25, 50), # F7
    (2.625, 46), (2.625, 50), (2.625, 53), (2.625, 57) # Bb7
]

for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Sax - motif in F minor, 4 notes, leave it hanging
sax_notes = [
    (1.5, 66), (1.875, 69), (2.25, 67), (2.625, 64)
]

for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking line in F minor, chromatic approach to Bb
bass_notes = [
    (3.0, 62), (3.375, 64), (3.75, 66), (4.125, 65), # D -> E -> G -> F
    (4.5, 62), (4.875, 64), (5.25, 66), (5.625, 65)
]

for time, note in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano - 7th chords on 2 and 4, comping in F minor
piano_notes = [
    # Bar 3
    (3.0, 38), (3.0, 42), (3.0, 46), (3.0, 50), # F7
    (3.375, 46), (3.375, 50), (3.375, 53), (3.375, 57), # Bb7
    (3.75, 38), (3.75, 42), (3.75, 46), (3.75, 50), # F7
    (4.125, 46), (4.125, 50), (4.125, 53), (4.125, 57) # Bb7
]

for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]

for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - walking line in F minor, chromatic approach to Bb
bass_notes = [
    (4.5, 65), (4.875, 66), (5.25, 64), (5.625, 62), # F -> Gb -> E -> D
    (6.0, 65), (6.375, 66), (6.75, 64), (7.125, 62)
]

for time, note in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano - 7th chords on 2 and 4, comping in F minor
piano_notes = [
    # Bar 4
    (4.5, 38), (4.5, 42), (4.5, 46), (4.5, 50), # F7
    (4.875, 46), (4.875, 50), (4.875, 53), (4.875, 57), # Bb7
    (5.25, 38), (5.25, 42), (5.25, 46), (5.25, 50), # F7
    (5.625, 46), (5.625, 50), (5.625, 53), (5.625, 57) # Bb7
]

for time, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(n)

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]

for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Sax - motif again, but finish it
sax_notes = [
    (4.5, 66), (4.875, 69), (5.25, 67), (5.625, 64)
]

for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(n)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
