
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
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) to A2 (MIDI 43)
# Walking line with chromatic approach
bass_notes = [
    # D2 (root) with chromatic approach on beat 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.0),
    # A2 (fifth) on beat 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    # D2 (root) on beat 4
    pretty_midi.Note(velocity=80, pitch=38, start=2.375, end=2.75)
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D-F-A-C) with open voicings, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),  # C5
    # Bar 3: Gm7 (G-Bb-D-F) on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.75),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.75),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.75),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.75),  # F5
    # Bar 4: Cm7 (C-Eb-G-Bb) on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Melody (Dm) - one short motif, sing it, leave it hanging, finish it
sax_notes = [
    # Bar 2: Dm
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),  # F4
    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    # Bar 4: resolve back to D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375)   # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: A2 (MIDI 43) to D2 (MIDI 38)
# Walking line with chromatic approach
bass_notes = [
    # A2 (fifth) with chromatic approach on beat 2
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.5),
    # D2 (root) on beat 3
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.875),
    # A2 (fifth) on beat 4
    pretty_midi.Note(velocity=80, pitch=43, start=3.875, end=4.25)
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G-Bb-D-F) with open voicings, comp on 2 and 4
piano_notes = [
    # Bar 3: Gm7 (G-Bb-D-F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5),  # F5
    # Bar 4: Cm7 (C-Eb-G-Bb) on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.25),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.25),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.25),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.25),  # Bb4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) to A2 (MIDI 43)
# Walking line with chromatic approach
bass_notes = [
    # D2 (root) with chromatic approach on beat 2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=37, start=4.875, end=5.0),
    # A2 (fifth) on beat 3
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.375),
    # D2 (root) on beat 4
    pretty_midi.Note(velocity=80, pitch=38, start=5.375, end=5.75)
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D-F-A-C) with open voicings, comp on 2 and 4
piano_notes = [
    # Bar 4: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0),  # C5
    # Bar 4: comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0),  # C5
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
