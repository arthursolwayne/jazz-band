
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
# Fm7 -> Bb7 -> Eb7 -> Am7
# Roots: F, Bb, Eb, A
# Chromatic approaches: E#, B, D#, G
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=2.25), # G (fifth)
    pretty_midi.Note(velocity=70, pitch=37, start=2.25, end=2.625), # E (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=40, start=2.625, end=3.0),  # G (fifth)
    # Bar 3 (3.0s)
    pretty_midi.Note(velocity=70, pitch=43, start=3.0, end=3.375),  # Bb (root)
    pretty_midi.Note(velocity=70, pitch=45, start=3.375, end=3.75), # D (fifth)
    pretty_midi.Note(velocity=70, pitch=44, start=3.75, end=4.125), # C (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=45, start=4.125, end=4.5),  # D (fifth)
    # Bar 4 (4.5s)
    pretty_midi.Note(velocity=70, pitch=47, start=4.5, end=4.875),  # Eb (root)
    pretty_midi.Note(velocity=70, pitch=49, start=4.875, end=5.25), # G (fifth)
    pretty_midi.Note(velocity=70, pitch=48, start=5.25, end=5.625), # F# (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=49, start=5.625, end=6.0),  # G (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last beat of each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),  # Db
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bb7 -> Eb7 -> Am7
# Motif: F, Ab, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),  # C
    # Leave it hanging for a beat
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # C again, return
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),
    # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend([

    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),

])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
