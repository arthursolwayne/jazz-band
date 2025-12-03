
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5s - 3.0s)

# Bass: walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    # Bar 3: A2 (root), B2 (chromatic approach), C#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=46, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=49, start=3.125, end=3.5)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # C#4
]
# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.875), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875), # F#4
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.875), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.875), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.875), # B4
])
piano.notes.extend(piano_notes)

# Drums: Bar 2
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.125, end=3.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Sax: Bar 2-4
# Motif: D4 (start), F#4 (end), leave it hanging
# Then come back and finish it on the next bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875), # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.875), # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.8125, end=4.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Piano (same as before, no new notes)

# Bar 4: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.8125, end=5.0)
]
drums.notes.extend(drum_notes)

# Sax: Bar 3-4
# Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0), # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.125), # F#4
]
sax.notes.extend(sax_notes)

# Bar 4: Piano
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.875), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.875), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.875), # B4
]
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
