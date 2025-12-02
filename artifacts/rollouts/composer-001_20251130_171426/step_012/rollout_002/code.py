
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
    # Kick on 1 and 3: 0.0, 0.75, 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.875),
    # Snare on 2 and 4: 0.375, 1.125
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.25),
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

# Bars 2-4 (1.5 - 6.0s)
# Saxophone melody (D minor, one short motif)
sax_notes = [
    # Bar 2: D (72) on beat 1
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.625),
    # Bb (70) on beat 2
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.0),
    # F (65) on beat 3
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.375),
    # G (67) on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75),
    # Bar 3: Rest
    # Bar 4: Repeat the motif, transposed up a half step (D# / Eb)
    pretty_midi.Note(velocity=110, pitch=73, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.0)
]
sax.notes.extend(sax_notes)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2: D (62), Eb (63), F (65), G (67)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),
    # Bar 3: A (69), Bb (70), B (71), C (60)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=70, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=2.875),
    # Bar 4: D (62), Eb (63), F (65), G (67)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=63, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.375)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=85, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=75, pitch=60, start=1.875, end=2.0),
    # Bar 3: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=3.125, end=3.25),
    pretty_midi.Note(velocity=85, pitch=65, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.25),
    pretty_midi.Note(velocity=75, pitch=60, start=3.125, end=3.25),
    # Bar 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.5),
    pretty_midi.Note(velocity=85, pitch=65, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.375, end=4.5),
    pretty_midi.Note(velocity=75, pitch=60, start=4.375, end=4.5)
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.25),
    # Hi-hat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.125, end=bar_start + i * 0.125 + 0.125)

drums.notes.extend([note for note in [pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.125),
                                     pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.875),
                                     pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.5),
                                     pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.25)] + 
                                     [pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.125, end=bar_start + i * 0.125 + 0.125) for i in range(0, 8)] for bar in range(2, 5)])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
