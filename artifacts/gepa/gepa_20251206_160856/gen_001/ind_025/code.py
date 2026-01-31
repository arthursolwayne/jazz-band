
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=21, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=23, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=20, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=21, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=23, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=25, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=24, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=25, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=27, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=28, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=26, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=28, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # E
]
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # D#
])
# Bar 4: Am7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # G
])
# Bar 2: Comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),  # E
])
# Bar 3: Comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # D#
])
# Bar 4: Comp on 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # G
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Start with F, then a tritone, then back to F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # F (back)
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # F (finish)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.625, end=bar_start + 3.0)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
