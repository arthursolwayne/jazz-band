
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),     # 1
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),     # 3
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),    # 2
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),     # 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.6875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=44, start=1.6875, end=1.875), # b9
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),   # 7
    pretty_midi.Note(velocity=80, pitch=41, start=2.0, end=2.1875),  # b7
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=40, start=2.1875, end=2.375), # b6
    pretty_midi.Note(velocity=80, pitch=39, start=2.375, end=2.5625), # b5
    pretty_midi.Note(velocity=80, pitch=38, start=2.5625, end=2.75),  # b4
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=2.9375),  # b6
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=41, start=2.9375, end=3.125), # b7
    pretty_midi.Note(velocity=80, pitch=43, start=3.125, end=3.3125), # root
    pretty_midi.Note(velocity=80, pitch=44, start=3.3125, end=3.5),   # b9
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),   # 7
    # Bar 4 (end)
    pretty_midi.Note(velocity=80, pitch=41, start=3.6875, end=3.875), # b7
    pretty_midi.Note(velocity=80, pitch=40, start=3.875, end=4.0),    # b6
    pretty_midi.Note(velocity=80, pitch=39, start=4.0, end=4.1875),   # b5
    pretty_midi.Note(velocity=80, pitch=38, start=4.1875, end=4.375), # b4
    pretty_midi.Note(velocity=80, pitch=40, start=4.375, end=4.5625), # b6
    pretty_midi.Note(velocity=80, pitch=41, start=4.5625, end=4.75),  # b7
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=4.9375),  # root
    pretty_midi.Note(velocity=80, pitch=44, start=4.9375, end=5.125), # b9
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.3125), # 7
    pretty_midi.Note(velocity=80, pitch=40, start=5.3125, end=5.5),   # b6
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.6875),   # b4
    pretty_midi.Note(velocity=80, pitch=39, start=5.6875, end=5.875), # b5
    pretty_midi.Note(velocity=80, pitch=40, start=5.875, end=6.0),    # b6
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.6875, end=1.875),  # Fm7
    pretty_midi.Note(velocity=90, pitch=40, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.6875, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.5625),  # Fm7
    pretty_midi.Note(velocity=90, pitch=40, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=37, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=41, start=2.375, end=2.5625),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=45, start=3.125, end=3.3125),  # Fm7
    pretty_midi.Note(velocity=90, pitch=40, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=37, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=41, start=3.125, end=3.3125),
]
piano.notes.extend(piano_notes)

# Sax: Motif, short, singable, ends on a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=40, start=2.375, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=41, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=3.25, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=39, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.0),   # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fmin_intro.mid")
