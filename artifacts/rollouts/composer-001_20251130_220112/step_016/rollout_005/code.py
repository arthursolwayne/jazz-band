
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Tenor sax, short motif (Dm7 -> G7 -> Cm7 -> F7)
# Dm7: D F A C (D, F, A, C)
# G7: G B D F (G, B, D, F)
# Cm7: C Eb G Bb (C, Eb, G, Bb)
# F7: F A C Eb (F, A, C, Eb)
# Motif: D, F, A, C, G, B, D, F, C, Eb, G, Bb, F, A, C, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.5),   # Eb
]
sax.notes.extend(sax_notes)

# BASS: Marcus - walking line in Dm (D, C, Bb, B, A, G, F#, G, F, E, D, Eb, C, Bb, B, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),   # B
    pretty_midi.Note(velocity=90, pitch=58, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=56, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=90, pitch=57, start=2.375, end=2.5),   # G
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.875, end=3.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),   # C
]
bass.notes.extend(bass_notes)

# PIANO: Diane - comping on 2 and 4, 7th chords
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
piano_notes = [
    # Bar 2: Dm7 on 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=2.0),
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=95, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=95, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=95, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=95, pitch=65, start=2.75, end=3.0),
    # Bar 4: Cm7 on 2
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=63, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=66, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Tenor sax, continuation of motif, but with a twist (Dm7 -> G7 -> Cm7 -> F7)
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.375, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.0),   # Eb
]
sax.notes.extend(sax_notes)

# BASS: Marcus - walking line in Dm (D, C, Bb, B, A, G, F#, G, F, E, D, Eb, C, Bb, B, C)
# Same pattern as before, shifted by a bar
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=58, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=57, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=57, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=63, start=4.375, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=59, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes)

# PIANO: Diane - comping on 2 and 4, 7th chords
# G7 on 2
# Cm7 on 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=95, pitch=63, start=4.5, end=4.75),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Tenor sax, finish the motif with F7 (F, A, C, Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.0),   # Eb
]
sax.notes.extend(sax_notes)

# BASS: Marcus - walking line in Dm (D, C, Bb, B, A, G, F#, G, F, E, D, Eb, C, Bb, B, C)
# Same pattern as before, shifted by a bar
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=59, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=58, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=57, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=57, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=55, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=63, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=59, start=6.125, end=6.25),
    pretty_midi.Note(velocity=90, pitch=60, start=6.25, end=6.375),
    pretty_midi.Note(velocity=90, pitch=62, start=6.375, end=6.5),
]
bass.notes.extend(bass_notes)

# PIANO: Diane - comping on 2 and 4, 7th chords
# F7 on 2
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=95, pitch=63, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Add drum fills in bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.625),   # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
