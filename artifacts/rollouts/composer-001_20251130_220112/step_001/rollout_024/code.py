
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm
# Fm: F, Ab, D, C (root, b3, 5, b7)
# Chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    (1.5, 64), (1.75, 63), (2.0, 62), (2.25, 61), # F, Eb, D, C
    # Bar 3 (2.5s)
    (2.5, 60), (2.75, 61), (3.0, 62), (3.25, 63), # Bb, B, C, C#
    # Bar 4 (3.5s)
    (3.5, 64), (3.75, 63), (4.0, 62), (4.25, 61), # F, Eb, D, C
    # Bar 4 (4.5s)
    (4.5, 60), (4.75, 61), (5.0, 62), (5.25, 63)  # Bb, B, C, C#
]
for time, note in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    (1.5, 59), (1.5, 62), (1.5, 65), (1.5, 67), # F7: F, A, C, Eb
    (2.0, 59), (2.0, 62), (2.0, 65), (2.0, 67),
    # Bar 3 (2.5s)
    (2.5, 57), (2.5, 60), (2.5, 63), (2.5, 65), # Bb7: Bb, D, F, Ab
    (3.0, 57), (3.0, 60), (3.0, 63), (3.0, 65),
    # Bar 4 (3.5s)
    (3.5, 59), (3.5, 62), (3.5, 65), (3.5, 67), # F7
    (4.0, 59), (4.0, 62), (4.0, 65), (4.0, 67),
    # Bar 4 (4.5s)
    (4.5, 57), (4.5, 60), (4.5, 63), (4.5, 65)  # Bb7
]
for time, note in piano_notes:
    pn = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(pn)

# Sax: Motif starts in bar 2
# Fm: F, Ab, D, C
# Motif: F -> Ab -> D -> C (four notes)
# Start at 1.5s, leave it hanging at 2.0s, come back at 4.5s to finish
sax_notes = [
    (1.5, 64), (1.75, 62), (2.0, 67), (2.25, 64),  # F, Ab, D, F
    (4.5, 62), (4.75, 67), (5.0, 64)               # Ab, D, F
]
for time, note in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sn)

# Drums: Bar 2 (1.5 - 3.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("wayne_intro.mid")
