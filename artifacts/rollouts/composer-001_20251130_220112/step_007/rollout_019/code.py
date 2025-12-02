
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2 and 4
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # C
    # Bar 3: Bb7 on beat 2 and 4
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625),  # E
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif (G - Ab - F)
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=1.875),  # F
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=3.125, end=3.25),  # Ab
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
