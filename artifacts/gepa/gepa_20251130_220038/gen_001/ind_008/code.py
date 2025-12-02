
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
# Walking line in Dm
bass_notes = [
    # Bar 2: Dm root, chromatic approach to F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C
    # Bar 3: Dm root, chromatic approach to G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # E
    # Bar 4: Dm root, chromatic approach to F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
# 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # C
    # Bar 2: comp on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),  # C
    # Bar 3: comp on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # C
    # Bar 4: comp on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - Eb - D (melodic minor), introduced in bar 2
sax_notes = [
    # Bar 2, beat 1: D
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Bar 2, beat 2: F
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),
    # Bar 2, beat 3: Eb
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),
    # Bar 2, beat 4: D (rest of the note)
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),
    # Bar 3, beat 1: D (reprise)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),
    # Bar 3, beat 2: F
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),
    # Bar 3, beat 3: Eb
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),
    # Bar 3, beat 4: D (finish the motif)
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
