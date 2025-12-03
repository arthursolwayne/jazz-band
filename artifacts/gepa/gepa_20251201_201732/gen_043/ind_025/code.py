
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43), walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 on beat 1, chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=40, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 to A2, chromatic approach to B2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=45, start=3.625, end=4.0),
    pretty_midi.Note(velocity=100, pitch=47, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: B2 to D3, chromatic approach to E3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=49, start=5.125, end=5.5),
    pretty_midi.Note(velocity=100, pitch=52, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
