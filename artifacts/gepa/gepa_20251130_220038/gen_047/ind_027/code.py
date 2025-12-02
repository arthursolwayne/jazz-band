
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    (0.0, 36, 100),     # Kick on 1
    (0.75, 42, 100),    # Hihat on 2
    (1.0, 38, 100),     # Snare on 3
    (1.5, 42, 100)      # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 64, 100),     # F (root)
    (1.75, 65, 100),    # Gb (chromatic)
    (2.0, 63, 100),     # Eb (3rd)
    (2.25, 62, 100),    # D (chromatic)
    (2.5, 60, 100),     # C (5th)
    (2.75, 61, 100),    # Db (chromatic)
    (3.0, 59, 100),     # Bb (7th)
    (3.25, 58, 100),    # A (chromatic)
    (3.5, 64, 100),     # F (root)
    (3.75, 65, 100),    # Gb (chromatic)
    (4.0, 63, 100),     # Eb (3rd)
    (4.25, 62, 100),    # D (chromatic)
    (4.5, 60, 100),     # C (5th)
    (4.75, 61, 100),    # Db (chromatic)
    (5.0, 59, 100),     # Bb (7th)
    (5.25, 58, 100)     # A (chromatic)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 63, 100),     # Eb (3rd)
    (2.0, 60, 100),     # C (5th)
    (2.0, 58, 100),     # A (7th)
    (2.0, 64, 100),     # F (root)
    # Bar 3
    (3.5, 63, 100),     # Eb (3rd)
    (3.5, 60, 100),     # C (5th)
    (3.5, 58, 100),     # A (7th)
    (3.5, 64, 100),     # F (root)
    # Bar 4
    (5.0, 63, 100),     # Eb (3rd)
    (5.0, 60, 100),     # C (5th)
    (5.0, 58, 100),     # A (7th)
    (5.0, 64, 100)      # F (root)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),     # Kick on 1
    (1.75, 42, 100),    # Hihat on 2
    (2.0, 38, 100),     # Snare on 3
    (2.25, 42, 100),    # Hihat on 4
    (2.5, 36, 100),     # Kick on 1
    (2.75, 42, 100),    # Hihat on 2
    (3.0, 38, 100),     # Snare on 3
    (3.25, 42, 100),    # Hihat on 4
    (3.5, 36, 100),     # Kick on 1
    (3.75, 42, 100),    # Hihat on 2
    (4.0, 38, 100),     # Snare on 3
    (4.25, 42, 100),    # Hihat on 4
    (4.5, 36, 100),     # Kick on 1
    (4.75, 42, 100),    # Hihat on 2
    (5.0, 38, 100),     # Snare on 3
    (5.25, 42, 100)     # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db, D
sax_notes = [
    (1.5, 71, 100),     # F (octave 4)
    (1.625, 70, 100),   # Gb
    (1.75, 68, 100),    # Ab
    (1.875, 69, 100),   # A
    (2.0, 71, 100),     # F (octave 4)
    (2.125, 70, 100),   # Gb
    (2.25, 68, 100),    # Ab
    (2.375, 69, 100),   # A
    (2.5, 67, 100),     # Bb
    (2.625, 69, 100),   # A
    (2.75, 67, 100),    # Bb
    (2.875, 65, 100),   # C
    (3.0, 67, 100),     # Bb
    (3.125, 65, 100),   # C
    (3.25, 63, 100),    # Db
    (3.375, 65, 100),   # C
    (3.5, 71, 100),     # F (octave 4)
    (3.625, 70, 100),   # Gb
    (3.75, 68, 100),    # Ab
    (3.875, 69, 100),   # A
    (4.0, 71, 100),     # F (octave 4)
    (4.125, 70, 100),   # Gb
    (4.25, 68, 100),    # Ab
    (4.375, 69, 100),   # A
    (4.5, 67, 100),     # Bb
    (4.625, 69, 100),   # A
    (4.75, 67, 100),    # Bb
    (4.875, 65, 100),   # C
    (5.0, 67, 100),     # Bb
    (5.125, 65, 100),   # C
    (5.25, 63, 100),    # Db
    (5.375, 65, 100),   # C
    (5.5, 71, 100)      # F (octave 4)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
