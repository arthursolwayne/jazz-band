
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),   # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # D#
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Ab
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante, short motif (start on beat 1 of bar 2)
sax_notes = [
    # Bar 2: F (53) -> A (60) on beat 1
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    # Bar 2: C (55) on beat 2
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625),
    # Bar 3: Bb (50) on beat 3
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=4.125),
    # Bar 4: E (58) on beat 4, end on beat 4 (6.0)
    pretty_midi.Note(velocity=110, pitch=58, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Output to file
midi.write("dante_intro.mid")
