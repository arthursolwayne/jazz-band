
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Marcus - Walking bass, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums - Bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)

# Dante - Sax solo, one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
