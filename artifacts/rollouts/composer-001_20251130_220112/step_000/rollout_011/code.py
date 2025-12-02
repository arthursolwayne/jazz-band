
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

# Sax: D (D4), E (E4), B (B3), D (D4) - one short motif, make it sing
# Start at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # E4
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625), # B3
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # E4
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # B3
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25), # E4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625), # B3
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D4
]

sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice
# D (D2), E (E2), F (F2), G (G2), A (A2), B (B2), C# (C#3), D (D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),  # E2
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # G2
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125), # C#3
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # E2
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # A2
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # C5

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # C5

    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # C5

    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),   # A4
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # C5

    # Bar 4 (4.5 - 5.25s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # C5

    # Bar 4 (5.25 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # A4
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # D4
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # C5
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
