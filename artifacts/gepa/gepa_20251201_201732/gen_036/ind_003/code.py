
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - Walking line in Fm (F - Ab - Bb - Db), chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),    # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),   # Gb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),   # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),    # Ab2 (root)
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),    # Bb2 (fifth)
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),   # B2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),   # Bb2
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),    # Db2 (fifth)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),    # Eb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),   # F3 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625),   # Gb3 (chromatic)
    pretty_midi.Note(velocity=80, pitch=54, start=5.625, end=6.0),    # G3 (fifth)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F - Ab - C - Db)
# Bar 3: Bb7 (Bb - D - F - Ab)
# Bar 4: Eb7 (Eb - G - Bb - Db)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Db)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # Ab3
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Db4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Bb3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # Eb3
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # Bb3
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Db4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C (Fm triad), one note per beat, staccato, then silence on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=110, pitch=58, start=2.25, end=2.625),  # Bb3
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F3 (repeat)
    pretty_midi.Note(velocity=110, pitch=58, start=5.25, end=5.625),  # Bb3
    pretty_midi.Note(velocity=110, pitch=60, start=6.0, end=6.375),  # C4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2
    if bar == 2:
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),   # Hihat
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),   # Hihat
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),   # Hihat
    # Bar 3
    elif bar == 3:
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),   # Hihat
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),   # Hihat
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),   # Hihat
    # Bar 4
    elif bar == 4:
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),   # Hihat
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),  # Snare
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),   # Hihat
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),   # Hihat

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
