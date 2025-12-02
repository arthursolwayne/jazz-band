
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=35, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=33, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=30, start=2.25, end=2.5),  # Bb
    # Bar 3: Fm7
    pretty_midi.Note(velocity=90, pitch=37, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=35, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=32, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=30, start=3.25, end=3.5),  # Bb
    # Bar 4: Fm7
    pretty_midi.Note(velocity=90, pitch=37, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=35, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=33, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=30, start=4.25, end=4.5),  # Bb
    # Bar 5: Fm7
    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=35, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=32, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=30, start=5.25, end=5.5),  # Bb
    # Bar 6: Fm7
    pretty_midi.Note(velocity=90, pitch=37, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=35, start=5.75, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=2.0, end=2.25),  # D
    # Bar 3: Fm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.25),  # D
    # Bar 4: Fm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=41, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=4.0, end=4.25),  # D
    # Bar 5: Fm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=5.0, end=5.25),  # D
    # Bar 6: Fm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=41, start=6.0, end=6.25),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=6.0, end=6.25),  # C
    pretty_midi.Note(velocity=90, pitch=46, start=6.0, end=6.25),  # D
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # G
    # Bar 5: Echo the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # Bb
    # Bar 6: Final resolution
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 6):
    pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5, end=bar * 1.5 + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5 + 1.125, end=bar * 1.5 + 1.5)
# Snare on 2 and 4
for bar in range(2, 6):
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 1.5 + 0.75, end=bar * 1.5 + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 1.5 + 1.875, end=bar * 1.5 + 2.0)
# Hi-hat on every eighth
for bar in range(2, 6):
    for i in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=bar * 1.5 + i * 0.375, end=bar * 1.5 + i * 0.375 + 0.125)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
