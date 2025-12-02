
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.0625, end=2.25),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.4375, end=2.625),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.8125, end=3.0),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.1875),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.1875, end=3.375),  # C#
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.5625, end=3.75),  # D#
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    # F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),  # E
    # Bar 3
    # C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.75),  # B
    # Bar 4
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: Dante, short motif - F, Bb, D, F (F7 arpeggio)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.0),  # F
    # Leave it hanging, then come back
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=70, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
