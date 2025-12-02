
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Marcus: Walking bass line (D minor)
bass_notes = [
    # D (2nd fret E string) - bar 2, beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # F (3rd fret E string) - bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    # G (4th fret E string) - bar 2, beat 3
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    # Bb (6th fret E string) - bar 2, beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    # C (8th fret E string) - bar 3, beat 1
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # D (2nd fret E string) - bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    # F (3rd fret E string) - bar 3, beat 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),
    # G (4th fret E string) - bar 3, beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    # D (2nd fret E string) - bar 4, beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    # F (3rd fret E string) - bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    # G (4th fret E string) - bar 4, beat 3
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),
    # Bb (6th fret E string) - bar 4, beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    # Bar 2, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    # Bar 3, beat 2: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    # Bar 3, beat 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    # Bar 4, beat 2: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    # Bar 4, beat 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing
# Melody: D - F# - Bb - D (bar 2, beats 1-4)
# Then repeat same motif on beat 1 of bar 3
# Leave it hanging on beat 3 of bar 4
sax_notes = [
    # Bar 2, beat 1: D
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Bar 2, beat 2: F#
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    # Bar 2, beat 3: Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # Bar 2, beat 4: D
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),
    # Bar 3, beat 1: D
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    # Bar 3, beat 2: F#
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    # Bar 3, beat 3: Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    # Bar 3, beat 4: D
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),
    # Bar 4, beat 1: D
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    # Bar 4, beat 2: F#
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    # Bar 4, beat 3: Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),
    # Bar 4, beat 4: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.875),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
