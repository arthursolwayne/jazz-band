
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hats on every eighth
for i in range(0, 4):
    for j in range(0, 4):
        start = i * 1.5 + j * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# C D Eb F G Ab Bb C
bass_notes = [
    (1.5, 60),  # C
    (1.875, 62),  # D
    (2.25, 60),  # C
    (2.625, 61),  # C#
    (3.0, 62),  # D
    (3.375, 64),  # E
    (3.75, 62),  # D
    (4.125, 63),  # D#
    (4.5, 64),  # E
    (4.875, 65),  # F
    (5.25, 67),  # G
    (5.625, 65),  # Gb
    (6.0, 64),  # F
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: C7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0))

# Bar 3: C7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5))

# Bar 4: C7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C Eb G C (hanging on Eb) then resolve on G
sax_notes = [
    (1.5, 60),  # C
    (1.75, 64),  # Eb
    (2.0, 67),  # G
    (2.25, 60),  # C
    (3.0, 64),  # Eb
    (3.25, 67),  # G
    (3.5, 69),  # Bb
    (3.75, 67),  # G
    (4.0, 64),  # Eb
    (4.25, 69),  # Bb
    (4.5, 67),  # G
    (4.75, 64),  # Eb
    (5.0, 60),  # C
    (5.25, 67),  # G
    (5.5, 60),  # C
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[1], start=note[0], end=note[0] + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
