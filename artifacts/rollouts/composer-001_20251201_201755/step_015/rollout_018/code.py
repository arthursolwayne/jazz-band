
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5s - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> Eb2 (chromatic approach) -> F2 (fifth) -> G2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=41, start=2.125, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.875),
    # Bar 3: A2 (root) -> Bb2 (chromatic) -> C3 (fifth) -> D3 (chromatic)
    pretty_midi.Note(velocity=80, pitch=45, start=2.875, end=3.25),
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=49, start=3.875, end=4.25),
    # Bar 4: G2 (root) -> Ab2 (chromatic) -> Bb2 (fifth) -> C3 (chromatic)
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.625),
    pretty_midi.Note(velocity=80, pitch=43, start=4.625, end=4.875),
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625)
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
]
# Bar 3: Am7 (A C E G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # E5
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=3.0),  # G5
])
# Bar 4: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # F5
])
piano.notes.extend(piano_notes)

# Dante on sax: short motif, make it sing
# Motif: D4, E4, F4, E4 (sings like a question)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.5),
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.875)
]
sax.notes.extend(sax_notes)

# Bar 3: sax repeats the motif an octave higher
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=2.875, end=3.25),
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=75, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=74, start=3.875, end=4.25)
]
sax.notes.extend(sax_notes)

# Bar 4: sax returns with the first note of the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.625)
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
