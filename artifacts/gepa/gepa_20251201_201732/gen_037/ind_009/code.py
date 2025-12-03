
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
# Bass (Marcus): Walking line (F2 - Bb2, MIDI 38 - 43), roots and fifths with chromatic approaches
# Fm7: F, C, Ab, D (MIDI 38, 43, 40, 45)
# Bass line: F (38) -> Gb (40) -> C (43) -> Bb (40)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, start it, leave it hanging
# Fm7: F, Ab, Bb, C (MIDI 38, 40, 42, 43)
# Motif: F (38) -> Ab (40) -> Bb (42) -> F (38), but only play first three notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=40, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=42, start=1.75, end=1.875)
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Bass (Marcus): Fm7 -> Bb7 -> Cm7 -> Fm7
# Fm7: F (38), Ab (40), C (43), D (45)
# Bb7: Bb (42), D (45), F (38), Ab (40)
# Cm7: C (43), Eb (47), G (47), Bb (42)
# Fm7 again
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375)
]
piano.notes.extend(piano_notes)

# Sax (Dante): Continue motif, implied resolution
# Bb (42) -> D (45) -> F (38)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=45, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375)
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Bass (Marcus): Cm7 -> Fm7
# Cm7: C (43), Eb (47), G (47), Bb (42)
# Fm7: F (38), Ab (40), C (43), D (45)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Cm7 -> Fm7
# Cm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)
]
# Fm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0)
])
piano.notes.extend(piano_notes)

# Sax (Dante): Finish the motif, resolution
# C (43) -> Eb (47) -> G (47) -> F (38)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=43, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=47, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=47, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0)
]
sax.notes.extend(sax_notes)

# Drums for bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
