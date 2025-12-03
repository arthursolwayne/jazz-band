
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus bass line: walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, C, Ab, D, Eb, Bb, Db, G
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25), # C2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125), # Db2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Diane piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab5
])
# Bar 4: Ab7 (Ab, C, Eb, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G5
])
piano.notes.extend(piano_notes)

# Little Ray drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
])

# Dante sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=1.96875), # F4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.4375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875),   # Gb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # F4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.3125),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.6875),   # Gb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625), # F4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.4375),  # Ab4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
