
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.375),  # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=2.375, end=2.5),   # F
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.625),   # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=2.875, end=3.0),   # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Eb
    # Bar 3: Bb7 on beat 2 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),  # Ab
    # Bar 4: F7 on beat 2 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # Eb
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (64) -> Ab (65) -> C (67) -> Bb (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),   # Bb
]

sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Bar 3: 1.5 - 3.0s already covered
# Bar 4: 3.0 - 4.5s
drum_notes_bar4 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]

drums.notes.extend(drum_notes_bar4)

# Bar 4: Bass continues
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.625),   # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.625, end=3.75),   # G
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=3.875),   # Gb
    pretty_midi.Note(velocity=90, pitch=43, start=3.875, end=4.0),    # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.125),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),   # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.375),   # D
    pretty_midi.Note(velocity=90, pitch=40, start=4.375, end=4.5),    # C
]

bass.notes.extend(bass_notes_bar4)

# Bar 4: Piano continues
piano_notes_bar4 = [
    # Bar 4: F7 on beat 2 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # Eb
    # Bar 4: F7 on beat 4 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # Eb
]

piano.notes.extend(piano_notes_bar4)

# Bar 4: Sax continues
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),   # Bb
]

sax.notes.extend(sax_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
