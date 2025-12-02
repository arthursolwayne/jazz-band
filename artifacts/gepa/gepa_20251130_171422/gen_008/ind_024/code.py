
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
]

piano.notes.extend(piano_notes)

# Sax: Melody, one short motif, make it sing
sax_notes = [
    # Bar 2 (start of motif)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),
    # Bar 4 (come back and finish it)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
