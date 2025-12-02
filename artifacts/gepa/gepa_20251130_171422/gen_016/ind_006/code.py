
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: motif starting at 1.5s
# Dm7 -> F -> Eb -> D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
# D - Eb - F - G - A - Bb - C - D
# Each note is a quarter note
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 on 2.25, G7 on 4.5
piano_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # C
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Drums: continue same pattern for bars 2-4
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0 * (i + 1), note.end + 3.0 * (i + 1))
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
