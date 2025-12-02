
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=73, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=3.0),  # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=2.0, end=2.25),  # D
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=80, pitch=73, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=77, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=80, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=81, start=3.5, end=3.75),  # F#
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=5.0, end=5.25),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (start at 1.5s)
sax_notes = [
    # First note: F (65) on beat 1
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    # Rest on beat 2
    # Third note: Ab (72) on beat 3
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),
    # Rest on beat 4
    # Repeat motif on beat 2 of bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),
    # Repeat motif on beat 2 of bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Bar 2
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 1.5 + i * 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=start, end=end))  # Hi-hat

# Bar 3
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 3.0 + i * 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=start, end=end))  # Hi-hat

# Bar 4
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.1875
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=start, end=end))  # Kick
    else:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=start, end=end))  # Snare
for i in range(8):
    start = 4.5 + i * 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=start, end=end))  # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
