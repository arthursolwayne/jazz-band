
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.25),  # D
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=3.375, end=3.75),  # D
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - G - D (half notes on 1, 2, 3, 4 of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # D (1 and 2)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),   # F (3)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),   # G (4)
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5),   # D (1 of bar 3)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.25),   # F (2 of bar 3)
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=6.0),   # G (3 of bar 3, leaves on 4)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.25),    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.25),     # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.25),    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=5.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar.mid")
