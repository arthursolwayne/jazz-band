
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Walking line in Dm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Rest on 1, comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    # Bar 3 - Rest on 1, comp on 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    # Bar 4 - Rest on 1, comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Motif
# Start on Dm7 (D F A C), play a short motif, leave it hanging, then come back
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=90, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend([n for n in drums.notes if n not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
