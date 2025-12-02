
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),   # Gb
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F7 - D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A7 - A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A7 - C#
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # A7 - E
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # A7 - G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F7 - D
]
piano.notes.extend(piano_notes)

# Drums (Bar 2-4)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),  # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare on 3
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),  # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

# Saxophone melody (Dante)
# Bar 2: Start with a motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # Bb
    # Bar 3: Leave it hanging and return
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),   # Bb
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
