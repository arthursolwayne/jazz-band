
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),  # A2 (fifth)
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625),  # C#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm9: D, F, A, C, E
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=75, pitch=69, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=70, pitch=72, start=1.5, end=2.25),  # E5
    # Bar 3: G7#9: G, B, D, F#, A#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=75, pitch=74, start=2.25, end=3.0),  # F#5
    pretty_midi.Note(velocity=70, pitch=76, start=2.25, end=3.0),  # A#5
    # Bar 4: Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=85, pitch=63, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=75, pitch=69, start=3.0, end=3.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First phrase: D4, Eb4, D4 (hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
    # Second phrase: F4, G4, A4, Bb4 (resolution)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
