
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
    # Hihat on every eighth
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

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),  # F#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.375, end=2.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.875, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=52, start=1.75, end=1.875),  # D
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.375),  # D#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.375),  # D
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=2.75, end=2.875),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=2.75, end=2.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=2.875, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
