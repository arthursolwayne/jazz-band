
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.875),
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625),
    # Bar 4: Bm7 (B D# F# A)
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: Tenor motif in D, short and singable
sax_notes = [
    # Bar 2: F# (upper register) - start the motif
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875), # F#
    # Bar 3: B (a third higher) - leave it hanging
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625), # B
    # Bar 4: resolve back to D with a chromatic approach
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
