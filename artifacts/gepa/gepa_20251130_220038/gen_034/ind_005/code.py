
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

# Bass line - Marcus (walking line, chromatic approaches, no repeated notes)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=54, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # D7: F
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # D7: G
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # D7: Bb
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625), # G7: G
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625), # G7: B
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625), # G7: D
    pretty_midi.Note(velocity=90, pitch=83, start=2.25, end=2.625), # G7: F
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D7: D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D7: F
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # D7: G
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # D7: Bb
    # Bar 4 (3.75 - 4.5)
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.125), # G7: G
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125), # G7: B
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.125), # G7: D
    pretty_midi.Note(velocity=90, pitch=83, start=3.75, end=4.125), # G7: F
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D7: F
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # D7: G
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # D7: Bb
    # Bar 4 (5.25 - 6.0)
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625), # G7: G
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625), # G7: B
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625), # G7: D
    pretty_midi.Note(velocity=90, pitch=83, start=5.25, end=5.625), # G7: F
]
piano.notes.extend(piano_notes)

# Sax - Dante (melody: a whisper at first, then a cry)
# Bar 2: Start the motif
sax_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # Eb
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # Bb
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # Eb
    # Bar 4 (3.75 - 4.5)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # Bb
    # Bar 4 (4.5 - 5.25)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # Eb
    # Bar 4 (5.25 - 6.0)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
