
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 (beat 2)
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.625),  # D
    # Bar 3: F7 on 2 (beat 2)
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.125),  # D
    # Bar 4: F7 on 2 (beat 2)
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Drums in Bars 2-4
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
])

# Saxophone (Dante) - melody
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.625),  # Gb
    # Bar 3: Continue melody
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # E
    # Bar 4: Final statement
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_moment.mid")
