
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm: F, Bb, E, Ab, D, G, C, F
# MIDI notes: 53 (F3), 50 (Bb3), 57 (E3), 55 (Ab3), 60 (D3), 62 (G3), 65 (C4), 53 (F3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb) - MIDI: 53, 55, 57, 59
# Bar 3: Bb7 (Bb, D, F, Ab) - MIDI: 50, 52, 53, 55
# Bar 4: Fm7 -> Cm7 (F, Ab, C, Eb -> C, Eb, G, Bb) - MIDI: 53, 55, 57, 59 -> 60, 62, 65, 67
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=55, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=59, start=1.5, end=1.75),
    # Bar 3: Bb7
    pretty_midi.Note(velocity=110, pitch=50, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.5),
    # Bar 4: Fm7
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.25),
    # Bar 4: Cm7
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75)
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53), Ab (55), Bb (50), F (53)
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=115, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=115, pitch=55, start=1.75, end=2.0),
    pretty_midi.Note(velocity=115, pitch=50, start=2.0, end=2.25),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=115, pitch=53, start=2.25, end=2.5),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=115, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=115, pitch=55, start=4.75, end=5.0),
    pretty_midi.Note(velocity=115, pitch=50, start=5.0, end=5.25),
    pretty_midi.Note(velocity=115, pitch=53, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
