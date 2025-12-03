
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # G2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),  # F2

    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Bb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=37, start=4.125, end=4.5),  # F2

    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E5
]

# Bar 3: Bb7 (Bb D F A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A5
])

# Bar 4: C7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B5
])

# Left hand: Root and fifth, with chromatic approach
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # G3

    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # A3
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75), # Bb3

    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # F3
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # G3
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - Bb4 - C5 - F4 (half note, then rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=58, start=1.5, end=3.0),  # F4 (half note)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.75),  # Bb4 (eighth note)
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.5),  # C5 (eighth note)
    pretty_midi.Note(velocity=110, pitch=58, start=4.5, end=6.0),  # F4 (half note)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
