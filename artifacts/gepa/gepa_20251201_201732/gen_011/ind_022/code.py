
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

# Marcus: Walking bass line in F (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),    # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),   # G2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),   # E2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),    # D2
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),    # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),   # G2
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),   # E2
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),    # D2
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),    # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),   # G2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),   # E2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),    # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),    # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),    # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),    # Eb
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),   # Ab
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),    # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),    # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),    # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),    # Bb
])
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),    # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),    # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),    # F
]
# Repeat the motif at the end
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),    # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5),    # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),    # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),    # F
])
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
