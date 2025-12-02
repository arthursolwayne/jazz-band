
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
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Fm7 chord: F, Ab, C, Eb
# Walking bass line: F, Gb, Ab, A, Bb, B, C, Db, Eb, E, F, Gb
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        notes = [pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75),  # Gb
                 pretty_midi.Note(velocity=100, pitch=68, start=start + 0.75, end=start + 1.125),  # Ab
                 pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5)]  # A
    elif bar == 3:
        notes = [pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.375),  # Bb
                 pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75),  # B
                 pretty_midi.Note(velocity=100, pitch=71, start=start + 0.75, end=start + 1.125),  # C
                 pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5)]  # Db
    elif bar == 4:
        notes = [pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.375),  # Eb
                 pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75),  # E
                 pretty_midi.Note(velocity=100, pitch=71, start=start + 0.75, end=start + 1.125),  # F
                 pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5)]  # Gb
    bass.notes.extend(notes)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7
        notes = [pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=100, pitch=68, start=start, end=start + 0.375),  # Ab
                 pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.375),  # C
                 pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.375)]  # Eb
    elif bar == 3:
        # Ab7
        notes = [pretty_midi.Note(velocity=100, pitch=68, start=start, end=start + 0.375),  # Ab
                 pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.375),  # C
                 pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.375),  # E
                 pretty_midi.Note(velocity=100, pitch=63, start=start, end=start + 0.375)]  # Gb
    elif bar == 4:
        # Cm7
        notes = [pretty_midi.Note(velocity=100, pitch=76, start=start, end=start + 0.375),  # C
                 pretty_midi.Note(velocity=100, pitch=73, start=start, end=start + 0.375),  # Eb
                 pretty_midi.Note(velocity=100, pitch=81, start=start, end=start + 0.375),  # G
                 pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375)]  # Bb
    piano.notes.extend(notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db, Eb, E, F
# Motif: F, Gb, Eb, C (quarter notes)
# Start on bar 2, leave it hanging, come back on bar 4

# Bar 2: F, Gb
note1 = pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875)  # F
note2 = pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.25)  # Gb
sax.notes.extend([note1, note2])

# Bar 4: Eb, C
note3 = pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875)  # Eb
note4 = pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25)  # C
sax.notes.extend([note3, note4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
