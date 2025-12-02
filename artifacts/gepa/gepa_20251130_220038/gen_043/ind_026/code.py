
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm
# Fm7 chord: F, Ab, C, Eb
# Chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: F -> Eb -> D -> C
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F (Ab in bass? No, F is root)
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # C
    # Bar 3: Bb -> A -> G -> F
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # F
    # Bar 4: Eb -> D -> C -> Bb
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, Eb
# Bar 2: chord on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Eb
    # Bar 3: chord on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # Eb
    # Bar 4: chord on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - 4 bars with a motif that sings and leaves it hanging
# Fm: F, Ab, C, Eb
# Motif: F -> Ab -> C -> Eb -> F (but leave it hanging at Eb)
sax_notes = [
    # Bar 2: F -> Ab -> C -> Eb -> F
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Eb
    # Bar 3: Rest
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Eb
    # Bar 4: Rest
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Eb
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("the_cellar_intro.mid")
