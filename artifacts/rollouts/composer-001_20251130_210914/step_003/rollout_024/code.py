
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif
# F7 (F A C E) -> F Bb D F (chromatic approach)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # F
]

# Bass: Walking line in F (F G Ab Bb B C D Eb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.625, end=1.75), # G
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=1.875), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0),  # Bb
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 (F A C E) on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0), # C
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.0), # E
    # D7 (D F A C) on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.75), # C
]

for note in sax_notes:
    sax.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Continue the rhythm
# Drums
for i in range(3):
    start = 3.0 + i * 1.5
    pretty_midi.Note(velocity=90, pitch=36, start=start, end=start+0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=start+0.75, end=start+1.125),  # Snare on 2
    for j in range(4):
        pretty_midi.Note(velocity=60, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)

# Bass: Continue the walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.125), # B
    pretty_midi.Note(velocity=80, pitch=65, start=3.125, end=3.25), # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=3.625, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # B7 (B D F# A) on beat 2
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.0), # B
    pretty_midi.Note(velocity=90, pitch=75, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0), # F#
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.0), # A
    # E7 (E G B D) on beat 4
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0), # E
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.0), # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax finishes the motif, returns to F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),  # F7
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums
for i in range(4):
    start = 4.5 + i * 1.5
    pretty_midi.Note(velocity=90, pitch=36, start=start, end=start+0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=start+0.75, end=start+1.125),  # Snare on 2
    for j in range(4):
        pretty_midi.Note(velocity=60, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)

# Bass: Final walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=4.875), # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Final 7th chord on 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0), # F7
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0), # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0), # C
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.0), # E
]
for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
