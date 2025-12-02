
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bass: Walking line in D, chromatic approaches, no repeated notes
# D Dorian: D, E, F#, G, A, B, C
bass_notes = [
    # Bar 2: D, F#, A, C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # A
    # Bar 3: B, D, F#, A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4: D, C, E, F#
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=66, start=5.625, end=6.0)   # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# G7: G, B, D, F
# C7: C, E, G, B
# F7: F, A, C, E
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # A
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # F
    # Bar 4: C7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0)    # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# D (62), F# (66), A (67), D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.125), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.125), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.875)   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
