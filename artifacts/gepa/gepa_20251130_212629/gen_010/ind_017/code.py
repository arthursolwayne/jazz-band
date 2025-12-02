
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax starts the motif
# F7, D7, Bb7, G7 - descending chromatic line
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=85, start=1.875, end=2.25),  # D7
    pretty_midi.Note(velocity=100, pitch=83, start=2.25, end=2.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0),  # G7
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in F (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=60, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=60, pitch=46, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=60, pitch=47, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # F

    # Bar 3: D7 on 2 (2.875 - 3.25)
    pretty_midi.Note(velocity=80, pitch=59, start=2.875, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.875, end=3.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=3.25),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
]
drums.notes.extend(drum_notes)

# Bar 4: Sax continues the motif (leaves it hanging)
# Repeat the same notes but end with a rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=85, start=3.375, end=3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=83, start=3.75, end=4.125),  # Bb7
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5),  # G7
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in F (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=60, pitch=46, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=60, pitch=46, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=60, pitch=47, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Bb7 on 2 (3.875 - 4.25)
    pretty_midi.Note(velocity=80, pitch=55, start=3.875, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.875, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=3.875, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.875, end=4.25),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
