
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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# F7, G7, Am7, D7
# Roots: F, G, A, D
# Fifths: C, D, E, A
# Chromatic approaches: E#, G#, Bb, C#

for bar in range(2, 5):
    start = bar * 1.5
    # Bass line
    if bar == 2:
        # F7: F, C, E#, G
        bass_notes = [pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=72, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=76, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # G7: G, D, G#, Bb
        bass_notes = [pretty_midi.Note(velocity=90, pitch=72, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=73, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=70, start=start + 1.125, end=start + 1.5)]
    elif bar == 4:
        # Am7: A, E, Bb, C
        bass_notes = [pretty_midi.Note(velocity=90, pitch=73, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=90, pitch=70, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=90, pitch=72, start=start + 1.125, end=start + 1.5)]
    bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# F7, G7, Am7, D7

for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # F7: F, A, C, E
        piano_notes = [pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=74, start=start + 0.375, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # G7: G, B, D, F
        piano_notes = [pretty_midi.Note(velocity=100, pitch=72, start=start, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=76, start=start + 0.375, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=69, start=start + 0.75, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)]
    elif bar == 4:
        # Am7: A, C, E, G
        piano_notes = [pretty_midi.Note(velocity=100, pitch=73, start=start, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=77, start=start + 0.75, end=start + 1.5),
                       pretty_midi.Note(velocity=100, pitch=76, start=start + 1.125, end=start + 1.5)]
    piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, A, G, D

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=73, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
