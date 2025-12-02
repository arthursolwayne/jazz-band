
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# F7 = F A C E
# B7 = B D# F# A
# C7 = C E G B
# G7 = G B D F
for bar in range(2, 4):
    start = bar * 1.5
    if bar == 2:
        chord = [53, 58, 60, 64]
    elif bar == 3:
        chord = [57, 62, 64, 67]
    else:
        chord = [60, 65, 67, 71]
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 0.375, end=start + 0.75))
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 1.125, end=start + 1.5))

# Sax: Short motif, start it, leave it hanging, come back and finish it
# F - G - A - F (F A Bb F)
motif = [65, 67, 68, 65]
note_lengths = [0.375, 0.375, 0.375, 0.375]
for i, note in enumerate(motif):
    if i == 0:
        start = 1.5
    elif i == 3:
        start = 3.0
    else:
        start = 1.5 + sum(note_lengths[:i])
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + note_lengths[i]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
