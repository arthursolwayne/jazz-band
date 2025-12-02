
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bars 2-4: Full quartet, starting at 1.5s

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625), # Db
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0)   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4 (bars 2-4)
# Bar 2: D7 on 2 (1.875 - 2.25)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # C
    # Bar 3: F7 on 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # D
    # Bar 4: G7 on 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=78, start=4.875, end=5.25)   # D#
]
piano.notes.extend(piano_notes)

# Sax (Dante) - melody in D, short motif, start it, leave it hanging, finish it
# Melody: D (62) - F (65) - Bb (71) - D (62) - F (65) - Bb (71) - D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 2.25
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625)
]
# Bar 3: 2.25 - 3.0
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
])
# Bar 4: 3.0 - 3.75
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125)
])
# Bar 5: 3.75 - 4.5
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875)
])
# Bar 6: 4.5 - 5.25
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625)
])
# Bar 7: 5.25 - 6.0
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375)
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
