
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
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

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (D3 in MIDI) on beat 1
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),
    # F2 (F3) on beat 2
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),
    # A2 (A3) on beat 3
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),
    # C3 on beat 4 (chromatic approach to D)
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C5
]
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # F5
])
# Bar 4: Cmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # B4
])
piano.notes.extend(piano_notes)

# Sax (Dante): Melody
# Start with a short motif, leave it hanging, then come back to finish it
sax_notes = [
    # Start of motif: D (D4) on beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    # F (F4) on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.125),
    # A (A4) on beat 3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    # Leave it hanging on beat 4 (no note), then finish it in bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),
    # Complete the motif on beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # G2 (G3) on beat 1
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),
    # B2 (B3) on beat 2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),
    # D3 on beat 3
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),
    # F3 on beat 4 (chromatic approach to G)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F5
]
# Bar 4: Cmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # B4
])
# Bar 4: Resolving Dmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.5),  # C5
])
piano.notes.extend(piano_notes)

# Drums (Bar 3 and 4)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hats on every eighth
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

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax (Dante): Resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

# Bass (Marcus): Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (D3) on beat 1
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),
    # F2 (F3) on beat 2
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),
    # A2 (A3) on beat 3
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),
    # C3 on beat 4 (chromatic approach to D)
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Drums (Bar 4)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hats on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
