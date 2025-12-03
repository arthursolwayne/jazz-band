
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)     # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),    # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),   # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),   # G2 on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),    # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
    
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F5
    
    # Bar 4: Bm7 (B D F# A)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # A5
]
piano.notes.extend(piano_notes)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)     # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: Bar 2 (1.5 - 3.0s)
# Motif: D4 (62) -> F#4 (67) -> B4 (71) -> D5 (69) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625), # B4 on 3
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # D5 on 4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4 on 1 (next bar)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),    # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),   # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),   # G2 on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Bar 3 (3.0 - 4.5s)
# G7 (G B D F) resolved to C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F5
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)     # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: Bar 3 (3.0 - 4.5s)
# Motif continues: D4 (62) -> F#4 (67) -> B4 (71) -> D5 (69) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125), # B4 on 3
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # D5 on 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4 on 1 (next bar)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) to G2 (MIDI 43) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),    # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),   # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),   # G2 on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Bar 4 (4.5 - 6.0s)
# Bm7 (B D F# A) resolved to D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # A5
]
piano.notes.extend(piano_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),       # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)     # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: Bar 4 (4.5 - 6.0s)
# Motif continues: D4 (62) -> F#4 (67) -> B4 (71) -> D5 (69) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # F#4 on 2
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625), # B4 on 3
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # D5 on 4
    pretty_midi.Note(velocity=110, pitch=62, start=6.0, end=6.375)   # D4 on 1 (next bar)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
