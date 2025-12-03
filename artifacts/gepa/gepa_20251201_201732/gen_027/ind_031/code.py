
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax melody starts
# F7 - G7 - A7 - Bb7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=108, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=110, start=1.875, end=2.25),  # G7
    pretty_midi.Note(velocity=100, pitch=112, start=2.25, end=2.625),  # A7
    pretty_midi.Note(velocity=100, pitch=111, start=2.625, end=3.0),  # Bb7
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in F
# D2 - F2 - G2 - A2 - F2 - G2 - A2 - Bb2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # A2
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Bb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, resolve on last chord
# Bar 2: F7 - G7 - A7 - Bb7
# Voicings: F7 (F, A, C, Eb), G7 (G, B, D, F), A7 (A, C#, E, G), Bb7 (Bb, D, F, Ab)
# Comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),  # Eb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=80, pitch=81, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=80, pitch=83, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=2.625, end=2.875),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.0),    # A
    pretty_midi.Note(velocity=80, pitch=84, start=3.75, end=4.0),    # C#
    pretty_midi.Note(velocity=80, pitch=87, start=3.75, end=4.0),    # E
    pretty_midi.Note(velocity=80, pitch=81, start=3.75, end=4.0),    # G
]
piano.notes.extend(piano_notes)

# Bar 3: Drums again
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums again
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
