
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bass: Walking line in Fm (F, Ab, D, C), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F, Ab, D, C
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # C2
    # Bar 3: Gb, Bb, Eb, Db
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Gb2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125), # Eb2
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),  # Db2
    # Bar 4: F, Ab, D, C
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # D5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # F5
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375), # Ab5
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # Eb5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (68), F (65), Gb (66) — incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625), # F4
    pretty_midi.Note(velocity=110, pitch=66, start=2.0625, end=2.25), # Gb4
    # Return and finish the motif at the end
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.4375), # F4
    pretty_midi.Note(velocity=110, pitch=68, start=5.4375, end=5.625), # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.8125), # F4
    pretty_midi.Note(velocity=110, pitch=74, start=5.8125, end=6.0),   # D5 (resolving up)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('fm_intro.mid')
