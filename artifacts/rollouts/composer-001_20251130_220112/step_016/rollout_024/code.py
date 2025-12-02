
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.1875),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=47, start=2.1875, end=2.375), # G
    pretty_midi.Note(velocity=90, pitch=48, start=2.375, end=2.5625), # G#
    pretty_midi.Note(velocity=90, pitch=46, start=2.5625, end=2.75), # F#
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=2.9375),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=2.9375, end=3.125), # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.125, end=3.3125), # A#
    pretty_midi.Note(velocity=90, pitch=49, start=3.3125, end=3.5),   # G#
    pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.6875),   # A
    # Bar 5
    pretty_midi.Note(velocity=90, pitch=52, start=3.6875, end=3.875), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.875, end=4.0625), # B
    pretty_midi.Note(velocity=90, pitch=51, start=4.0625, end=4.25),  # A#
    pretty_midi.Note(velocity=90, pitch=52, start=4.25, end=4.4375),  # Bb
    # Bar 6
    pretty_midi.Note(velocity=90, pitch=55, start=4.4375, end=4.625), # C
    pretty_midi.Note(velocity=90, pitch=56, start=4.625, end=4.8125), # C#
    pretty_midi.Note(velocity=90, pitch=54, start=4.8125, end=5.0),   # C
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.1875),   # C#
    # Bar 7
    pretty_midi.Note(velocity=90, pitch=53, start=5.1875, end=5.375), # B
    pretty_midi.Note(velocity=90, pitch=54, start=5.375, end=5.5625), # C
    pretty_midi.Note(velocity=90, pitch=52, start=5.5625, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=5.75, end=5.9375),  # B
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=55, start=1.875, end=2.0),   # C7 (F7)
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=85, pitch=46, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=95, pitch=55, start=2.625, end=2.75),  # C7 (F7)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=85, pitch=46, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=2.75),  # F
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=55, start=3.375, end=3.5),   # C7
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=85, pitch=46, start=3.375, end=3.5),   # E
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=95, pitch=55, start=4.125, end=4.25),  # C7
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=85, pitch=46, start=4.125, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.25),  # F
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=55, start=4.875, end=5.0),   # C7
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=85, pitch=46, start=4.875, end=5.0),   # E
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=95, pitch=55, start=5.625, end=5.75),  # C7
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=85, pitch=46, start=5.625, end=5.75),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=5.75),  # F
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D (F7)
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0),   # C
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=65, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.5625, end=2.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.9375),  # C
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.9375, end=3.125), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.3125), # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.3125, end=3.5),   # C
    # Bar 5
    pretty_midi.Note(velocity=110, pitch=62, start=3.6875, end=3.875), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.875, end=4.0625), # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.0625, end=4.25),  # C
    # Bar 6
    pretty_midi.Note(velocity=110, pitch=65, start=4.4375, end=4.625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.8125), # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.8125, end=5.0),   # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.1875),   # C
    # Bar 7
    pretty_midi.Note(velocity=110, pitch=62, start=5.1875, end=5.375), # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.375, end=5.5625), # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.5625, end=5.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=5.9375),  # D
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar (Bar 2-4)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)

drums.notes.extend([note for note in drums.notes if note not in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
