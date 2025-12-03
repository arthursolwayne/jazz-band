
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Fm7 - 1.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25), # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=56, start=2.25, end=2.625), # Bb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # F2

    # Bar 3 (Ab7 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75), # Eb3 (fifth)
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125), # D3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # Ab2

    # Bar 4 (Fm7 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625), # Bb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.0),  # D5

    # Bar 3: Ab7 (Ab, C, Eb, Gb)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # Gb4

    # Bar 4: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # F5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # Ab5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # C6
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # D6
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Gb - Ab - A (F, Gb, Ab, A), play on beat 1, leave on 2, return on 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Gb5
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # Ab5
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=3.0),   # A5

    # Leave it hanging (no note on beat 2)
    # Return on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Gb5
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # Ab5
    pretty_midi.Note(velocity=110, pitch=68, start=4.125, end=4.5),   # A5
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + (i + 1) * 0.1875)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
