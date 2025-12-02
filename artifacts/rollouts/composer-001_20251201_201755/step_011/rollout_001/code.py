
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
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (Fm), roots and fifths with chromatic approaches
# Fm: F, Ab, D, C
# Bar 2: F -> Eb -> D -> C
# Bar 3: Ab -> G -> F -> Eb
# Bar 4: D -> C -> Bb -> B
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [pretty_midi.Note(velocity=80, pitch=38, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=80, pitch=40, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=80, pitch=50, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=80, pitch=48, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=80, pitch=40, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=80, pitch=41, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=80, pitch=38, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=80, pitch=40, start=start + 1.125, end=start + 1.5)]
    elif bar == 4:
        notes = [pretty_midi.Note(velocity=80, pitch=50, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=80, pitch=48, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=80, pitch=47, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=80, pitch=49, start=start + 1.125, end=start + 1.5)]
    for note in notes:
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Ab7 (Ab, C, Eb, G)
# Bar 4: D7 (D, F#, A, C)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [pretty_midi.Note(velocity=100, pitch=53, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=60, start=start, end=start + 0.75)]
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=100, pitch=51, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=58, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=56, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.75)]
    elif bar == 4:
        notes = [pretty_midi.Note(velocity=100, pitch=60, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75),
                 pretty_midi.Note(velocity=100, pitch=60, start=start, end=start + 0.75)]
    for note in notes:
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F -> Ab -> Bb -> C (ascending)
# Play on beats 1 and 3 of bar 2, then leave it hanging on beat 2 of bar 3, then resolve on beat 3 of bar 4
note1 = pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.5 + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=51, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
note3 = pretty_midi.Note(velocity=110, pitch=50, start=3.0 + 0.75, end=3.0 + 0.75 + 0.375)
note4 = pretty_midi.Note(velocity=110, pitch=55, start=4.5 + 1.125, end=4.5 + 1.125 + 0.375)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
