
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

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # F
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # F
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=54, start=1.5, end=2.0),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.5),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=5.0),  # Bb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, G, F (MIDI 53, 48, 55, 53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=48, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),  # F (return)
    pretty_midi.Note(velocity=110, pitch=48, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=55, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=53, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(2):
    for offset in [0.0, 0.375, 0.75, 1.125]:
        pretty_midi.Note(velocity=100, pitch=36, start=1.5 + offset, end=1.5 + offset + 0.375)
        pretty_midi.Note(velocity=110, pitch=38, start=1.5 + offset + 0.375, end=1.5 + offset + 0.5)
        pretty_midi.Note(velocity=80, pitch=42, start=1.5 + offset, end=1.5 + offset + 0.1875)

# Bar 3 (3.0 - 4.5s)
for i in range(2):
    for offset in [0.0, 0.375, 0.75, 1.125]:
        pretty_midi.Note(velocity=100, pitch=36, start=3.0 + offset, end=3.0 + offset + 0.375)
        pretty_midi.Note(velocity=110, pitch=38, start=3.0 + offset + 0.375, end=3.0 + offset + 0.5)
        pretty_midi.Note(velocity=80, pitch=42, start=3.0 + offset, end=3.0 + offset + 0.1875)

# Bar 4 (4.5 - 6.0s)
for i in range(2):
    for offset in [0.0, 0.375, 0.75, 1.125]:
        pretty_midi.Note(velocity=100, pitch=36, start=4.5 + offset, end=4.5 + offset + 0.375)
        pretty_midi.Note(velocity=110, pitch=38, start=4.5 + offset + 0.375, end=4.5 + offset + 0.5)
        pretty_midi.Note(velocity=80, pitch=42, start=4.5 + offset, end=4.5 + offset + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
