
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (walking line in Fm, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: Fm (F, C, Eb)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # F
    # Bar 3: Bbm (Bb, F, Ab)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125), # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # Bb
    # Bar 4: Ebm (Eb, Bb, Db)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625), # A (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),
    # Bar 4: Ebm7 (Eb, Gb, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Saxophone: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (48), Ab (53), Bb (50), F (48) - spaced out over the first two bars
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=50, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=48, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=53, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=48, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=48, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2 (1.5-3.0s)
for start in [1.5, 1.875, 2.25, 2.625, 3.0]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375) if start % 1.5 == 0 else None
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875) if (start + 0.75) % 1.5 == 0 else None
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)

# Bar 3 (3.0-4.5s)
for start in [3.0, 3.375, 3.75, 4.125, 4.5]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375) if start % 1.5 == 0 else None
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875) if (start + 0.75) % 1.5 == 0 else None
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)

# Bar 4 (4.5-6.0s)
for start in [4.5, 4.875, 5.25, 5.625, 6.0]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375) if start % 1.5 == 0 else None
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875) if (start + 0.75) % 1.5 == 0 else None
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
