
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus): D2 (MIDI 38) on 1 and 3, with chromatic approach on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=39, start=2.125, end=2.5),  # D#2 on 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875) # D2 on 3
]
bass.notes.extend(bass_notes)

# Piano (Diane): Cmaj7 (C-E-G-B) on beat 2, G7 (G-B-D-F) on beat 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0)   # F
]
piano.notes.extend(piano_notes)

# Sax (Dante): Melody starts with a short motif (D - F - G - D), then leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),   # F4 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),   # G4 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)    # D4 on 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass (Marcus): D2 (MIDI 38) on 1 and 3, with chromatic approach on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=39, start=3.875, end=4.25), # D#2 on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.625) # D2 on 3
]
bass.notes.extend(bass_notes)

# Piano (Diane): A7 (A-C#-E-G) on beat 2, Dm7 (D-F-A-C) on beat 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # C#
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.5)   # C
]
piano.notes.extend(piano_notes)

# Sax (Dante): Melody continues with a variation of the motif (D - E - F - D), then leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),   # E4 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),   # F4 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)    # D4 on 4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass (Marcus): D2 (MIDI 38) on 1 and 3, with chromatic approach on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=39, start=5.375, end=5.75), # D#2 on 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0)   # D2 on 3
]
bass.notes.extend(bass_notes)

# Piano (Diane): Gmaj7 (G-B-D-F#) on beat 2, C7 (C-E-G-B) on beat 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=6.0)   # B
]
piano.notes.extend(piano_notes)

# Sax (Dante): Melody finishes with a resolution (D - C - B - D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),   # C4 on 2
    pretty_midi.Note(velocity=100, pitch=59, start=5.5, end=5.75),   # B4 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.25)    # D4 on 4
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save("dante_intro.mid")
