
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=41, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=56, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=90, pitch=63, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5-2.0s)
    pretty_midi.Note(velocity=95, pitch=59, start=1.5, end=2.0),  # D7
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=2.0),
    # Bar 3 (2.0-2.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=2.0, end=2.5),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.5),
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.5),
    pretty_midi.Note(velocity=95, pitch=67, start=2.0, end=2.5),
    # Bar 4 (2.5-3.0s)
    pretty_midi.Note(velocity=95, pitch=59, start=2.5, end=3.0),  # D7
    pretty_midi.Note(velocity=90, pitch=61, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=95, pitch=64, start=2.5, end=3.0),
    # Bar 5 (3.0-3.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.5),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.5),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.5),
    # Bar 6 (3.5-4.0s)
    pretty_midi.Note(velocity=95, pitch=59, start=3.5, end=4.0),  # D7
    pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=4.0),
    pretty_midi.Note(velocity=95, pitch=64, start=3.5, end=4.0),
    # Bar 7 (4.0-4.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=4.0, end=4.5),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=66, start=4.0, end=4.5),
    pretty_midi.Note(velocity=95, pitch=67, start=4.0, end=4.5),
    # Bar 8 (4.5-5.0s)
    pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=5.0),  # D7
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=5.0),
    # Bar 9 (5.0-5.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=5.0, end=5.5),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.5),
    pretty_midi.Note(velocity=90, pitch=66, start=5.0, end=5.5),
    pretty_midi.Note(velocity=95, pitch=67, start=5.0, end=5.5),
    # Bar 10 (5.5-6.0s)
    pretty_midi.Note(velocity=95, pitch=59, start=5.5, end=6.0),  # D7
    pretty_midi.Note(velocity=90, pitch=61, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=6.0),
    pretty_midi.Note(velocity=95, pitch=64, start=5.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Dante (motif, make it sing)
sax_notes = [
    # Bar 2 (1.5-2.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G
    # Bar 3 (2.0-2.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # G
    # Bar 4 (2.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G
    # Bar 5 (3.0-3.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G
    # Bar 6 (3.5-4.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # G
    # Bar 7 (4.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # G
    # Bar 8 (4.5-5.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # G
    # Bar 9 (5.0-5.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # G
    # Bar 10 (5.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: fill the bar
# Bar 2 (1.5-2.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 3 (2.0-2.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.5),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 4 (2.5-3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=3.0),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 5 (3.0-3.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 6 (3.5-4.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=4.0),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 7 (4.0-4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.5),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 8 (4.5-5.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 9 (5.0-5.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.375, end=5.5),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.5),      # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 10 (5.5-6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=6.0),      # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
