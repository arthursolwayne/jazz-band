
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: F - D - Bb - G (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=3.0),  # F (half note)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # D (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # Bb (eighth note)
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # G (eighth note)
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # G (eighth note)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
# F - G - Ab - A - Bb - C - Db - D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comping on 2 and 4
# F7 on beat 2, F7 on beat 4
piano_notes = []
# F7 chord: F, A, C, E
for beat in [2, 4]:
    start = 1.5 + (beat * 0.375) - 0.125
    end = start + 0.25
    for pitch in [71, 76, 77, 81]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: C - Bb - A - G (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=4.5),  # C (half note)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # Bb (eighth note)
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A (eighth note)
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # G (eighth note)
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # G (eighth note)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
# F - G - Ab - A - Bb - C - Db - D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # Db
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comping on 2 and 4
# F7 on beat 2, F7 on beat 4
piano_notes = []
# F7 chord: F, A, C, E
for beat in [2, 4]:
    start = 3.0 + (beat * 0.375) - 0.125
    end = start + 0.25
    for pitch in [71, 76, 77, 81]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: F - D - Bb - G (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=6.0),  # F (half note)
    pretty_midi.Note(velocity=110, pitch=67, start=6.0, end=6.375),  # D (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=6.375, end=6.75),  # Bb (eighth note)
    pretty_midi.Note(velocity=110, pitch=66, start=6.75, end=7.125),  # G (eighth note)
    pretty_midi.Note(velocity=110, pitch=66, start=7.125, end=7.5),  # G (eighth note)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
# F - G - Ab - A - Bb - C - Db - D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=6.375, end=6.75),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=6.75, end=7.125),  # Db
    pretty_midi.Note(velocity=90, pitch=69, start=7.125, end=7.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comping on 2 and 4
# F7 on beat 2, F7 on beat 4
piano_notes = []
# F7 chord: F, A, C, E
for beat in [2, 4]:
    start = 4.5 + (beat * 0.375) - 0.125
    end = start + 0.25
    for pitch in [71, 76, 77, 81]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
for bar in [3, 4]:
    start = 1.5 + (bar * 1.5)
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),  # Snare on 4
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),  # Hihat on every 8th
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
