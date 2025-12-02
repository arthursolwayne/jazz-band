
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (MIDI 41) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    # G2 (MIDI 43) - fifth
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # D2 (MIDI 38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C4
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Bb4
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax - short motif, make it sing
# Start it, leave it hanging, come back and finish it
# Motif: D4 (MIDI 62), F4 (MIDI 65), G4 (MIDI 67) -> D4 (MIDI 62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # D4 (come back)
]
sax.notes.extend(sax_notes)

# Add instruments to midi
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("waynes_moment.mid")
