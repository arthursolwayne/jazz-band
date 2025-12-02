
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
    # Hihat on every eighth
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=39, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=90, pitch=44, start=2.375, end=2.5625), # A#
    pretty_midi.Note(velocity=90, pitch=45, start=2.5625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=2.75, end=2.9375),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=47, start=2.9375, end=3.125), # B
    pretty_midi.Note(velocity=90, pitch=46, start=3.125, end=3.3125), # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=3.3125, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.6875),   # G
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Bbm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.6875),  # Db
    # Bar 3 - Dm7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.4375), # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.4375), # Eb
    # Bar 4 - Gm7 (F, G, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=69, start=2.8125, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.8125, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.8125, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=2.8125, end=3.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax - motif, short and singable
sax_notes = [
    # Bar 2 - motif start (F, Ab, Bb)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # Bb
    # Bar 3 - leave it hanging (rest)
    # Bar 4 - return and finish (F, Eb, F)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625), # F
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.6875, end=1.875), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),    # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),   # Hihat on 4
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.1875, end=2.375), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),   # Hihat on 4
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.9375, end=3.125), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.3125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),    # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),    # Hihat on 4
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
