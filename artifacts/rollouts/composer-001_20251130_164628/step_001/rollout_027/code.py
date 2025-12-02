
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
    # Hi-hat on every 8th
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # F -> Gb -> G -> Ab (chromatic approach to G)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=70, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),
    # G -> A -> Bb -> B (chromatic approach to B)
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=74, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=74, start=2.375, end=2.5),
    # B -> C -> Db -> D (chromatic approach to D)
    pretty_midi.Note(velocity=80, pitch=74, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=75, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=76, start=2.875, end=3.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 1
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.625),  # C
    # Bar 2: G7 on beat 2
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.0),  # D
    # Bar 2: C7 on beat 3 (no chord here, just a transition)
    # Bar 2: A7 on beat 4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=2.75),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.0),  # A
    # Bar 3: Repeat motif
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=74, start=2.375, end=2.5),  # A
    # Bar 4: End the motif
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=74, start=2.875, end=3.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3 and 4: Full quartet (3.0 - 6.0s)
# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=70, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),
    # G -> A -> Bb -> B
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=74, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=74, start=3.875, end=4.0),
    # B -> C -> Db -> D
    pretty_midi.Note(velocity=80, pitch=74, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=75, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=76, start=4.375, end=4.5),
    # D -> Eb -> E -> F
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=75, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=77, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.0),
    # F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=70, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=71, start=5.375, end=5.5),
    # G -> A -> Bb -> B
    pretty_midi.Note(velocity=80, pitch=72, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=73, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=74, start=5.875, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 1
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.125),  # C
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=3.875),  # D
    # Bar 3: C7 on beat 3 (no chord here, just a transition)
    # Bar 3: A7 on beat 4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=4.875, end=5.0),  # E
    # Bar 4: F7 on beat 1
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=5.0, end=5.125),  # C
    # Bar 4: G7 on beat 2
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=5.875),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=5.75, end=5.875),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=5.75, end=5.875),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=5.75, end=5.875),  # D
    # Bar 4: C7 on beat 3 (no chord here, just a transition)
    # Bar 4: A7 on beat 4
    pretty_midi.Note(velocity=100, pitch=74, start=5.875, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=5.875, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=5.875, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=5.875, end=6.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif again, but slightly varied
sax_notes = [
    # Bar 3: Start the motif
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.5),  # A
    # Bar 4: Repeat motif with variation
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.375),  # Eb
    pretty_midi.Note(velocity=110, pitch=74, start=5.375, end=5.5),  # A
    # Bar 4: End with a resolution
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=5.75, end=5.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=71, start=5.875, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
