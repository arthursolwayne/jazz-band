
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Roots: F, Bb, B, Eb
# Roots (MIDI): 71 (F4), 67 (Bb4), 68 (B4), 64 (Eb4)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4 on 1
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Ab4 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Bb4 on 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Eb4 on 4

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb4 on 1
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Db4 on 2
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # B4 on 3
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # Bb4 on 4

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # A4 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # F4 on 3
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # Ab4 on 4
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Bm7 (B, D, F#, A)
piano_notes = []

# Bar 2 (1.5 - 3.0s)
# F7: F (71), A (74), C (69), E (67)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))  # E

# Bar 3 (3.0 - 4.5s)
# Bb7: Bb (67), D (65), F (71), Ab (69)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5))  # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5))  # Ab

# Bar 4 (4.5 - 6.0s)
# Bm7: B (71), D (65), F# (67), A (69)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0))  # B
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0))  # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0))  # F#
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0))  # A

piano.notes.extend(piano_notes)

# Sax: motif with tension and release
# Bar 2: F (71), Bb (67), Ab (69) -> F (71), Bb (67), B (68) - leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.0),  # B

    # Bar 3: Rest, let the tension breathe
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5),  # B

    # Bar 4: Repeat motif with variation
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
