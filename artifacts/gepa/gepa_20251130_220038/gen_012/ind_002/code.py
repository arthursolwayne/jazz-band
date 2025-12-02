
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
# Fm: F, Ab, Bb, D, Eb, G, etc. Walking line with chromatic passing tones

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),   # Bb
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, C
# Bb7 = Bb, Db, Eb, F
# Fm7 again
# Bb7 again

piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # Bb

    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Bb7

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),  # Bb

    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # Bb7

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # Bb

    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Bb7
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (64) -> Gb (63) -> F (64) -> E (60) -> D (59) -> C (58)

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=58, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
