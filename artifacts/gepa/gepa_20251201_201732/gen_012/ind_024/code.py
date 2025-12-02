
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # D2 (38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F#2 (43) - fifth
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    # E2 (41) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    # G2 (43) - fifth again
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chords each bar
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C#4
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F4
])
# Bar 4: Bm7 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A4
])
piano.notes.extend(piano_notes)

# Sax: motif
# Bar 2: Start the motif (D4, E4, F#4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625),  # F#4
]
# Bar 3: Leave it hanging
# Bar 4: Come back and finish it (G4, A4, B4)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.5625),  # B4
])
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Bass (3.0 - 4.5s)
# Walking line with chromatic approaches
bass_notes = [
    # A2 (55) - root
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),
    # C#3 (58) - third
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75),
    # C3 (52) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),
    # D3 (56) - root again
    pretty_midi.Note(velocity=90, pitch=56, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Bar 4: Bass (4.5 - 6.0s)
# Walking line with chromatic approaches
bass_notes = [
    # B2 (53) - root
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),
    # D3 (56) - third
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25),
    # C#3 (58) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),
    # D3 (56) - root again
    pretty_midi.Note(velocity=90, pitch=56, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
# G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F4
]
# Bar 4: Bm7 (B, D, F#, A)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A4
])
piano.notes.extend(piano_notes)

# Save the MIDI file
midi.write("jazz_piece.mid")
