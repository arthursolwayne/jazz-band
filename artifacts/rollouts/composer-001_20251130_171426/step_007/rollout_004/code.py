
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Walking line, chromatic approaches)
# Fm7 = F Ab C Eb
# Chromatic approaches to each chord tone

# Bar 2: Fm7 (F Ab C Eb)
# Bass line: E - F - Gb - Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=1.5, end=1.75))  # E
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25))  # Gb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5))  # Ab

# Bar 3: Bb7 (Bb D F Ab)
# Bass line: A - Bb - B - C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=2.75, end=3.0))  # Bb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5))  # C

# Bar 4: Eb7 (Eb G Bb D)
# Bass line: D - Eb - F - G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=61, start=3.5, end=3.75))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5))  # G

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Fm7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=75, start=1.5, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0))  # Eb

# Bar 3: Bb7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=75, start=2.5, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=3.0))  # Ab

# Bar 4: Eb7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=4.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=4.0))  # D

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Gb - Ab - G (Fm scale, with a twist)

# Bar 2: Start motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0))  # Gb

# Bar 3: Let it hang, then return
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5))  # G

# Bar 4: Finish the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0))  # Gb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25))  # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5))  # G

# Drums for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25))

# Hi-hat on every eighth
for i in range(4, 12):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
