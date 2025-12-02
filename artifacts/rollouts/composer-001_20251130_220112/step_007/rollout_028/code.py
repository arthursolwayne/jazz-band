
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
for i in range(8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet begins (1.5 - 3.0s)

# Marcus (bass): Walking line, chromatic approaches
# F7 chord: F A C E
# Walking bass line: F Eb G A Bb C
bass_notes = [
    (1.5, 71),  # F
    (1.75, 69),  # Eb
    (2.0, 72),  # G
    (2.25, 74),  # A
    (2.5, 71),  # Bb
    (2.75, 72),  # C
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Diane (piano): 7th chords, comp on 2 and 4
# F7 chord: F A C E
# Comp on beat 2 and 4

# F7 on beat 2 (1.75 - 2.0)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0),
])

# F7 on beat 4 (2.75 - 3.0)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=2.75, end=3.0),
])

# Little Ray (drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)

# Kick on 1 (1.5) and 3 (2.25)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))

# Snare on 2 (1.75) and 4 (2.75)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875))

# Hi-hat on every eighth
for i in range(8):
    start = 1.5 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus (bass): Walking line, chromatic approaches
# F7 chord: F A C E
# Walking bass line: F Eb G A Bb C
bass_notes = [
    (3.0, 71),  # F
    (3.25, 69),  # Eb
    (3.5, 72),  # G
    (3.75, 74),  # A
    (4.0, 71),  # Bb
    (4.25, 72),  # C
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Diane (piano): 7th chords, comp on 2 and 4
# F7 chord: F A C E
# Comp on beat 2 and 4

# F7 on beat 2 (3.25 - 3.5)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.5),
])

# F7 on beat 4 (4.25 - 4.5)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=79, start=4.25, end=4.5),
])

# Little Ray (drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)

# Kick on 1 (3.0) and 3 (3.75)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))

# Snare on 2 (3.25) and 4 (4.25)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375))

# Hi-hat on every eighth
for i in range(8):
    start = 3.0 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus (bass): Walking line, chromatic approaches
# F7 chord: F A C E
# Walking bass line: F Eb G A Bb C
bass_notes = [
    (4.5, 71),  # F
    (4.75, 69),  # Eb
    (5.0, 72),  # G
    (5.25, 74),  # A
    (5.5, 71),  # Bb
    (5.75, 72),  # C
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Diane (piano): 7th chords, comp on 2 and 4
# F7 chord: F A C E
# Comp on beat 2 and 4

# F7 on beat 2 (4.75 - 5.0)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=79, start=4.75, end=5.0),
])

# F7 on beat 4 (5.75 - 6.0)
piano.notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=79, start=5.75, end=6.0),
])

# Little Ray (drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4 (4.5 - 6.0s)

# Kick on 1 (4.5) and 3 (5.25)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))

# Snare on 2 (4.75) and 4 (5.75)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.75, end=5.875))

# Hi-hat on every eighth
for i in range(8):
    start = 4.5 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7: F A C E

# Motif: F (71) - Bb (71) - C (72) - F (71) -> leave it hanging on C (72)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5))

# Come back and finish it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0))

# Add some space at the end to let it hang
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
