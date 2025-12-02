
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),  # A
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=85, pitch=76, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=3.5, end=3.75),  # C
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=95, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=85, pitch=78, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=5.0, end=5.25),  # C#
]
piano.notes.extend(piano_notes)

# Drums for Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Saxophone (Dante) - Motif starting on bar 2
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # B
    # Bar 3: Continue motif (leave it hanging)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # B
    # Bar 4: Finish motif
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Drums for Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.125, end=6.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Piano for Bar 3 (3.0 - 4.5s) - G7 on 2 and 4
piano_notes = [
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=85, pitch=76, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=3.5, end=3.75),  # C
    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=95, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=85, pitch=78, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=5.0, end=5.25),  # C#
]
piano.notes.extend(piano_notes)

# Bass line for Bar 3 and 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # A
]
bass.notes.extend(bass_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
