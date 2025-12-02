
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=37, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=39, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),  # Bb
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),  # Bb
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),  # Bb
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.5),  # Bb
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.0),  # Bb
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=40, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=4.25, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Dante on sax (motif, start it, leave it hanging, come back and finish it)
sax_notes = [
    # Bar 2, beat 1 (motif start)
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=63, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),  # G
    # Bar 3, beat 1 (motif return)
    pretty_midi.Note(velocity=110, pitch=63, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.5),  # G
    # Bar 4, beat 1 (motif resolution)
    pretty_midi.Note(velocity=110, pitch=63, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=57, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=110, pitch=55, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=55, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=110, pitch=55, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=110, pitch=50, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
