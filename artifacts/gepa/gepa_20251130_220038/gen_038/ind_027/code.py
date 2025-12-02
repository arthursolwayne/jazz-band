
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
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # F7 chord: F, A, C, E
    # Walking bass line with chromatic approach
    if bar == 2:
        notes = [pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=90, pitch=68, start=start + 0.375, end=start + 0.75),  # E
                 pretty_midi.Note(velocity=90, pitch=71, start=start + 0.75, end=start + 1.125),  # G
                 pretty_midi.Note(velocity=90, pitch=72, start=start + 1.125, end=start + 1.5)]  # A
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=90, pitch=72, start=start, end=start + 0.375),  # A
                 pretty_midi.Note(velocity=90, pitch=70, start=start + 0.375, end=start + 0.75),  # G#
                 pretty_midi.Note(velocity=90, pitch=69, start=start + 0.75, end=start + 1.125),  # F
                 pretty_midi.Note(velocity=90, pitch=68, start=start + 1.125, end=start + 1.5)]  # E
    elif bar == 4:
        notes = [pretty_midi.Note(velocity=90, pitch=68, start=start, end=start + 0.375),  # E
                 pretty_midi.Note(velocity=90, pitch=70, start=start + 0.375, end=start + 0.75),  # G#
                 pretty_midi.Note(velocity=90, pitch=72, start=start + 0.75, end=start + 1.125),  # A
                 pretty_midi.Note(velocity=90, pitch=71, start=start + 1.125, end=start + 1.5)]  # G
    bass.notes.extend(notes)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # F7 = F, A, C, E
    # Comp on 2 and 4
    if bar == 2:
        # 2nd beat (0.375 - 0.75)
        chord = [pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),  # F
                 pretty_midi.Note(velocity=90, pitch=71, start=start + 0.375, end=start + 0.75),  # G
                 pretty_midi.Note(velocity=90, pitch=72, start=start + 0.375, end=start + 0.75),  # A
                 pretty_midi.Note(velocity=90, pitch=68, start=start + 0.375, end=start + 0.75)]  # E
    elif bar == 3:
        # No comp on 3rd bar
        pass
    elif bar == 4:
        # 4th beat (1.125 - 1.5)
        chord = [pretty_midi.Note(velocity=90, pitch=69, start=start + 1.125, end=start + 1.5),  # F
                 pretty_midi.Note(velocity=90, pitch=71, start=start + 1.125, end=start + 1.5),  # G
                 pretty_midi.Note(velocity=90, pitch=72, start=start + 1.125, end=start + 1.5),  # A
                 pretty_midi.Note(velocity=90, pitch=68, start=start + 1.125, end=start + 1.5)]  # E
    piano.notes.extend(chord)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, D, F
# Starts on bar 2, ends on bar 4

notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0)   # F
]
sax.notes.extend(notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
