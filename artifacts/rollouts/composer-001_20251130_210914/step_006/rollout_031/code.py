
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

# Bass: walking line in Fm, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # Db
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
]
piano.notes.extend(piano_notes)

# Sax: short motif. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25), # F
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75), # F
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.625), # Db
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
