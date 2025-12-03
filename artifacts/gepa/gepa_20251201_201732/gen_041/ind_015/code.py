
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (41) - chromatic approach to G2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    # G2 (43)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # B2 (46) - chromatic approach to C#3
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C#4
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # F5
])
# Bar 4: Bbm7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625),  # Ab5
])
# Resolving chord: D7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C#4
])
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F#4 (67), B4 (71), D5 (74) — 4 notes, no scale runs
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.0625, end=2.25),
    # Leave it hanging for a moment
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.4375),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=71, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
]
drums.notes.extend(drum_notes)

# Bar 3: Marcus continues walking line
# D2 (38), F#2 (41), G2 (43), B2 (46)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375)
]
bass.notes.extend(bass_notes)

# Bar 3: Diane plays Gm7 (G, Bb, D, F) and resolves on 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # F5
]
piano.notes.extend(piano_notes)

# Bar 4: Diane plays Bbm7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625),  # Ab5
]
piano.notes.extend(piano_notes)

# Final resolve on D7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C#4
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
