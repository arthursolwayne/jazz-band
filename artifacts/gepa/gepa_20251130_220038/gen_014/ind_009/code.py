
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Dm7 chord: D, F, A, C
# Walk Dm7, Dm7b5, Dm7, Dm7b5
bass_notes = []
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D
])
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
piano_notes = []
# Bar 2: comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # C
])
# Bar 3: comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # C
])
# Bar 4: comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.125),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=6.0, end=6.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=6.0, end=6.125),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.125),  # C
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - Eb - F - D, then repeat with a half-step shift
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.6875, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.1875, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.6875, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=5.8125, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat
    for i in range(8):
        start = bar_start + (i * 0.1875)
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
