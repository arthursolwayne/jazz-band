
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

# Bar 1: No piano, bass, or sax

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    # Bar 4: Eb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=54, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Bass (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=54, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Sax (Dante): Motif, sing it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
