
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F#2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # C#5
]
piano.notes.extend(piano_notes)

# Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # C#5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=4.5),  # E5
]
piano.notes.extend(piano_notes)

# Bar 4: C7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# You: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - D4 (hanging on G4), then restate on D4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Drum fill for bar 4 (start at 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),  # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
