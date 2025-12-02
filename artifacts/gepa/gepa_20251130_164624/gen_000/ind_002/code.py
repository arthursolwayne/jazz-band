
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in Fm, chromatic approaches
# Fm: F, Ab, D, C
# Walking bass line: F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=2.375, end=2.5),   # C
    pretty_midi.Note(velocity=80, pitch=74, start=2.5, end=2.625),   # D
    pretty_midi.Note(velocity=80, pitch=75, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=2.875, end=3.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Fm7 (F, Ab, C, Eb)
# Bar 2: comp on beat 2 (0.75s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.625),  # Ab
    # Bar 2: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Sax melody, short motif, start it, leave it hanging
# Fm: F, Ab, D, C
# Motif: F -> Gb -> Ab -> C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line in Fm
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.5),   # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.875, end=4.0),   # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.0, end=4.125),   # D
    pretty_midi.Note(velocity=80, pitch=75, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=4.25, end=4.375),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=4.375, end=4.5),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Bar 3: comp on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.125),  # Ab
    # Bar 3: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Sax melody continuation, leave it hanging
# Fm: F -> Gb -> Ab -> C -> Eb -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in Fm
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=5.125, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=5.375, end=5.5),   # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.5, end=5.625),   # D
    pretty_midi.Note(velocity=80, pitch=75, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=5.875),  # E
    pretty_midi.Note(velocity=80, pitch=77, start=5.875, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Bar 4: comp on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.625),  # Ab
    # Bar 4: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.375),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Sax melody, finish the motif
# Fm: F -> Gb -> Ab -> C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=4.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.125),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=5.25),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
