
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Fm7 -> Bb7 -> Eb7 -> Ab7
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=35, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=39, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 on bar 2, Bb7 on bar 3, Eb7 on bar 4
piano_notes = [
    # Bar 2 (1.5-2.25s): Fm7
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.25),   # Db
    # Bar 3 (2.25-3.0s): Bb7
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),   # Gb
    # Bar 4 (3.0-3.75s): Eb7
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.75),   # B
    # Bar 4 (3.75-4.5s): Eb7 (again)
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.5),   # B
    # Bar 4 (4.5-5.25s): Eb7 (again)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=5.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=5.25),   # B
    # Bar 4 (5.25-6.0s): Eb7 (again)
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=6.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=6.0),   # B
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4, same pattern as bar 1
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: Melody (Bar 2)
# Fm -> Bb -> Eb -> Ab (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375), # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875), # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.9375), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.3125, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875), # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0), # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
