
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25),  # D5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=3.0),  # F5
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=3.0),  # Ab4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Continue with full quartet (3.0 - 4.5s)
# Bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),  # F5
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.75),  # Ab4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Continue with motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Continue with full quartet (4.5 - 6.0s)
# Bass: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last chord
piano_notes = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: End of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Drums: Continue pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
