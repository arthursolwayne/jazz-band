
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line with chromatic approaches
bass_notes = [
    # Bar 2 - Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.5),  # D

    # Bar 3 - Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=3.25, end=3.5),  # D

    # Bar 4 - Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # C

    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75),  # C

    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50) - Bb (46) - C (52) - D (50), then repeat a half step higher
sax_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.65),  # D
    pretty_midi.Note(velocity=110, pitch=46, start=1.65, end=1.8),  # Bb
    pretty_midi.Note(velocity=110, pitch=52, start=1.8, end=1.95),  # C
    pretty_midi.Note(velocity=110, pitch=50, start=1.95, end=2.0),  # D

    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=51, start=2.5, end=2.65),  # Eb
    pretty_midi.Note(velocity=110, pitch=47, start=2.65, end=2.8),  # B
    pretty_midi.Note(velocity=110, pitch=53, start=2.8, end=2.95),  # C#
    pretty_midi.Note(velocity=110, pitch=51, start=2.95, end=3.0),  # Eb

    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=110, pitch=50, start=3.5, end=3.65),  # D
    pretty_midi.Note(velocity=110, pitch=46, start=3.65, end=3.8),  # Bb
    pretty_midi.Note(velocity=110, pitch=52, start=3.8, end=3.95),  # C
    pretty_midi.Note(velocity=110, pitch=50, start=3.95, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: continue with same pattern
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4

    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
